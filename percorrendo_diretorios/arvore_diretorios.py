import os

# Percorre a arvore de diretorios
for folder_name, sub_folders, file_names in os.walk('/home/rresq/tmp/delicius'):
    print(f"The current folder is {folder_name}")

    for sub_folder in sub_folders:
        print(f"SUBFOLDER OF {folder_name} : {sub_folder}")

    for file_name in file_names:
        print(f'FILE INSIDE {folder_name}: {file_name}')
