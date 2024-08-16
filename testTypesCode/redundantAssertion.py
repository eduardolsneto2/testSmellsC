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
    #         print(text + ' atende ao redundant assertion')
    #    else:
    #         print(text + ' não atende ao redundant assertion')
    return responseArray

def assertRuleForBlock(block):
    isAllEqual = False
    if block is not None:
        lines = block.find_all('expr_stmt')
        for line in lines:
            names = line.find_all('name')
            for name in names:
                if 'assert' in name.text:
                    arguments = line.find_all('argument')
                    allValues = []
                    for argument in arguments:
                        value = argument.find(['literal', 'name'])
                        allValues.append(value)
                    if not isAllEqual and len(allValues) > 1:
                        isAllEqual = all_equal(allValues)
    return not isAllEqual

def all_equal(iterator):
    return len(set(iterator)) <= 1