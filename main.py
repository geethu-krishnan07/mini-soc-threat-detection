from datetime import datetime

print("=" * 45)
print("       MINI SOC THREAT DETECTION")
print("=" * 45)

print("SOC Monitoring Started...")
print("System Time:", datetime.now())
print("Status: Monitoring Active")
print(" ")
print("Failed Login Detection")

failed_attempts = [1, 2, 3]

print("Failed Login Attempts:", len(failed_attempts))

if len(failed_attempts) >= 3:
    print("ALERT: Multiple failed login attempts detected!")