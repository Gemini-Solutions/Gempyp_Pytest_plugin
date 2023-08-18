def readFile(filename):
    with open(filename, 'r') as file_handler:
        return file_handler.read()
    
def writeInFile(filename, content):
    with open(filename, 'w') as file_handler:
        file_handler.write(content)
        
def appendInFile(filename, content):
    with open(filename, 'a+') as file_handler:
        file_handler.write(content)
        
def fileCursorToBeginning(filename):
    file_handler = open(filename, 'r') 
    file_handler.seek(0)
    return file_handler