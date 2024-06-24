#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline.
# 3. Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_destinations = our_routes.intersection(competitor_routes)
unique_destinations = our_routes.difference(competitor_routes)
unique_destinations2 = competitor_routes.difference(our_routes)
all_destinations = our_routes.union(competitor_routes)

print("Shared destinations: ", shared_destinations)
print("Our Unique Destinations: ", unique_destinations)
print("Their Unique Destinations: ", unique_destinations2)
print("All destinations: ", all_destinations)
