events = [
    {"user": "alice", "action": "ConsoleLogin", "success": False},
    {"user": "bob", "action": "ConsoleLogin", "success": False},
    {"user": "alice", "action": "ConsoleLogin", "success": False},
    {
        "user": "alice",
        "action": "AttachUserPolicy",
        "policy": "AdministratorAccess",
        "success": True,
    },
    {"user": "charlie", "action": "ConsoleLogin", "success": True},
    {"user": "alice", "action": "ConsoleLogin", "success": False},
    {"user": "bob", "action": "ConsoleLogin", "success": False},
    {"user": "bob", "action": "ConsoleLogin", "success": False},
    {
        "user": "bob",
        "action": "CreateUser",
        "success": True,
        "new_user": "temp_backdoor",
    },
]

failed_logins = {}

for e in events:
    if e["action"] == "ConsoleLogin" and e["success"] == False:
        user = e["user"]
        if user not in failed_logins:
            failed_logins[user] = 0
        failed_logins[user] += 1

suspicious_users = []

for e in events:
    user = e["user"]
    if failed_logins.get(user, 0) >= 3:
        if e["action"] in ["AttachUserPolicy", "CreateUser"]:
            if user not in suspicious_users:
                suspicious_users.append(user)

print("Users with suspicious activity:", suspicious_users)
