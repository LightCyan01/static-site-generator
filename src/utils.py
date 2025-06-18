import os
from textnode import TextNode, TextType
from leafnode import LeafNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html = [text_node_to_html_node(text_nodes) for text_nodes in nodes]
    return html

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return [n for n in nodes if n.text]

def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _: 
            raise ValueError(f"Error: {text_node.text_type}")

def generate_page(from_path, template_path, dest_path, basepath="/"):
    from parser import markdown_to_html_node
    from extractors import extract_title

    #1. log
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    #2. read markdown
    with open(from_path, "r") as f:
        md = f.read()
        
    #3. read template
    with open(template_path, "r") as f:
        template = f.read()
        
    #4. convert markdown to HTML string
    root = markdown_to_html_node(md)
    content_html = root.to_html()
    
    #5. extract h1 as title
    title = extract_title(md)
    
    #6. add title & content to template
    page = (template.replace("{{ Title }}", title).replace("{{ Content }}", content_html).replace('href="/', f'href="{basepath}').replace('src="/',  f'src="{basepath}'))
    
    #7. write results
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    #crawl every entry
    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            
            #path to src markdown
            src_md = os.path.join(root, filename)
            
            #relative path
            rel_dir = os.path.relpath(root, dir_path_content)
            
            #output dir
            out_dir = os.path.join(dest_dir_path, rel_dir)
            os.makedirs(out_dir, exist_ok=True)
            
            base, _ = os.path.splitext(filename)
            dst_html = os.path.join(out_dir, base + ".html")
            
            generate_page(src_md, template_path, dst_html, basepath)
    