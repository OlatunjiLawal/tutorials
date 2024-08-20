import json
import sys

def json_load(file_path):

    try:

        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error concerning the decoding of JSON from the file: {file_path}")
        return None

def main():
    
    file_path = input("Enter the file path to the JSON file.")
    data = json_load(file_path)

    if data is not None:
        
        print("Loaded JSON data successfully:")
        print(json.dumps(data, indent=4))
    else:
        print("Failed to load JSON.")

if __name__ == "__main__":
    main()