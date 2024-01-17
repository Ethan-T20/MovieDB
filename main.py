import csv

def search_csv(file_path, search_term, search_column):
    found_rows = []
    # Open the CSV file for reading
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        # Create a DictReader object, treating the first row as column names
        csv_reader = csv.DictReader(csvfile)
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Check if the search term is present in the specified column
            if search_term.lower() in row[search_column].lower():
                # Add the entire row to the list of found rows
                found_rows.append(row)
    return found_rows

def print_search_results(results):
    if results:
        print("Search Results:")
        # Print each found row
        for row in results:
            print(row)
    else:
        print("No matching rows found.")

def main():
    
    csv_file_path = 'imdb_top_1000.csv'
    
    # Prompt the user to enter the search term and column to search
    search_column = input("Enter search category(Title,Released_Year,Genre,Director): ")
    search_term = input("Enter search term: ")
    

    try:
        # Perform the search and print the results
        search_results = search_csv(csv_file_path, search_term, search_column)
        print_search_results(search_results)
    except KeyError:
        # Handle the case where the specified column is not found
        print(f"Column '{search_column}' not found in the CSV file.")

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
