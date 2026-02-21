import random
import datetime

# Open the file in write mode
f = open("app_server.log", "w")

# Capture the exact start time outside the loop
start_time = datetime.datetime.now()

# Generate 50 log events
for i in range(10000):
    # Add 'i' seconds to the start time so the clock moves forward
    time_added = datetime.timedelta(seconds=i)
    new_time = start_time + time_added
    timestamp = new_time.strftime("%Y-%m-%d %H:%M:%S")

    # Roll a 100-sided die
    roll = random.randint(1, 100)
    
    # The Attack (10% chance) - Hardcoded Attacker IP
    if roll <= 10:
         f.write(f"{timestamp} WARN Login Failed - User: Admin - IP: 10.10.10.5\n")
    # The Noise (90% chance)
    else:
         f.write(f"{timestamp} INFO Login Success - User: User123\n")

# Close and save the file
f.close()
