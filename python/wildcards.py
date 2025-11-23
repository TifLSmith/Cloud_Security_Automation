policies = [
    {"name": "AdminPolicy", "actions": ["s3:*", "ec2:*"]},
    {"name": "ReadOnlyPolicy", "actions": ["s3:GetObject"]},
    {"name": "DevPolicy", "actions": ["logs:*", "ec2:StartInstances"]},
]

wildcards_found = []

for p in policies:
    wildcards = []

    for action in p["actions"]:
        if "*" in action:
            wildcards.append(action)

    if wildcards:
        wildcards_found.append({
            "policy": p["name"],
            "wildcards": wildcards
        })

print(wildcards_found)