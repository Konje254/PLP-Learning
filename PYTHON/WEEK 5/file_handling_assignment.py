def  write_in_file(Path): 
    with open (Path, 'w') as f:
        f.writelines(['Sarah', '\n8', '\nDon'])
        
def  read_in_file(Path): 
    with open (Path, 'r+') as f:
        file_contents = f.readlines()
        for line in file_contents:
            print(line)

def append_in_file(Path): 
    with open (Path, 'a') as f:
        f.writelines(['\nKing', '\n20', '\nJunior'])

try:
    write_in_file("C:/Users/WVK LMMS/Desktop/LEARNING/PYTHON/WEEK 5/my_file.txt")
    read_in_file("C:/Users/WVK LMMS/Desktop/LEARNING/PYTHON/WEEK 5/my_file.txt")
    append_in_file("C:/Users/WVK LMMS/Desktop/LEARNING/PYTHON/WEEK 5/my_file.txt")

except (FileNotFoundError, PermissionError) as error:
    print(error)
