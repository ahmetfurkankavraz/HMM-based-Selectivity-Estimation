import json

def check_valid(name):
    name_parts = name.split(' ')
    for name_part in name_parts:
        if name_part.endswith('.'):
            return False
    return True

# Read JSON data from file with explicit encoding
with open('dblp.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# Extract author names
authors = []
for obj in json_data:
    if 'author' in obj:
        for author in obj['author']:
            if check_valid(author):
                authors.append(author)

# Save author names in a different file
with open('authors.txt', 'w', encoding='utf-8') as output_file:
    for author in authors:
        output_file.write(author + '\n')

print("Author names saved in authors.txt file.")
