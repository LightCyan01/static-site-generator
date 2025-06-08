import unittest
import test_config

from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_no_delimiter(self):
        node = TextNode("hello world", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        # only one node, unchanged text/type
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, "hello world")
        self.assertEqual(out[0].text_type, TextType.TEXT)

    def test_single_pair(self):
        node = TextNode("before `c` after", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        # should get [TEXT, CODE, TEXT]
        texts = [n.text for n in out]
        types = [n.text_type for n in out]
        self.assertEqual(texts, ["before ", "c", " after"])
        self.assertEqual(types, [TextType.TEXT, TextType.CODE, TextType.TEXT])

    def test_multiple_pairs(self):
        node = TextNode("`x` & `y`", TextType.TEXT)
        out = split_nodes_delimiter([node], "`", TextType.CODE)
        texts = [n.text for n in out]
        types = [n.text_type for n in out]
        self.assertEqual(texts, ["x", " & ", "y"])
        self.assertEqual(types, [TextType.CODE, TextType.TEXT, TextType.CODE])

    def test_non_text_nodes_pass_through(self):
        bold = TextNode("bold", TextType.BOLD)
        normal = TextNode("just text", TextType.TEXT)
        out = split_nodes_delimiter([bold, normal], "`", TextType.CODE)
        # bold node untouched, then normal split into one
        self.assertIs(out[0], bold)
        self.assertEqual(out[1].text, "just text")
        self.assertEqual(out[1].text_type, TextType.TEXT)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("oops `no close", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)
            
if __name__ == "__main__":
    unittest.main()