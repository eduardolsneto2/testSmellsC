from bs4 import BeautifulSoup

def getBlocksFromXmlData(fileName):
    with open("./testCodeExamples/" +fileName, 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')
    functions = soup.find_all('function')
    blocks = []
    for function in functions:
        block = function.find('block_content')
        blocks.append(block)
    return blocks


def getCodeFromXmlFile(fileName):
    blocks = getBlocksFromXmlData(fileName)
    return blocks

def getSetupBlock(fileName):
    with open("./testCodeExamples/" +fileName, 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')
    # this needs to change since there could be blocks inside functions
    functions = soup.find_all('function')
    for function in functions:
        name = function.find('name', recursive=False)
        if 'setup' in name.text:
            return function.find('block_content')
    return False