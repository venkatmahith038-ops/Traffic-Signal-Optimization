from traffic import get_density, predict
from signal_controller import signal_time
from ambulance import ambulance_priority

roads = {
    "North": 35,
    "South": 85,
    "East": 62,
    "West": 18
}

print("=====================================")
print("SMART TRAFFIC SIGNAL OPTIMIZATION")
print("=====================================")

print("\nCurrent Vehicle Counts\n")

for road, count in roads.items():
    print(f"{road} Road : {count}")

print("\nPredicted Next Cycle\n")

predicted = {}
for road, count in roads.items():
    predicted[road] = predict(count)
    print(f"{road} Road : {predicted[road]}")

print("\nTraffic Density\n")

density = {}
for road, count in predicted.items():
    density[road] = get_density(count)
    print(f"{road} Road : {density[road]}")

print("\nOptimized Signal Timings\n")

for road in roads:
    print(f"{road} Road : {signal_time(density[road])} sec")

ambulance = input("\nIs ambulance detected? (yes/no): ").lower()

if ambulance == "yes":
    road = input("Enter Road (North/South/East/West): ").capitalize()
    ambulance_priority(road)

print("\nSystem Status : SUCCESS")