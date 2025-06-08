
from textnode import TextNode, TextType

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