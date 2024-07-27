import os

def print_tree(startpath, indent=''):
    """
    Print the directory tree starting from startpath, showing all code inside the files.
    """
    if not os.path.isdir(startpath):
        print(f"{startpath} is not a valid directory.")
        return

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")

        # Exclude hidden directories (e.g., .git)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if f.startswith('.'):  # Exclude hidden files
                continue
            file_path = os.path.join(root, f)
            print(f"{sub_indent}{f}")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    code_lines = file.readlines()
                    for line in code_lines:
                        print(f"{sub_indent}    {line.strip()}")
            except UnicodeDecodeError:
                print(f"{sub_indent}    Could not read file: Non-UTF-8 encoding")
            except Exception as e:
                print(f"{sub_indent}    Could not read file: {e}")

if __name__ == '__main__':
    project_path = input("Enter the path to the project directory: ")
    print_tree(project_path)
