from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE_BLOCK = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
    
def block_to_block_type(text: str):
    lines = text.splitlines()
        
    # headings
    if re.match("^#{1,6}\s", lines[0]):
        return BlockType.HEADING
        
    #code block
    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE_BLOCK
        
    #quote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
        
    #unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
        
    #ordered list
    if all(re.match("^\d+\.\s", line) for line in lines):
        return BlockType.ORDERED_LIST
        
    return BlockType.PARAGRAPH