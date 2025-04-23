import os
import json

# Load categories for checking
categories_file = "./categories.json"
categories = [category["name"] for category in json.load(open(categories_file))["categories"]]

# Define the base directory containing the subnet data folders
base_directory = "./data"

# List to hold all subnet data
subnets = []

# Iterate over each subdirectory in the base directory
for subdir in os.listdir(base_directory):
    subdir_path = os.path.join(base_directory, subdir)
    if os.path.isdir(subdir_path):
        for filename in os.listdir(subdir_path):
            if filename.endswith(".json"):
                filepath = os.path.join(subdir_path, filename)
                with open(filepath, "r") as file:
                    subnet_data = json.load(file)

                    # Check all categories in subnet_data["categories"] is in the categories list
                    if "categories" in subnet_data:
                        for category in subnet_data["categories"]:
                            if category not in categories:
                                print(f"Category '{category}' in subnet {subdir} not found in {categories_file}")
                                exit(1)

                    # Add subnet_id based on the subdirectory name
                    subnet_data["subnet_id"] = int(subdir)
                    subnets.append(subnet_data)

# Sort the subnets list by subnet_id
subnets.sort(key=lambda x: x["subnet_id"])

# Define the output file path
output_file = "./subnets.json"

# Write the aggregated data to the output file
with open(output_file, "w") as outfile:
    json.dump(subnets, outfile, indent=4)

print(f"Aggregated subnets data has been written to {output_file}")
