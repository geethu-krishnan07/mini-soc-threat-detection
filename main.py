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

if failed_attempts >= 5:
    print("HIGH ALERT: Possible brute-force attack!")
elif failed_attempts >= 3:
    print("MEDIUM ALERT: Suspicious login activity!")
else:
    print("Status: Normal")