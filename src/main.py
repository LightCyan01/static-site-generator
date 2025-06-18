import sys
from utils import generate_pages_recursive
from file_utils import copy_static_to_public

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static_to_public("static", "public")
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="docs", basepath=basepath)
    
if __name__ == "__main__":
    main()