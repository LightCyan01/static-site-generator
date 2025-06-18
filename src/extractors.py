import re

def extract_markdown_images(text):
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def extract_markdown_links(text):
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def extract_title(markdown: str):
    for line in markdown.splitlines():
        stripped_line = line.strip()
        if(stripped_line.startswith("# ")):
            return stripped_line[2:].strip()
        raise ValueError("No H1 header found")