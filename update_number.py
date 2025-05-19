import os
import datetime
import random
import subprocess

FILENAME = "number.txt"

# Lire le nombre actuel
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("0")

with open(FILENAME, "r") as f:
    current = int(f.read().strip())

# Incrémenter
new_number = current + 1
with open(FILENAME, "w") as f:
    f.write(str(new_number))

# Commit Git
commit_message = f"Update number to {new_number} on {datetime.date.today()}"
subprocess.run(["git", "add", FILENAME])
subprocess.run(["git", "commit", "-m", commit_message])
