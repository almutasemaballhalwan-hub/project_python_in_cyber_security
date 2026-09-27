# Security policy: Minimum 8 characters to mitigate brute-force attacks
password = input("Enter the your password :")
if len(password) < 8:
    print("password must be at least 8 characters long")
