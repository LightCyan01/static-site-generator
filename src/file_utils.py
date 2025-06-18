import os
import shutil

def clear_directory(path: str):
    if os.path.exists(path):
        for name in os.listdir(path):
            full = os.path.join(path, name)
            print(f"Full Path: {full}")
            if os.path.isdir(full):
                print(f"Removing Directory: {full}")
                shutil.rmtree(full)
            else:
                print(f"Removing: {full}")
                os.remove(full)
    else:
        print(f"Creating Directory: {path}")
        os.makedirs(path)

def copy_recursive(src: str, dst: str):
    for name in os.listdir(src):
        source = os.path.join(src, name)
        print(f"Source Path: {source}")
        dest = os.path.join(dst, name)
        print(f"Distribution/Public Path: {dest}")
        
        if os.path.isdir(source):
            os.makedirs(dest, exist_ok=True)
            copy_recursive(source, dest)
        else:
            shutil.copy2(source, dest)
            print(f"copied {source} -> {dest}")

def copy_static_to_public(static_dir="static", public_dir="public"):
    clear_directory(public_dir)
    copy_recursive(static_dir, public_dir)