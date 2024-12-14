import csv
from collections import defaultdict
import codecs

#doesnt work for small and big
def load_file(filepath):
    """Load a file and return its rows as a list of lists without using csv module."""
    with open(filepath, "r", errors="replace") as file:
        return list(csv.reader(codecs.open(file,"rU", "utf-16" )))


def myjoin(f1, f2, f3, f4):
    """
    Implements the join operation:
    - Join file1, file2, and file3 on their first field.
    - Join the second field of file3 with the first field of file4.
    - Output: first field of file4, first/second fields of file1, second field of file2, and second field of file4.
    """
    # Load files
    file1 = load_file(f1)
    file2 = load_file(f2)
    file3 = load_file(f3)
    file4 = load_file(f4)

    # Convert file4 into a dictionary for fast lookups
    file4_dict = defaultdict(list)
    for key, value in file4:
        file4_dict[key.strip()].append(value.strip())

    # Index file1 and file2 by their first fields
    file1_dict = defaultdict(list)
    for a, b1 in file1:
        file1_dict[a.strip()].append(b1.strip())

    file2_dict = defaultdict(list)
    for a2, c in file2:
        file2_dict[a2.strip()].append(c.strip())

    # Perform the join operation
    output = []
    for a3, d in file3:
        a3 = a3.strip()
        d = d.strip()
        if a3 in file1_dict and a3 in file2_dict:  # Matches in file1 and file2
            for b1 in file1_dict[a3]:
                for c in file2_dict[a3]:
                    if d in file4_dict:  # Match file3's second field with file4's first field
                        for e in file4_dict[d]:
                            output.append([d, a3, b1, c, e])

    # Sort output alphabetically
    #output.sort()

    return output


if __name__ == "__main__":
    import sys

    # Ensure correct usage
    if len(sys.argv) != 5:
        print("Usage: python3 gg2.py <file1.csv> <file2.csv> <file3.csv> <file4.csv>")
        sys.exit(1)

    # Parse input filenames
    f1, f2, f3, f4 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Perform the join operation
    joined_data = myjoin(f1, f2, f3, f4)
