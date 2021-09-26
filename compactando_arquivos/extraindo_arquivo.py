import zipfile, os

os.chdir('/home/rresq/tmp')
example_file = zipfile.ZipFile('example.zip')
example_file.extractall()
example_file.close()
