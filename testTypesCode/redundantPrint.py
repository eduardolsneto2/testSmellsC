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
            print(text + ' atende ao redundant print')
       else:
            print(text + ' não atende ao redundant print')
    return responseArray

def assertRuleForBlock(block):
    hasPrintStatement = False
    lines = block.find_all('expr_stmt')
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if 'print' in name.text:
                hasPrintStatement = True
    return not hasPrintStatement