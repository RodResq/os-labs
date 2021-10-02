import traceback

try:
    raise Exception('This is the error message')
except:
    with open('erro_info.txt', 'w') as file_object:
        file_object.write(traceback.format_exc())
    print('The traceback info was written to error_info.txt')
