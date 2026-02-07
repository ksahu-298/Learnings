#Mini Project – Countdown Timer (with 1-second gap)
# Print a countdown before something exciting happens- using for loop, range() and time module.

import time
count= int(input("Enter the countdown start number: "))

print("\n The countdown begins now! \n")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print("Action! 💥💣")