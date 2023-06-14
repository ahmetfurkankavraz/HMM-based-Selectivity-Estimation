import random
import random, math

def generate_random_suffixes(s):
    length = len(s)
    
    suffix_length = random.randint(1, 4)  # Random suffix length
    suffix = s[length - suffix_length:]  # Extract the suffix
    
    return "%" + suffix

def select_random_authors():
    with open("authors.txt", "r") as file:
        all_authors = file.readlines()
    
    num_authors = len(all_authors)
    selected_authors = random.sample(all_authors, 100)
    
    for i in range(0, 100):
        selected_authors[i] = selected_authors[i].strip()
        selected_authors[i] = generate_random_suffixes(selected_authors[i])

    return selected_authors

# Example usage
selected_authors = select_random_authors()
with open("queries.txt", "w") as file:
    for author in selected_authors:
        file.write(author + '\n')
