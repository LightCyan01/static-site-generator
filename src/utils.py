
from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        else:
            parts = node.text.split(delimiter)
            
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter {delimiter}")
            
            for i, chunk in enumerate(parts):
                if not chunk:
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(chunk, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(chunk, text_type))
    
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        for alt, url in extract_markdown_images(text):
            marker = f"![{alt}]({url})"
            parts = text.split(marker, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url=url))
            
            text = after
            
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        text = node.text
        for alt, url in extract_markdown_links(text):
            marker = f"[{alt}]({url})"
            parts = text. split(marker, 1)
            before = parts[0]
            after = parts[1] if len(parts) > 1 else ""
            
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url=url))
            
            text = after
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match

def extract_markdown_links(text):
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match


def markdown_to_blocks(markdown):
    raw = markdown.split("\n\n")
    return [block.strip() for block in raw if block.strip()]