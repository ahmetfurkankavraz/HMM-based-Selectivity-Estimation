import random
import random, math

import random

def select_non_overlapping_substrings(s):
    length = len(s)
    if length < 4:
        return None
    
    min_length = 2  # Minimum length of 2 or the remaining characters - (num_substrings - 1) * 3
    max_length = length - min_length * 2
    
    start_index_1 = random.randint(0, max_length)  # Random start index for the first substring
    end_index_1 = random.randint(start_index_1, length - min_length * 2)  # Random end index for the first substring
    
    start_index_2 = random.randint(end_index_1 + 1, length - min_length)  # Random start index for the second substring
    end_index_2 = random.randint(start_index_2 + min_length, length)  # Random end index for the second substring
    
    substring1 = s[start_index_1:end_index_1]  # Extract the first substring
    substring2 = s[start_index_2:end_index_2]  # Extract the second substring
    
    combined_string = f"%{substring1}%{substring2}%"  # Combine the substrings using "%"
    return combined_string


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
        random_like_query = select_non_overlapping_substrings(author)
        print(random_like_query)
        file.write(random_like_query + '\n')
