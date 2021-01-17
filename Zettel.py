import re

class Zettel:
    def __init__(self, text = "", name = "") -> None:
        self.text = text
        self.name = name
        self.tags = extract_tags(text)
        self.title = extract_title(text)
        super().__init__()


def extract_tags(text):
    pat = re.compile("#\w+[\s+\n]") # Checks for hashtags like #example
    tags = re.findall(pat, text)
    tags = [tag[:-1] for tag in tags]
    print(tags)

    return tags

def extract_title(text):
    print(len(text))
    import pdb; pdb.set_trace() #todo Pattern lädt nicht richtig
    pat = re.compile("^# .*$\n+") #looks for pattern "# this is a title \n"
    title = re.findall(pat, text)
    print(title)

    return title