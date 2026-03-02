# Suspicious Login Log Analyzer

##  Project Overview

This project simulates a basic Security Operations Center (SOC) task by analyzing login logs to detect repeated failed authentication attempts. It identifies potentially malicious IP addresses exceeding a configurable failure threshold and generates a structured CSV report.

The objective is to demonstrate foundational security monitoring and brute-force detection logic.

---

##  Features

- Detects repeated failed login attempts
- Configurable detection threshold
- Flags suspicious IP addresses
- Generates CSV security report
- Lightweight and easy to extend

---

##  Technologies Used

- Python
- CSV module
- Collections (defaultdict)

---

##  Project Structure

├── log_analyzer.py
├── login_logs.txt
├── suspicious_report.csv (generated)
└── README.md

##  How It Works

1. Reads login log file
2. Counts failed attempts per IP address
3. Flags IPs exceeding threshold
4. Exports suspicious activity to CSV

---

##  How To Run

```bash
python log_analyzer.py

🧠 Security Concept Demonstrated

This project demonstrates:

Log analysis

Brute-force detection logic

Threshold-based alerting

Basic security monitoring automation

🔮 Future Improvements

Add timestamp analysis

Detect login frequency anomalies

Visualize failed attempts

Integrate with real log formats (Apache, SSH logs)

Build a dashboard interface

👤 Author

Wilson Augosto
IT – Network Systems
CCNA Certified
