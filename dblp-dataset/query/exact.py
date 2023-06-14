import random
import random, math

def select_random_authors():
    with open("authors.txt", "r") as file:
        all_authors = file.readlines()
    
    num_authors = len(all_authors)
    selected_authors = random.sample(all_authors, 100)
    
    return selected_authors

# Example usage
selected_authors = select_random_authors()
with open("queries.txt", "w") as file:
    for author in selected_authors:
        author = author.strip()
        file.write(author + '\n')
