import os
from urllib import parse

ignoreList = ".git .github .gitignore generate_readme.py readme.md".split()

text = "# Leetcode Solutions\n\n"

for fileName in sorted(os.listdir()):
    if fileName.lower() not in ignoreList:
        text += f"[{fileName}]({parse.quote(fileName)})\n\n"

with open("Readme.md", "w") as fp:
    fp.write(text)
