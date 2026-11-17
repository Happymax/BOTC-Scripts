#!/bin/env python3
# Converter for YAML to JSON and vice versa
import json
import yaml

# TODO: Implement the conversion logic for JSON to YAML as well

if __name__ == "__main__":
    # Read the input file
    with open("input.yaml", "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    # Convert YAML to JSON
    json_data = json.dumps(yaml_data, indent=4)

    # Write the output file
    with open("output.json", "w") as json_file:
        json_file.write(json_data)

    print("Conversion from YAML to JSON completed successfully.")