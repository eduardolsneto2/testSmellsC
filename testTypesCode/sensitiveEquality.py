import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    print('---------')
    print('for File:' + fileName)
    responseArray = []
    for index, block in enumerate(blocks):
       response = assertRuleForBlock(block)
       text = 'bloco ' + str(index)
       responseArray.append(response)
       if response:
            print(text + ' atende ao sensitive equality')
       else:
            print(text + ' não atende ao sensitive equality')
    return responseArray

def assertRuleForBlock(block):
    hasStringStatement = False
    lines = block.find_all('expr_stmt')
    allStringStatements = ['atof','atoi','atol', 'strtod', 'strtol', 'strtoul', 'sprintf', 'itoa']
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if name.text in allStringStatements:
                hasStringStatement = True
    return not hasStringStatement
