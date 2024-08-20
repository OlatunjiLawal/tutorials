import json
import sys

dire_wolves = {
    "Grey Wind": {
        "Owner": "Robb Stark",
        "Status": "Deceased"
    },
    "Lady": {
        "Owner": "Sansa Stark",
        "Status": "Deceased"
    },
    "Nymeria": {
        "Owner": "Arya Stark",
        "Status": "Living"
    },
    "Summer": {
        "Owner": "Bran Stark",
        "Status": "Deceased"
    },
    "Shaggydog": {
        "Owner": "Rickon Stark",
        "Status": "Deceased"
    },
    "Ghost": {
        "Owner": "Jon Snow",
        "Status": "Living"
    }
}

with open('dire_wolves.json', 'w') as file:
    json.dump(dire_wolves, file, indent=4)



def json_load(file_path):

    try:

        with open('dire_wolves.json', 'r') as file:
            loaded_direwolves = json.load(file)
        return loaded_direwolves
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