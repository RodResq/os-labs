import os

path = os.path.join('usr', 'bin', 'span')
print(path)

# uniao de nomes de arquivos em pastas
my_files = ['account.txt', 'details.csv', 'invite.docx']
for file_name in my_files:
    print(os.path.join('/home/rresq/tmp', file_name))
