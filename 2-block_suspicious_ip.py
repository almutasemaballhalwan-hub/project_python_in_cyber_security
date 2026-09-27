# Revoked access for 10.0.0.5 due to detected unauthorized port scanning activity.
Allowed_ips = ["192.168.1.2", "192.168.1.10", "10.0.0.5"]
print(Allowed_ips)
Allowed_ips.remove("10.0.0.5")
print("The suspicious IP has been deleted")
print(Allowed_ips)
