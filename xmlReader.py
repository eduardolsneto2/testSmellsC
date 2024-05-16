from bs4 import BeautifulSoup

def getBlocksFromXmlData(fileName):
    with open("./testCodeExamples/" +fileName, 'r') as f:
        file = f.read() 
    soup = BeautifulSoup(file, 'xml')
    # this needs to change since there could be blocks inside functions
    blocks = soup.find_all('block_content')
    return blocks


def getCodeFromXmlFile(fileName):
    blocks = getBlocksFromXmlData(fileName)
    return blocks