import zipfile, os

os.chdir('/home/rresq/tmp')
example_file = zipfile.ZipFile('example.zip')
list_files = example_file.namelist()
print(f"Lista files {list_files}")
spam_info = example_file.getinfo('spam.txt')
print(f"Tamanho do zip arquivo {spam_info.file_size}")
compress_file = spam_info.compress_size
print(f"Tamnho arquivo comprimido {compress_file}")
example_file.close()
