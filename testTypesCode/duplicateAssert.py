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
    #         print(text + ' atende ao duplicate assert')
    #    else:
    #         print(text + ' não atende ao cduplicate assert')
    return responseArray

def assertRuleForBlock(block):
    allFirstArguments = []
    if block is not None:
        lines = block.find_all('expr_stmt')
        for line in lines:
            names = line.find_all('name')
            for name in names:
                if 'assert' in name.text:
                    firstArgument = line.find('argument')
                    if firstArgument is not None:
                        value = firstArgument.find('name')
                        allFirstArguments.append(value)
    return len(allFirstArguments) == len(set(allFirstArguments))
