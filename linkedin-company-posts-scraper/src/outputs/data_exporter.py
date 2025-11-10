thonimport json

def export_data(data, filename="output.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)