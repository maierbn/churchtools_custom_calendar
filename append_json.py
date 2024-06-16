import sys
import json

def append_json(source_file, dest_file):
    # Read the source JSON file
    with open(source_file, 'r') as sf:
        source_data = json.load(sf)
    
    # Read the destination JSON file
    with open(dest_file, 'r') as df:
        dest_data = json.load(df)
    
    # Append the source data to the destination data
    dest_data.append(source_data)
    
    # Write the updated destination data back to the file
    with open(dest_file, 'w') as df:
        json.dump(dest_data, df, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 append_json.py <source_file> <dest_file>")
        sys.exit(1)
    
    source_file = sys.argv[1]
    dest_file = sys.argv[2]

    append_json(source_file, dest_file)
