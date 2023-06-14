import psycopg2

# Database connection details
DB_HOST = 'localhost'
DB_NAME = 'advanceddb'
DB_USER = 'postgres'
DB_PASSWORD = '1234'
TABLE_NAME = 'simplifiedthousand'

# Function to read the file and return a list of strings
def read_strings_from_file(file_path):
    with open(file_path, 'r') as file:
        strings = file.readlines()
    strings = [string.strip() for string in strings]
    return strings

# Function to connect to the database and store strings in the table
def store_strings_in_database(strings):
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Create table if it doesn't exist
    create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (id SERIAL PRIMARY KEY, string TEXT);"
    cursor.execute(create_table_query)

    # Insert strings into the table
    for string in strings:
        insert_query = f"INSERT INTO {TABLE_NAME} (string) VALUES (%s);"
        cursor.execute(insert_query, (string,))

    conn.commit()
    cursor.close()
    conn.close()

# File path of the file containing strings
file_path = 'authors.txt'

# Read strings from file
strings = read_strings_from_file(file_path)

# Store strings in the database
store_strings_in_database(strings)

print ('Strings stored in the database:')