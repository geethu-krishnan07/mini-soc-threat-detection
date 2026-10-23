from datetime import datetime

print("=" * 45)
print("       MINI SOC THREAT DETECTION")
print("=" * 45)

print("SOC Monitoring Started...")
print("System Time:", datetime.now())
print("Status: Monitoring Active")
print(" ")
print("Failed Login Detection")

failed_attempts = int(input("Enter number of failed login attempts: "))

print("Failed Login Attempts:", failed_attempts)


print("\n----- SOC ALERT DETAILS -----")
print("Failed Login Attempts:", failed_attempts)

if failed_attempts >= 5:
    print("Severity: HIGH")
    print("Alert: Possible brute-force attack!")
elif failed_attempts >= 3:
    print("Severity: MEDIUM")
    print("Alert: Suspicious login activity!")
else:
    print("Severity: LOW")
    print("Alert: Normal login activity")
with open("alerts.txt", "a") as file:
    file.write(f"Time: {datetime.now()}\n")
    file.write(f"Failed Attempts: {failed_attempts}\n")

    if failed_attempts >= 5:
        file.write("Severity: HIGH\n")
    elif failed_attempts >= 3:
        file.write("Severity: MEDIUM\n")
    else:
        file.write("Severity: LOW\n")

    file.write("-" * 30 + "\n")