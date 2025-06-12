import unittest
import test_config

from blocks import block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    
    def test_heading(self):
        block = "## test"
        assert block_to_block_type(block) == BlockType.HEADING
    
    def test_codeblocks(self):
        code = "```code block```"
        assert block_to_block_type(code) == BlockType.CODE_BLOCK

    def test_quote(self):
        quote = "> line1\n> line2"
        assert block_to_block_type(quote) == BlockType.QUOTE

    def test_unordered_list(self):
        unordered = "- one\n- two"
        assert block_to_block_type(unordered) == BlockType.UNORDERED_LIST

    def test_ordered_list(self):
        ordered = "1. first\n2. second"
        assert block_to_block_type(ordered) == BlockType.ORDERED_LIST

    def test_paragraph(self):
        para = "Just some text without special markers."
        assert block_to_block_type(para) == BlockType.PARAGRAPH 

if __name__ == "__main__":
    unittest.main()