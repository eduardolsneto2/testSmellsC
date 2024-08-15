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
            print(text + ' atende ao eager Test')
       else:
            print(text + ' não atende ao eager Test')
        return responseArray

def assertRuleForBlock(block):
    numberOfExpressions = 0
    lines = block.find_all('expr_stmt')
    for line in lines:
        expressions = line.find_all('call')
        for expression in expressions:
            name = expression.find('name')
            if 'assert' not in name.text:
                numberOfExpressions += 1
    return numberOfExpressions <= 1