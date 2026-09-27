# ==========================================
# Upload Filter System
# We block uploads of executable file extensions (like .exe and .sh),
# because an attacker could run them on the server to execute malicious commands and take control.
# ==========================================
dangerous_extensions = [".exe", ".bat", ".sh", ".vbs"]
uploaded_file_ext = ".exe"

if uploaded_file_ext in dangerous_extensions:
    print("Alert: Malicious file upload blocked!")
