
from parentnode import ParentNode
from textnode import TextNode, TextType
from utils import text_node_to_html_node, text_to_children
from blocks import block_to_block_type, BlockType

def markdown_to_blocks(markdown):
    raw = markdown.split("\n\n")
    return [block.strip() for block in raw if block.strip()]

def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    
    for block in blocks:
        blocktype = block_to_block_type(block)
        
        if blocktype == BlockType.HEADING:
            level = len(block) - len(block.lstrip('#'))
            text = block[level + 1 :]
            children = text_to_children(text)
            node = ParentNode(tag=f"h{level}", children=children)
            
        elif blocktype == BlockType.CODE_BLOCK:
            lines = block.splitlines()
            
            code = "\n".join(lines[1:-1]) + "\n"
            text_node = TextNode(code, TextType.CODE)
            code_leaf = text_node_to_html_node(text_node)
            node = ParentNode(tag="pre", children=[code_leaf])
        
        elif blocktype == BlockType.QUOTE:
            inner = [line[1:].lstrip() for line in block.splitlines()]
            text = "\n".join(inner)
            children = text_to_children(text)
            node = ParentNode(tag="blockquote", children=children)
        
        elif blocktype == BlockType.UNORDERED_LIST:
            items = []
            
            for line in block.splitlines():
                text = line[2:]
                items.append(ParentNode(tag="li", children=text_to_children(text)))
            node = ParentNode(tag="ul", children=items)
                
        elif blocktype == BlockType.ORDERED_LIST:
            items = []
            
            for line in block.splitlines():
                _, rest = line.split('. ', 1)
                items.append(ParentNode(tag="li", children=text_to_children(rest)))
            node = ParentNode(tag="ol", children=items)
        
        else:
            text = block.replace("\n", " ")
            children = text_to_children(text)
            node = ParentNode(tag="p", children=children)
            
        block_nodes.append(node)
        
    return ParentNode(tag="div", children=block_nodes)
