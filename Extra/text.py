import csv


def print_rows(file_path, num_rows=5):
    """Print the first few rows of a CSV file."""
    print(f"\n--- {file_path} (first {num_rows} rows) ---")
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            reader.sort()
            for i, row in enumerate(reader):
                print(row)
                if i + 1 == num_rows:
                    break
    except Exception as e:
        print(f"Error reading {file_path}: {e}")


if __name__ == "__main__":
    import sys

    f1 = sys.argv[1]
    f2 = sys.argv[2]
    f3 = sys.argv[3]
    f4 = sys.argv[4]

    # Files to inspect
    files_to_check = [f1, f2, f3, f4]

    # Print rows from each file
    for file_path in files_to_check:
        print_rows(file_path, num_rows=5)