import csv
import geocoder
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Patch

def address_to_coordinates(address):
    # Define the image dimensions and corners
    image_width = 1820
    image_height = 1226
    bottom_right_lat, bottom_right_lon = 51.734810, -1.303312
    top_left_lat, top_left_lon = 51.781122, -1.193131

    # Geocode the address to get the latitude and longitude
    location = geocoder.osm(address)
    if location.ok:
        latitude = location.lat
        longitude = location.lng

        # Convert latitude and longitude to image coordinates
        x = int((longitude - bottom_right_lon) / (top_left_lon - bottom_right_lon) * image_width)
        y = int((latitude - top_left_lat) / (bottom_right_lat - top_left_lat) * image_height)
        if 0<x<1820 and 0<y<1226:
            return x, y
        else:
            return None
    else:
        print("Location not found.")
        return None


# Load the Oxford map image
image_path = "oxfordMap.png"
oxford_map = mpimg.imread(image_path)

# Create a scatter plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(oxford_map)

# Define the coordinates and food types
coordinates = {
    "Fast Food": [],
    "Coffee": [],
    "Chinese Food": [],
    "Bar": [],
    "Brunch": [],
    "Afternoon Tea": []
}

# Read addresses from the CSV file and populate coordinates
with open("foodData.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        food_type = row["type"]
        address = row["location"]
        coords = address_to_coordinates(address)
        if coords:
            coordinates[food_type].append(coords)


# Define the colors for each food type
colors = {
    "Fast Food": "yellow",
    "Coffee": "brown",
    "Chinese Food": "red",
    "Bar": "purple",
    "Brunch": "orange",
    "Afternoon Tea": "green"
}

# Plot scatter dots for each coordinate
legend_handles = []
for food_type, coords in coordinates.items():
    color = colors[food_type]
    for i, (x, y) in enumerate(coords):
        if i == 0:  # Only include the first dot in the legend
            legend_handles.append(Patch(color=color, label=food_type))
        ax.scatter(x, y, color=color, marker="o")

# Add a legend with custom handles
legend = ax.legend(handles=legend_handles, loc='upper right', shadow=True)
plt.savefig("oxFood.png")
# Show the plot
plt.show()
