import paramiko
import os
from dotenv import load_dotenv

load_dotenv()

# SSH connection details
hostname = os.getenv("HOST")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")  # Replace or use a secure method like getpass()

# Path to the project directory on the SSH server
project_dir = os.getenv("PROJECT_DIR")

# Local directory to save files
local_dir = "./data"
os.makedirs(local_dir, exist_ok=True)

# Connect to the SSH server
try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)

    # Navigate to the project directory
    sftp = ssh.open_sftp()
    sftp.chdir(project_dir)

    # List files in the directory
    files = sftp.listdir()
    print("Files on server:", files)

    # Download data.tar.xz if it exists
    if "data.tar.xz" in files:
        remote_file = os.path.join(project_dir, "data.tar.xz")
        local_file = os.path.join(local_dir, "data.tar.xz")
        print(f"Downloading {remote_file} to {local_file}")
        sftp.get(remote_file, local_file)

        # Extract the tar file locally
        import tarfile
        with tarfile.open(local_file, "r:xz") as tar:
            tar.extractall(local_dir)
        print(f"Extracted data to {local_dir}")

    sftp.close()
    ssh.close()

except Exception as e:
    print("An error occurred:", e)