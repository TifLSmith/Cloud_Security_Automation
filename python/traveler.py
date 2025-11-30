events = [
    {"user": "alice", "location": "US", "time": 1},
    {"user": "alice", "location": "Germany", "time": 3},
    {"user": "bob", "location": "US", "time": 2},
    {"user": "bob", "location": "US", "time": 5},
    {"user": "charlie", "location": "Japan", "time": 1},
    {"user": "charlie", "location": "Brazil", "time": 2},
]

last_seen_location = {}
impossible_travel = []

for e in events:
    user = e["user"]
    location = e["location"]
    time = e["time"]

    if user in last_seen_location:
       prev_location = last_seen_location[user]["location"]
       prev_time = last_seen_location[user]["time"]

       if prev_location != location and (time - prev_time) < 5:
          if user not in impossible_travel:
             impossible_travel.append(user)
    
    last_seen_location[user] = {"location": location, "time": time}

print ("Impossible travel detected:", impossible_travel)

