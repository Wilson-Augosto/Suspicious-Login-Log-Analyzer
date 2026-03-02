import csv
from collections import defaultdict

LOG_FILE = "login_logs.txt"
THRESHOLD = 3  # change this to adjust detection sensitivity
OUTPUT_FILE = "suspicious_report.csv"

failed_attempts = defaultdict(int)

# Read log file
with open(LOG_FILE, "r") as file:
    for line in file:
        ip, status = line.strip().split(" - ")
        if status == "FAILED":
            failed_attempts[ip] += 1

# Detect suspicious IPs
suspicious_ips = {ip: count for ip, count in failed_attempts.items() if count >= THRESHOLD}

# Print results
print("Suspicious IP Addresses:")
for ip, count in suspicious_ips.items():
    print(f"{ip} - {count} failed attempts")

# Export to CSV
with open(OUTPUT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP Address", "Failed Attempts"])
    for ip, count in suspicious_ips.items():
        writer.writerow([ip, count])

print(f"\nReport saved to {OUTPUT_FILE}")