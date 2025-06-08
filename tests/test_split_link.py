import unittest
import test_config

from textnode import TextNode, TextType
from utils import split_nodes_link  

class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "Visit [Boot.dev](https://boot.dev) and [YouTube](https://youtube.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])

        expected = [
            TextNode("Visit ", TextType.TEXT),
            TextNode("Boot.dev", TextType.LINK, url="https://boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("YouTube", TextType.LINK, url="https://youtube.com"),
        ]
        self.assertListEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()
