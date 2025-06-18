from utils import generate_page
from file_utils import copy_static_to_public

def main():
    copy_static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    
if __name__ == "__main__":
    main()