import random

def generate_queries(input_string):
    query = None
    length = len(input_string)
    
    while query is None:
        # num_substrings = random.randint(2, min(5, length // 3))  # Random number of substrings (2 to 5 or maximum based on string length)
        num_substrings = random.randint(2, 5)  # Random number of substrings (2 to 5)
        substrings = []
        remaining_length = length
        
        for _ in range(num_substrings):
            if remaining_length <= 0:
                break  # Break if there are no more remaining characters
            
            min_length = max(4, remaining_length - (num_substrings - 1) * 3)  # Minimum length of 2 or the remaining characters - (num_substrings - 1) * 3
            max_length = remaining_length - (num_substrings - 1) * 2  # Maximum length based on remaining characters
            
            if min_length > max_length:
                break  # Break if min_length becomes greater than max_length
            
            substring_len = random.randint(min_length, max_length)  # Random length for substring
            
            start_index = random.randint(0, length - substring_len)  # Random start index for substring
            end_index = start_index + substring_len  # Calculate end index for substring
            substring = input_string[start_index:end_index]  # Extract substring
            
            substrings.append(substring)
            remaining_length -= substring_len
        
        if len(substrings) >= 2:
            query = "%".join(substrings)  # Join substrings with "%"
            query = f"%{query}%"  # Add "%" at the start and end of the query
    
    return query

# Example usage
input_string = "Alexandre Kruszewski"
query = generate_queries(input_string)
print(query)
