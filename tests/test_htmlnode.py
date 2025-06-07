import unittest
import test_config

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    
    def test_no_props(self):
        node = HTMLNode(tag="p", value="Hello", children=None, props=None)
        assert node.props_to_html() == ""
    
    def test_single_prop(self):
        node = HTMLNode(tag="a", value="Link", children=None, props={"href": "http://example.com"})
        assert node.props_to_html() == ' href="http://example.com"'
        
    def test_multiple_props(self):
        attrs = {"href": "http://example.com", "target": "_blank"}
        node = HTMLNode(tag="a", value="Link", children=None, props=attrs)
        expected = ' href="http://example.com" target="_blank"'
        assert node.props_to_html() == expected
        
    def test_repr_all_fields(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"id": "main"})
        rep = repr(node)
        assert "HTMLNode(div" in rep
        assert "Hello" in rep
        assert "[]" in rep
        assert "{'id': 'main'}" in rep

if __name__ == "__main__":
    unittest.main()