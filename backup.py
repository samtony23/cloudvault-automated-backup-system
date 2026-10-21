import subprocess

import shutil
import subprocess
from pathlib import Path

# Source folder containing files to back up
source_folder = Path("source_files")

# Destination folder for local backup copies
backup_folder = Path("backups")

# Create the backup folder if it does not exist
backup_folder.mkdir(exist_ok=True)

# Copy every file from source_files to backups
for file in source_folder.iterdir():
    if file.is_file():
        destination = backup_folder / file.name
        shutil.copy2(file, destination)

        print(f"Backup completed: {file.name}")

# Upload local backups to AWS S3
subprocess.run([
    "aws", "s3", "cp",
    str(backup_folder),
    "s3://cloudvault-backup-tony/",
    "--recursive",
    "--region", "eu-north-1"
], check=True)

print("All backups uploaded to AWS S3 successfully!")
