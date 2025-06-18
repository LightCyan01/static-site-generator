from utils import generate_pages_recursive
from file_utils import copy_static_to_public

def main():
    copy_static_to_public("static", "public")
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="public")
    
if __name__ == "__main__":
    main()