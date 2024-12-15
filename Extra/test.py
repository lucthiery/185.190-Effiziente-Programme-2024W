def search_in_file(file_path, search_string):
    with open(file_path, 'r') as file:
        for line in file:
            if search_string in line.strip():  # Check if the string is in the row
                print(line.strip())  # Print the whole row

# Example usage:
search_in_file('../data/f4.csv', '1H4YIF8Z6VD5ALVBZ')