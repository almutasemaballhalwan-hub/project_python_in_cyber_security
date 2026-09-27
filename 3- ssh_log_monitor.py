# Monitor logs for SSH brute-force attacks to prevent unauthorized access.
log_entry = "Sep 27 14:32:11 server1 sshd: FAILED login for user root from 192.168.1.50"
if "FAILED" in log_entry:
    print("Warning A possible hacking operation has been found !")
