''' RETURN:

"data_files" → list of file names that end with "data", using .endswith("data").
"file_name_lengths" → dictionary mapping each file ID to the number of characters in its file name.
"large_files" → list of file names whose size is at least 100.

Requirements:

Use .items(), .endswith() and loops.
Manually count file-name characters.
No count(), no list comprehensions, no previous functions.
Do not modify files.
No print() inside the function.
Return exactly the three required keys.'''

files = {
    "F101": {"name": "salesdata", "owner": "Aarav", "size": 120},
    "F102": {"name": "userdata", "owner": "Maya", "size": 85},
    "F103": {"name": "report.txt", "owner": "Rohan", "size": 200},
    "F104": {"name": "customerdata", "owner": "Neha", "size": 150},
    "F105": {"name": "backupdata", "owner": "Kabir", "size": 95}
}

def analyze_file(files):
    data_files = []
    file_name_lengths = {}
    large_files = []

    for key,value in files.items():
        if value['name'].endswith('data'):
            data_files.append(value['name'])

        char_count_file = 0
        for char in value['name']:
            char_count_file += 1
        file_name_lengths[key] = char_count_file

        files_size = 0
        if value['size'] >= 100:
            large_files.append(value['name'])

    return {

        "data_files": data_files,
        "file_name_lengths": file_name_lengths,
        "large_files": large_files
    }

print(analyze_file(files))