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
    #         print(text + ' atende ao mystery guest')
    #    else:
    #         print(text + ' não atende ao mystery guest')
    return responseArray

def assertRuleForBlock(block):
    hasFileStatement = False
    if block is not None:
        lines = block.find_all('expr_stmt')
        allStatements = ['fopen', 'fclose', 'fgets']
        for line in lines:
            names = line.find_all('name')
            for name in names:
                if name.text in allStatements:
                    hasFileStatement = True
    return not hasFileStatement