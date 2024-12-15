from collections import defaultdict
import csv

#works with smal but csv.Error: line contains NUL for big file
def load_file(filepath):
    """Load a file and return its rows as a list of lists, splitting on commas."""
    with open(filepath, 'r') as file:
        return list(csv.reader(file))





def myjoin( f1, f2, f3, f4):
    """
    Implements the join operation as specified:
    - Join file1, file2, and file3 on their first field.
    - Join the second field of file3 with the first field of file4.
    - Output: first field of file4, first/second fields of file1, second field of file2, and second field of file4.
    """
    # Start time logging


    file1_path = f1
    file2_path = f2
    file3_path = f3
    file4_path = f4


    # Load files
    file1 = load_file(file1_path)
    file2 = load_file(file2_path)
    file3 = load_file(file3_path)
    file4 = load_file(file4_path)

    # Convert file4 into a dictionary for fast lookups
    file4_dict = defaultdict(list)
    for key, value in file4:
        file4_dict[key].append(value)

    # Index file1 and file2 by their first fields
    file1_dict = defaultdict(list)
    for a, b1 in file1:
        file1_dict[a].append(b1)

    file2_dict = defaultdict(list)
    for a2, c in file2:
        file2_dict[a2].append(c)

    # Perform the join operation
    output = []
    for a3, d in file3:
        if a3 in file1_dict and a3 in file2_dict:  # Ensure matches exist in file1 and file2
            for b1 in file1_dict[a3]:  # File1 values for matching key
                for c in file2_dict[a3]:  # File2 values for matching key
                    if d in file4_dict:  # Check if file3's second field matches file4's first field
                        for e in file4_dict[d]:  # Iterate over all matches in file4
                            output.append([d, a3, b1, c, e])

    # Sort output alphabetically (lexicographically by all fields)
    output.sort()

    return output

if __name__ == "__main__":
    import sys

    # Ensure correct usage
    if len(sys.argv) != 5:
        print("Usage: python3 gg2_v1.py <file1.csv> <file2.csv> <file3.csv> <file4.csv>")
        sys.exit(1)

    # Parse input filenames
    f1, f2, f3, f4 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Perform the join operation
    joined_data = myjoin(f1, f2, f3, f4)

    for row in joined_data:
        print(','.join(row))

