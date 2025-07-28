# 🔍 Job Log Analyzer

A Python-based utility that parses job logs, computes job durations, flags long-running jobs with appropriate warnings or errors, and displays the results in a well-formatted, color-coded table. Unit tests are included to validate core functionality.

---

## 📁 Project Structure

├── main.py # Entry point: parses log and prints analysis <br>
├── utils.py # Helper functions for parsing and analysis <br>
├── test_main.py # Unit tests for job analysis logic <br>
├── logs.log # Sample or input log file (not included here) <br>
├── requirements.txt # Dependencies for this project <br>
└── README.md # You're here! <br>

## 🧠 Features

- Parses job logs in CSV-like format:  
  `HH:MM:SS, Job Description, START|END, PID`
- Computes duration for each job using matching START and END entries
- Categorizes job durations:
  - ✅ **[OK]** if ≤ 5 minutes  
  - ⚠️ **[WARNING]** if > 5 and ≤ 10 minutes  
  - ❌ **[ERROR]** if > 10 minutes  
  - ℹ️ **[INFO] Incomplete log** for unmatched entries
- Displays results using the `tabulate` and `termcolor` libraries
- Unit test coverage with `unittest`

## 🖥️ How to Run
- Make sure logs.log exists in the same directory, then run:

```bash
python main.py
```

```bash
# Example output:
+-------------------+----------+----------+------------+
| Job               | Duration | Minutes  | Status     |
+-------------------+----------+----------+------------+
| ETL Job A-101     | 0:04:00  | 4.00     | [OK]       |
| ETL Job B-102     | 0:08:00  | 8.00     | [WARNING]  |
| ETL Job C-103     | 0:13:00  | 13.00    | [ERROR]    |
| ETL Job D-104     | Incomplete | -      | [INFO]     |
+-------------------+----------+----------+------------+
```

### 🧪 Running Tests
- All test cases for [OK], [WARNING], [ERROR], and incomplete logs should pass.
```bash
python test_main.py
```

### ✅ Prerequisites

Install dependencies:

```bash
pip install -r requirements.txt
```