import sys
import tempfile
import os


def sort_file(file_path, sort_key):
    """Sort a file by the specified column."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Sort lines by the specified key (the first column in this case)
    sorted_lines = sorted(lines, key=lambda x: x.split(',')[sort_key])

    # Create a temporary file to store sorted lines
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='')
    temp_file.writelines(sorted_lines)
    temp_file.close()

    return temp_file.name


def join_files(file1, file2, join_column1, join_column2):
    """Join two sorted files on the specified columns."""
    joined_lines = []

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Create iterators for both files
        iter1 = iter(lines1)
        iter2 = iter(lines2)

        line1 = next(iter1, None)
        line2 = next(iter2, None)

        while line1 and line2:
            key1 = line1.split(',')[join_column1]
            key2 = line2.split(',')[join_column2]

            if key1 < key2:
                line1 = next(iter1, None)
            elif key1 > key2:
                line2 = next(iter2, None)
            else:
                # Join the lines and add to result
                joined_lines.append(line1.strip() + ',' + line2.strip() + '\n')
                line1 = next(iter1, None)
                line2 = next(iter2, None)

    return joined_lines


def main():
    if len(sys.argv) != 5:
        print("Usage: python script.py file1 file2 file3 file4")
        sys.exit(1)

    file1, file2, file3, file4 = sys.argv[1:5]

    # Sort the files by the first column
    sorted_f1 = sort_file(file1, 0)
    sorted_f2 = sort_file(file2, 0)
    sorted_f3 = sort_file(file3, 0)
    sorted_f4 = sort_file(file4, 0)

    # Perform the joins: file1 join file2 -> join file3 -> sort by 4th column -> join file4
    joined_1_2 = join_files(sorted_f1, sorted_f2, 0, 0)
    joined_1_2_3 = join_files(joined_1_2, sorted_f3, 0, 0)

    # Sort by 4th column
    joined_1_2_3_sorted = sorted(joined_1_2_3, key=lambda x: x.split(',')[3])

    # Join with file4 based on 4th column of previous result and first column of file4
    final_result = join_files(joined_1_2_3_sorted, sorted_f4, 3, 0)

    # Output the result
    for line in final_result:
        print(line.strip())

    # Clean up temporary files
    os.remove(sorted_f1)
    os.remove(sorted_f2)
    os.remove(sorted_f3)
    os.remove(sorted_f4)


if __name__ == "__main__":
    main()
