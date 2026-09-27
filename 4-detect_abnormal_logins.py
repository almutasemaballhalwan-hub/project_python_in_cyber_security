# ==========================================
# Auto-Ban System
# We enforce a maximum attempt threshold (3 times) to avoid locking out
# legitimate users with typos, while preventing automated brute-force attacks.
# ==========================================
target_ip = "192.168.1.100"
failed_attempts = 4
max_allowed_attempts = 3

if failed_attempts > max_allowed_attempts:
    print("The IP has been Blocked: " + target_ip)
else:
    print("Login Successful for: " + target_ip)
