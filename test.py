import os
import shutil
from lxml import etree
import xml.etree.ElementTree as ET



def createxml():
    
    if os.path.exists('file.xml') and os.path.getsize('file.xml') > 0:
        pass
    else:
        root = etree.Element('config') 
        element = etree.SubElement(root, 'file')
        etree.SubElement(element, 'file1', source_path="")
        etree.SubElement(element, 'file1', destination_path="")
        etree.SubElement(element, 'file1', file_name="")   
        tree = root.getroottree()
        tree.write('file.xml')
        exit("file.xml Creating!\nOpen file.xml and fill in the data to copybetween the quotes.")
        
def parseXML():
    global dict
    tree = ET.parse("file.xml")
    root = tree.getroot()
    dict = []
    for element in root:
        for i in element:
            for k, v in i.items():
                dict.append(k)
                dict.append(v)


def find_path():
    global input_file_path
    input_file_path = dict[1] + '/'   
    try:
        os.scandir(path=input_file_path)
        return "Path found!"
    except (NotADirectoryError, FileNotFoundError):
        return "Path not found!"

def find_file_path():
    global destination_path
    destination_path = dict[3] + '/'
    try:
        os.scandir(path=destination_path)
        return "Path found!"
    except (FileNotFoundError, NotADirectoryError):
        return "Path not found!"

def find_file():
    global file_name_find
    file_name_find = dict[5]
    finaly_file = os.path.isfile(input_file_path + file_name_find)
    if finaly_file == True:
        return 'File copied!'
    else:
        return 'File not found!'

def coping():
    try: 
        coping_file = shutil.copy(input_file_path + file_name_find, destination_path)
        return coping_file, "file copied!"   
    except (FileNotFoundError, NotADirectoryError):
        return "Error coping!"



if __name__ == "__main__":
    createxml()
    parseXML()
    print(find_path())
    print(find_file_path())
    print(find_file())
    print(coping())


