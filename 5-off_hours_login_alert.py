# ==========================================
# Off-hours Login Monitoring
# Logging in outside official working hours (8 AM - 4 PM) is a critical indicator,
# as it often means an employee's credentials were compromised by an intruder.
# ==========================================
login_hour = 2  # 2 AM

if login_hour > 16 or login_hour < 8:
    print("Warning: Attempt to log in outside working hours!")
