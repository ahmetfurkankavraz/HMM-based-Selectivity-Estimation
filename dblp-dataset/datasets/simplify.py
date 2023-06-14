import random

def select_random_lines(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]  # Remove leading/trailing whitespaces
    random_lines = random.sample(lines, num_lines)
    return random_lines

def save_list_to_file(strings, file_path):
    with open(file_path, 'w') as file:
        for string in strings:
            file.write(string + '\n')

file_path = 'authors.txt'  # Replace with the path to your file
num_lines = 800000  # Specify the number of random lines to select

random_lines = select_random_lines(file_path, num_lines)

# Print the randomly selected lines
save_list_to_file(random_lines, f"{num_lines}simplified.txt")
