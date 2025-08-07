import sys
import json

def append_json(source_file, dest_file):
    # Read the source JSON file
    with open(source_file, 'r') as file:
        source_data = json.load(file)["data"]
    
    # Read the destination JSON file
    with open(dest_file, 'r') as file:
        dest_data = json.load(file)["data"]
    
    # Append the source data to the destination data
    dest_data += source_data
    
    # Write the updated destination data back to the file
    with open(dest_file, 'w') as file:
        result = {
            "data": dest_data
        }
        json.dump(result, file, indent=4)

    print(f"[append_json.py] appended {source_file} ({len(source_data)} entries) to {dest_file} (now {len(dest_data)} entries)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 append_json.py <source_file> <dest_file>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    dest_file = sys.argv[2]

    append_json(source_file, dest_file)
