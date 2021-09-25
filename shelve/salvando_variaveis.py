import shelve

# shel_file = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shel_file['cats'] = cats
# shel_file.close()

shelf_file = shelve.open('mydata')
print(type(shelf_file))
print(shelf_file['cats'])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()
