import os

for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unlink(filename) # apaga o arquivo de forma permante
        print(filename)
