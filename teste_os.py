import os
import datetime
import pathlib
import zipfile

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

# Verificando o path absoluto a partir de um path relativo com abspath()
path_absoluto = os.path.abspath('.')
print(f"O path absoluto e: {path_absoluto}")

path_absoluto2 = os.path.abspath('.idea/')
print(f"A path absoluto a partir de uma pasta e: {path_absoluto2}")

# Retorno boolean com isabs()
eabs = os.path.isabs('.')
print(f"O path dado  e um path absoluto: {eabs}")
eabs2 = os.path.isabs(os.path.abspath('.'))
print(f"O path dado  e um path absoluto: {eabs2}")

# basename() e dirname()
base_name = os.path.basename('/home/rresq/github/os-labs/teste_os.py')
print(f"O metodo basename() retorna tudo que estiver depois da ultima barra, no caso o nome do arquivo: {base_name}")

dir_name = os.path.dirname('/home/rresq/github/os-labs/teste_os.py')
print(f"o metodo dirname() retorna tudo que estiver antes da ultima barra: {dir_name}")

# Caso dirname e basename sejam necessarios
full_path = '/home/rresq/github/os-labs/teste_os.py'
ex_split = os.path.split(full_path) # retorna uma tupla
print(f"Caso dirname e basename sejam necessarios: {ex_split}")
print(f"O arquivo test_os.py esta na tupla? {base_name in ex_split}")

retorno = '/home/rresq/github/os-labs'.split(os.path.sep)
print(retorno)

# Obtendo o tamanho de um arquivo com getsize()
tamanho = os.path.getsize('/home/rresq/github/os-labs/teste_os.py')
print(f"O tamanho do arquivo tem: {tamanho} bytes")

# Obtendo a lista de arquivo dentro de um diretorio
list_files = os.listdir('/home/rresq/tmp')
print(f"O diretorios contidos em tmp sao: {list_files}")

# Obtendo o tamanho totoal de todos os arquivos presente em um diretorio
total_size = 0
for filename in os.listdir('/home/rresq/tmp'):
    arquivo = os.path.join('/home/rresq/tmp', filename)
    if os.path.isfile(arquivo):
        if not zipfile.is_zipfile(arquivo):
            tamanho_arquivo = os.path.getsize(arquivo)
            data_criacao_arquivo = os.path.getctime(os.path.join('/home/rresq/tmp', filename))
            data_formatada = datetime.datetime.fromtimestamp(data_criacao_arquivo)
            print(f"O tamanho tottao do arquivo {filename} e: {tamanho_arquivo} Bytes,  e sua Data de criacao e: {data_formatada}")
            total_size = total_size + tamanho_arquivo
print(f"O tamanho total de todos os arquivos e: {total_size}")
