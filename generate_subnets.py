import os
import json

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
