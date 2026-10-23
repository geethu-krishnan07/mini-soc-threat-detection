
from datetime import datetime

print("=" * 45)
print("       MINI SOC THREAT DETECTION")
print("=" * 45)

print("SOC Monitoring Started...")
print("System Time:", datetime.now())
print("Status: Monitoring Active")

print("\nFailed Login Detection")

try:
    failed_attempts = int(input("Enter number of failed login attempts: "))

    if failed_attempts < 0:
        print("Invalid input! Enter a positive number.")

    else:
        print("Failed Login Attempts:", failed_attempts)

        print("\n----- SOC ALERT DETAILS -----")
        print("Failed Login Attempts:", failed_attempts)

        if failed_attempts >= 5:
            severity = "HIGH"
            print("Severity: HIGH")
            print("Alert: Possible brute-force attack!")

        elif failed_attempts >= 3:
            severity = "MEDIUM"
            print("Severity: MEDIUM")
            print("Alert: Suspicious login activity!")

        else:
            severity = "LOW"
            print("Severity: LOW")
            print("Alert: Normal login activity")

        with open("alerts.txt", "a") as file:
            file.write(f"Time: {datetime.now()}\n")
            file.write(f"Failed Attempts: {failed_attempts}\n")
            file.write(f"Severity: {severity}\n")
            file.write("-" * 30 + "\n")

        print("\n----- SOC ALERT SUMMARY -----")

        with open("alerts.txt", "r") as file:
            logs = file.readlines()

        high_alerts = sum("Severity: HIGH" in line for line in logs)
        medium_alerts = sum("Severity: MEDIUM" in line for line in logs)
        low_alerts = sum("Severity: LOW" in line for line in logs)

        print("Total HIGH Alerts:", high_alerts)
        print("Total MEDIUM Alerts:", medium_alerts)
        print("Total LOW Alerts:", low_alerts)

except ValueError:
    print("Invalid input! Please enter a number.")
