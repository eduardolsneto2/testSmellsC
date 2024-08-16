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
       responseArray.append(response)
    #    if response:
    #         print(text + ' atende ao empty test')
    #    else:
    #         print(text + ' não atende ao empty test')
    return responseArray

def assertRuleForBlock(block):
    lines = []
    if block is not None:
        for line in block:
            if line.name != 'comment' and line.name != None:
                lines.append(line)
    return len(lines) > 0
