import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    # print('---------')
    # print('for File:' + fileName)
    responseArray = []
    for index, block in enumerate(blocks):
       response = assertRuleForBlock(block)
       text = 'bloco ' + str(index)
       responseArray.append(not response)
    #    if response:
    #         print(text + ' atende ao conditional test logic')
    #    else:
    #         print(text + ' não atende ao conditional test logic')
    return responseArray

def assertRuleForBlock(block):
    if block is not None:
        lines = block.find_all(['if', 'while', 'for', 'switch'])
        return len(lines) == 0
    return True
