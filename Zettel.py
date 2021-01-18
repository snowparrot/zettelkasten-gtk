import re

class Zettel:
    def __init__(self, text = "", name = "") -> None:
        self.text = text
        self.name = name
        self.tags = extract_tags(text)
        self.title = extract_title(text)
        print(self.title)
        super().__init__()


def extract_tags(text):
    pat = re.compile("#\w+[\s+\n]") # Checks for hashtags like #example
    tags = re.findall(pat, text)
    tags = [tag[:-1] for tag in tags]
    print(tags)

    return tags

def extract_title(text):
    lines = text.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]