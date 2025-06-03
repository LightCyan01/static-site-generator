from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    print(HTMLNode(tag="div", value="Hello", children=[], props={"id": "main"}))

if __name__ == "__main__":
    main()