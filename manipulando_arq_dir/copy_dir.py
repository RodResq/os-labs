import shutil, os

os.chdir('/home/rresq/tmp')
retorno = shutil.copytree('/home/rresq/tmp/origin', '/home/rresq/tmp/origin_backup')
print(retorno)
