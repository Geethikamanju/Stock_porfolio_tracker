import csv
import os
from datetime import datetime

# ---------------------------------------------------------
# 1. HARDCODED STOCK PRICES DICTIONARY
# ---------------------------------------------------------
# Dictionary mapping stock ticker symbols to their unit price (USD)
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.00,
    "MSFT": 425.20,
    "GOOGL": 175.80,
    "AMZN": 186.40,
    "NVDA": 130.25,
    "META": 505.75,
    "NFLX": 660.10,
}


def display_available_stocks(stock_dict: dict[str, float]) -> None:
    """Displays the list of supported stocks and their configured prices."""
    print("\n" + "=" * 45)
    print(f"{'TICKER':<10} | {'STOCK NAME / COMPANY':<20} | {'PRICE ($)':>10}")
    print("-" * 45)
    names = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "MSFT": "Microsoft Corp.",
        "GOOGL": "Alphabet Inc.",
        "AMZN": "Amazon.com Inc.",
        "NVDA": "NVIDIA Corp.",
        "META": "Meta Platforms",
        "NFLX": "Netflix Inc.",
    }
    for ticker, price in stock_dict.items():
        company = names.get(ticker, "Stock Asset")
        print(f"{ticker:<10} | {company:<20} | ${price:>9.2f}")
    print("=" * 45 + "\n")


def calculate_portfolio_breakdown(
    holdings: dict[str, int], stock_dict: dict[str, float]
) -> tuple[list[dict], float]:
    """
    Calculates subtotal for each holding and total portfolio value.

    Returns:
        tuple containing:
        - list of item breakdown dicts (ticker, shares, price, subtotal)
        - total portfolio value as float
    """
    breakdown = []
    total_investment = 0.0

    for ticker, shares in holdings.items():
        price = stock_dict.get(ticker, 0.0)
        subtotal = shares * price
        total_investment += subtotal
        breakdown.append(
            {
                "ticker": ticker,
                "shares": shares,
                "price": price,
                "subtotal": subtotal,
            }
        )

    return breakdown, total_investment


def display_portfolio_summary(
    breakdown: list[dict], total_value: float
) -> None:
    """Prints a formatted summary table of current portfolio holdings."""
    print("\n" + "=" * 60)
    print("                PORTFOLIO SUMMARY REPORT")
    print("=" * 60)
    print(
        f"{'TICKER':<10} | {'SHARES':>8} | {'UNIT PRICE ($)':>15} | {'SUBTOTAL ($)':>15}"
    )
    print("-" * 60)

    for item in breakdown:
        print(
            f"{item['ticker']:<10} | {item['shares']:>8} | ${item['price']:>14.2f} | ${item['subtotal']:>14.2f}"
        )

    print("-" * 60)
    print(f"{'TOTAL INVESTMENT VALUE:':<38} ${total_value:>18.2f}")
    print("=" * 60 + "\n")


def save_to_txt(
    breakdown: list[dict],
    total_value: float,
    filename: str = "portfolio_summary.txt",
) -> str:
    """
    Saves portfolio summary report to a plain text (.txt) file.

    Demonstrates:
    - File open in write mode ('w') with UTF-8 encoding
    - String formatting and writing lines to file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("         STOCK PORTFOLIO TRACKER - INVESTMENT REPORT\n")
        file.write(f" Generated on: {timestamp}\n")
        file.write("=" * 60 + "\n")
        file.write(
            f"{'TICKER':<10} | {'SHARES':>8} | {'UNIT PRICE ($)':>15} | {'SUBTOTAL ($)':>15}\n"
        )
        file.write("-" * 60 + "\n")

        for item in breakdown:
            file.write(
                f"{item['ticker']:<10} | {item['shares']:>8} | ${item['price']:>14.2f} | ${item['subtotal']:>14.2f}\n"
            )

        file.write("-" * 60 + "\n")
        file.write(f"{'TOTAL INVESTMENT VALUE:':<38} ${total_value:>18.2f}\n")
        file.write("=" * 60 + "\n")

    return os.path.abspath(filename)


def save_to_csv(
    breakdown: list[dict],
    total_value: float,
    filename: str = "portfolio_summary.csv",
) -> str:
    """
    Saves portfolio summary report to a Comma-Separated Values (.csv) file.

    Demonstrates:
    - Standard library csv.writer
    - Structured tabular export with headers and rows
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(
            ["Stock Ticker", "Quantity (Shares)", "Unit Price (USD)", "Subtotal (USD)"]
        )

        # Write each holding row
        for item in breakdown:
            writer.writerow(
                [
                    item["ticker"],
                    item["shares"],
                    f"{item['price']:.2f}",
                    f"{item['subtotal']:.2f}",
                ]
            )

        # Write total summary row
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"{total_value:.2f}"])

    return os.path.abspath(filename)


def collect_user_holdings(stock_dict: dict[str, float]) -> dict[str, int]:
    """
    Interactively collects stock symbols and quantities from the user.
    Includes input validation and helpful prompts.
    """
    holdings: dict[str, int] = {}

    print("\nEnter your stocks one by one.")
    print("Type 'DONE' or press Enter without typing a ticker when finished.\n")

    while True:
        raw_ticker = input("Enter Stock Ticker (e.g., AAPL) or 'DONE': ").strip()

        # Exit condition
        if not raw_ticker or raw_ticker.upper() == "DONE":
            if not holdings:
                print("No stocks entered yet. Please add at least one stock.")
                continue
            break

        ticker = raw_ticker.upper()

        # Validate ticker against dictionary
        if ticker not in stock_dict:
            print(f"-> '{raw_ticker}' is not in the price list.")
            print(f"   Supported stocks: {', '.join(stock_dict.keys())}")
            continue

        # Get valid quantity
        while True:
            quantity_str = input(
                f"Enter quantity of shares for {ticker}: "
            ).strip()
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("-> Quantity must be a positive integer greater than zero.")
                    continue
                break
            except ValueError:
                print("-> Invalid input! Please enter a valid whole number for shares.")

        # Update holdings (add to existing if already present)
        if ticker in holdings:
            holdings[ticker] += quantity
            print(
                f"-> Updated {ticker}: total now {holdings[ticker]} shares."
            )
        else:
            holdings[ticker] = quantity
            print(f"-> Added {quantity} shares of {ticker}.")

        print("-" * 45)

    return holdings


def prompt_save_options(breakdown: list[dict], total_value: float) -> None:
    """Offers file saving options and handles saving according to user choice."""
    print("\nFile Export Options:")
    print("  [1] Save to Plain Text (.txt)")
    print("  [2] Save to CSV Spreadsheet (.csv)")
    print("  [3] Save to Both (.txt and .csv)")
    print("  [4] Skip saving")

    choice = input("Select an option (1-4) [Default: 3]: ").strip()

    if choice in ("1", ""):
        if choice == "":
            choice = "3"  # default to both if empty
        else:
            path_txt = save_to_txt(breakdown, total_value)
            print(f"[OK] Saved text report to: {path_txt}")
            return

    if choice == "2":
        path_csv = save_to_csv(breakdown, total_value)
        print(f"[OK] Saved CSV spreadsheet to: {path_csv}")
    elif choice == "3":
        path_txt = save_to_txt(breakdown, total_value)
        path_csv = save_to_csv(breakdown, total_value)
        print(f"[OK] Saved text report to: {path_txt}")
        print(f"[OK] Saved CSV spreadsheet to: {path_csv}")
    elif choice == "4":
        print("-> Export skipped.")
    else:
        print("-> Invalid choice. Export skipped.")


def main() -> None:
    """Main execution flow for the Stock Portfolio Tracker."""
    print("=" * 60)
    print("      WELCOME TO THE STOCK PORTFOLIO TRACKER (TASK 2)      ")
    print("=" * 60)

    # 1. Display available stocks and prices
    display_available_stocks(STOCK_PRICES)

    # 2. Collect user holdings
    holdings = collect_user_holdings(STOCK_PRICES)

    # 3. Calculate portfolio values
    breakdown, total_value = calculate_portfolio_breakdown(
        holdings, STOCK_PRICES
    )

    # 4. Display formatted summary table
    display_portfolio_summary(breakdown, total_value)

    # 5. Save results to file
    prompt_save_options(breakdown, total_value)

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
