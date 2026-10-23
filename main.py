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

if failed_attempts >= 3:
    print("ALERT: Multiple failed login attempts detected!")
else:
    print("Status: Normal")