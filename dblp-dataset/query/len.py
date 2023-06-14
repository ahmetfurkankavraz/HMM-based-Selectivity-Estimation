def select_random_authors():
    with open("authors.txt", "r") as file:
        all_authors = file.readlines()
    
    min_length = 100
    max_length = 0
    total_word_length = 0
    for author in all_authors:
        author = author.strip()
        min_length = min(min_length, len(author))
        max_length = max(max_length, len(author))
        total_word_length += len(author)    

    num_authors = len(all_authors)
    print(min_length)
    print(total_word_length / num_authors)
    print(max_length)

select_random_authors()