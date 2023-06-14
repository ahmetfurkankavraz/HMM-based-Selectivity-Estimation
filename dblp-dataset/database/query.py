import psycopg2

# Database connection details
DB_HOST = 'localhost'
DB_NAME = 'advanceddb'
DB_USER = 'postgres'
DB_PASSWORD = '1234'
TABLE_NAME = 'simplified'

# Function to perform a select query on the database table
def select_strings_from_database(query):
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    select_query = f"SELECT string FROM {TABLE_NAME} WHERE string LIKE '{query}';"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return len(rows)

def run_queries():
    with open("queries.txt", "r") as file:
        all_queries = file.readlines()

    with open("output.txt", "w") as output_file:
        for query in all_queries:
            query = query.strip()
            result = select_strings_from_database(query)
            output_file.write(f"{result}\n")

# Perform a select query on the database and write results to output.txt
run_queries()
