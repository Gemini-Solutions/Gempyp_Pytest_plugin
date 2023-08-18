import pytest
from  file_handling_utility import *
import logging 

@pytest.fixture
def test_filepath():
    return ('src\\pytest_demo\\file.txt')

def test_write_content_to_file(test_filepath):
    content = """This is gempyp demo.
    Here we are demonstrating pytest integration in gempyp.
    This functions demonstrates to test writing into the file utility.\n"""
    writeInFile(test_filepath, content)
    with open(test_filepath, 'r') as fh:
        assert(fh.read() == content)
    
    
def test_append_content(test_filepath):
    content = "This functions demonstrates to test append utility.\n"
    appendInFile(test_filepath, content)
    with open(test_filepath, 'r') as fh:
        line = fh.readlines()
    print(line)
    assert(line[-1] == content)
    
def test_seek(test_filepath):
    cursor = fileCursorToBeginning(test_filepath)
    first_line = cursor.readline()
    with open(test_filepath, 'r') as fh:
        line = fh.readline()
    assert(line == first_line)
    
def test_read(test_filepath):
    file_content = readFile(test_filepath)
    with open(test_filepath, 'r') as fh:
        text = fh.read()
    assert(text == file_content)