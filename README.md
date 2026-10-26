# Task 2: Stock Portfolio Tracker (CodeAlpha)

A clean, robust Python application that calculates total investment value based on manually defined stock prices and user input.

---

## 📌 Project Overview

This project satisfies all requirements for **Task 2: Stock Portfolio Tracker**:
1. **Stock Price Configuration**: Uses a predefined dictionary mapping stock ticker symbols to their prices (e.g., `{"AAPL": 180.50, "TSLA": 250.00}`).
2. **User Input & Validation**: Allows users to enter multiple stock symbols and their corresponding share quantities, with case-insensitivity and input error handling.
3. **Calculations**: Accurately computes subtotal values (`quantity * price`) for each stock and accumulates the total investment value.
4. **Summary Display**: Displays an aligned tabular portfolio report in the console.
5. **File Handling & Export**: Allows users to export their summary report to `.txt` and/or `.csv` format.

---

## 🔑 Key Concepts Used

| Concept | Implementation in this Project |
| :--- | :--- |
| **Dictionary** | Used `STOCK_PRICES` to store ticker-to-price key-value pairs, and `holdings` to track user share counts. |
| **Input / Output** | `input()` for reading tickers and share quantities; formatted `print()` with alignment specifiers for tabular reports. |
| **Basic Arithmetic** | Multiplications for individual stock investments (`shares * price`) and cumulative addition for total portfolio value. |
| **File Handling** | Safe context managers (`with open(...) as f`) for writing formatted plain text (`.txt`) and structured tabular data (`csv.writer`). |

---

## 📁 Project Structure

```text
Stock_portfolio/
├── portfolio_tracker.py       # Main application script
├── test_portfolio_tracker.py  # Automated unit tests
├── portfolio_summary.txt      # Generated plain-text investment report
├── portfolio_summary.csv      # Generated CSV investment spreadsheet
└── README.md                  # Project documentation
```

---

## 🚀 How to Run

### 1. Run the Application
Execute the Python script in your terminal:
```bash
python3 portfolio_tracker.py
```

### 2. Run the Unit Tests
Run the test suite to verify calculation and file output logic:
```bash
python3 -m unittest test_portfolio_tracker.py
```

---

## 🖥️ Example Interactive Session

```text
============================================================
      WELCOME TO THE STOCK PORTFOLIO TRACKER (TASK 2)      
============================================================

=============================================
TICKER     | STOCK NAME / COMPANY |  PRICE ($)
---------------------------------------------
AAPL       | Apple Inc.           | $   180.50
TSLA       | Tesla Inc.           | $   250.00
MSFT       | Microsoft Corp.      | $   425.20
GOOGL      | Alphabet Inc.        | $   175.80
AMZN       | Amazon.com Inc.      | $   186.40
NVDA       | NVIDIA Corp.         | $   130.25
META       | Meta Platforms       | $   505.75
NFLX       | Netflix Inc.         | $   660.10
=============================================

Enter your stocks one by one.
Type 'DONE' or press Enter without typing a ticker when finished.

Enter Stock Ticker (e.g., AAPL) or 'DONE': AAPL
Enter quantity of shares for AAPL: 10
-> Added 10 shares of AAPL.
---------------------------------------------
Enter Stock Ticker (e.g., AAPL) or 'DONE': TSLA
Enter quantity of shares for TSLA: 5
-> Added 5 shares of TSLA.
---------------------------------------------
Enter Stock Ticker (e.g., AAPL) or 'DONE': DONE

============================================================
                PORTFOLIO SUMMARY REPORT
============================================================
TICKER     |   SHARES |  UNIT PRICE ($) |    SUBTOTAL ($)
------------------------------------------------------------
AAPL       |       10 | $        180.50 | $       1805.00
TSLA       |        5 | $        250.00 | $       1250.00
------------------------------------------------------------
TOTAL INVESTMENT VALUE:                $           3055.00
============================================================

File Export Options:
  [1] Save to Plain Text (.txt)
  [2] Save to CSV Spreadsheet (.csv)
  [3] Save to Both (.txt and .csv)
  [4] Skip saving
Select an option (1-4) [Default: 3]: 3
[OK] Saved text report to: portfolio_summary.txt
[OK] Saved CSV spreadsheet to: portfolio_summary.csv

Thank you for using Stock Portfolio Tracker!
```

---

## 📄 Output Files

### `portfolio_summary.txt`
```text
============================================================
         STOCK PORTFOLIO TRACKER - INVESTMENT REPORT
 Generated on: 2026-10-26 10:54:14
============================================================
TICKER     |   SHARES |  UNIT PRICE ($) |    SUBTOTAL ($)
------------------------------------------------------------
AAPL       |       10 | $        180.50 | $       1805.00
TSLA       |        5 | $        250.00 | $       1250.00
------------------------------------------------------------
TOTAL INVESTMENT VALUE:                $           3055.00
============================================================
```

### `portfolio_summary.csv`
```csv
Stock Ticker,Quantity (Shares),Unit Price (USD),Subtotal (USD)
AAPL,10,180.50,1805.00
TSLA,5,250.00,1250.00

TOTAL INVESTMENT,,,3055.00
```
