"""The json.dumps() function that takes one argument: a piece of data that should
   be converted to the json format. The function returns a string, which can then
   write to a data file."""

from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

