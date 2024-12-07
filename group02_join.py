import time
from datetime import datetime
from collections import defaultdict
import yaml


def log_time(message):
    """Helper function to log time and message."""
    with open("runtime_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {message}\n")


def load_file(filepath):
    """Load a file and return its rows as a list of lists, splitting on commas."""
    with open(filepath, "r") as file:
        return [line.strip().split(",") for line in file]


def load_config(config_path="config.yaml"):
    """Load configuration settings from a YAML file."""
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)


def myjoin(config_path="config.yaml"):
    """
    Implements the join operation as specified:
    - Join file1, file2, and file3 on their first field.
    - Join the second field of file3 with the first field of file4.
    - Output: first field of file4, first/second fields of file1, second field of file2, and second field of file4.
    """
    # Start time logging
    log_time("Join operation started.")
    start_time = time.process_time()
    start_wall_time = time.time()

    config = load_config(config_path)

    file1_path = config['files']['file1']
    file2_path = config['files']['file2']
    file3_path = config['files']['file3']
    file4_path = config['files']['file4']
    log_file = config['log_file']

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

    # Write output to a file, joining the list into a comma-separated string
    with open("output.csv", "w") as out_file:
        for line in output:
            out_file.write(",".join(line) + "\n")

    # End time logging with process_time()
    end_time = time.process_time()
    end_wall_time = time.time()

    # Calculate CPU time and wall time
    cpu_time = end_time - start_time
    wall_time = end_wall_time - start_wall_time

    # Log the times
    log_time(f"Join operation completed.")
    log_time(f"CPU time: {cpu_time:.4f} seconds")
    log_time(f"Wall time: {wall_time:.4f} seconds")

    print(f"Join operation complete. Output saved to output.csv.")
    print(f"CPU time: {cpu_time:.4f} seconds")
    print(f"Wall time: {wall_time:.4f} seconds")

    print("Join operation complete. Output saved to output.csv.")
    return output

if __name__ == "__main__":
    print("Running myjoin...")
    output = myjoin("config.yaml")