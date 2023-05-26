from geopy.distance import geodesic

locations = {
    1: (23.8728568, 90.3984184, "Uttara Branch"),
    2: (23.8513998, 90.3944536, "City Bank Airport"),
    3: (23.8330429, 90.4092871, "City Bank Nikunja"),
    4: (23.8679743, 90.3840879, "City Bank Beside Uttara Diagnostic"),
    5: (23.8248293, 90.3551134, "City Bank Mirpur 12"),
    6: (23.827149, 90.4106238, "City Bank Le Meridien"),
    7: (23.8629078, 90.3816318, "City Bank Shaheed Sarani"),
    8: (23.8673789, 90.429412, "City Bank Narayanganj"),
    9: (23.8248938, 90.3549467, "City Bank Pallabi"),
    10: (23.813316, 90.4147498, "City Bank JFP")
}

start_location = (23.8728568, 90.3984184)

# Calculate distances from start_location to all other locations
distances = {}
for location_id, location_data in locations.items():
    latitude, longitude, address = location_data
    distance = geodesic(start_location, (latitude, longitude)).kilometers
    distances[location_id] = distance

# Sort the locations based on distances in ascending order
sorted_locations = sorted(locations.items(), key=lambda x: distances[x[0]])

# Print the addresses in sorted order
for location_id, location_data in sorted_locations:
    _, _, address = location_data
    print(f"--> {location_id}: {address}")