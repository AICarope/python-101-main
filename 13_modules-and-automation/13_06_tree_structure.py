# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path

entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)