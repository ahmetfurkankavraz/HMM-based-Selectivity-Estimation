import random
import random, math

def generate_random_prefixes(s):
    length = len(s)
    
    prefix_length = random.randint(1, 4)  # Random prefix length
    prefix = s[:prefix_length]  # Extract the prefix
    
    return prefix + "%"

def select_random_authors():
    with open("authors.txt", "r") as file:
        all_authors = file.readlines()
    
    num_authors = len(all_authors)
    selected_authors = random.sample(all_authors, 100)
    
    for i in range(0, 100):
        selected_authors[i] = selected_authors[i].strip()
        selected_authors[i] = generate_random_prefixes(selected_authors[i])

    return selected_authors

# Example usage
selected_authors = select_random_authors()
with open("queries.txt", "w") as file:
    for author in selected_authors:
        file.write(author + '\n')
