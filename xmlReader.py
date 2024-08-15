from bs4 import BeautifulSoup, NavigableString

def getBlocksFromXmlData(fileName):
    with open(fileName, 'r') as f:
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
    with open(fileName, 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')
    functions = soup.find_all('function')
    for function in functions:
        name = function.find('name', recursive=False)
        if 'setup' in name.text:
            return function.find('block_content')
    return False

def getGlobalVariables(fileName):
    with open(fileName, 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')
    variables = soup.find('unit').find_all('decl_stmt', recursive=False)
    allVariables = []
    for line in variables:
        name = line.find('decl').find('name', recursive=False)
        allVariables.append(name.text)
    if len(allVariables) == 0:
        return False
    else:
        return allVariables