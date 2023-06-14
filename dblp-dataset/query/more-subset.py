import random
import random, math

def generate_random_like_query(string):
    pattern = ''
    for i in range(len(string)):
        if random.random() < 0.55:
            pattern += string[i]
        else:
            pattern += '%'
    return pattern

def canonicalize_string(string):
    prev_char = ''
    canonicalized_string = ''
    for char in string:
        if char == '%' and '%' == prev_char:
            continue
        prev_char = char
        canonicalized_string += char
    canonicalized_string = canonicalized_string.strip('%')
    canonicalized_string = f"%{canonicalized_string}%"
    return canonicalized_string

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
        random_like_query = generate_random_like_query(author)
        canonicalize_str = canonicalize_string(random_like_query)
        file.write(canonicalize_str + '\n')
