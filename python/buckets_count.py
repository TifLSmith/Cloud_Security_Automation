buckets = [
	{"name": "prod", "public": True},
	{"name": "prod", "public": False},
	{"name": "prod", "public": True}

]

count = 0
	
for b in buckets:
	    if b["public"]:
		count += 1

print("Public buckets:", count)
