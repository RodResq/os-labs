import shutil, os

os.chdir('/home/rresq/tmp/origin')
retorno = shutil.copy('/home/rresq/tmp/origin/spam.txt', '/home/rresq/tmp/destino')
print(retorno)
