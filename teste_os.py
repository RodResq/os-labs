import os

path = os.path.join('usr', 'bin', 'span')
print(path)

# uniao de nomes de arquivos em pastas
my_files = ['account.txt', 'details.csv', 'invite.docx']
for file_name in my_files:
    print(os.path.join('/home/rresq/tmp', file_name))

# Obtendo o diretorio de trabalho atual
current_directory = os.getcwd()
print(f"Diretorio de trabalho atual: {current_directory}")

# Criando diretorios
# os.makedirs('/home/rresq/github/os-labs/teste_1/teste_2/teste_3')
# os.mkdir(f"{current_directory}/new_diretory")
