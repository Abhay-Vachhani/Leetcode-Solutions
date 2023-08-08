import os
from urllib import parse

ignoreList = ".git .github .gitignore generate_readme.py readme.md".split()

text = "# Leetcode Solutions\n\n"
text += "Leetcode Profile: https://leetcode.com/abhayvachhani28/\n\n---\n\n"
# Rank on 2023-08-08: 2,700,474

for fileName in sorted(os.listdir()):
    if fileName.lower() not in ignoreList:
        text += f"[{fileName}]({parse.quote(fileName)})\n\n"

with open("Readme.md", "w") as fp:
    fp.write(text)
