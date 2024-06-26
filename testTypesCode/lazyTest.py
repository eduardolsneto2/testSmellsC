import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    print('---------')
    print('for File:' + fileName)
    allExpressions = []
    for index, block in enumerate(blocks):
       response = assertRuleForBlock(block)
       allExpressions = allExpressions + response
    print(allExpressions)
    if len(allExpressions) == len(set(allExpressions)):
        print('atende ao lazy Test')
    else:
        print('não atende ao lazy Test')

def assertRuleForBlock(block):
    allExpressions = []
    lines = block.find_all('expr_stmt')
    for line in lines:
        expressions = line.find_all('call')
        for expression in expressions:
            name = expression.find('name')
            if 'assert' not in name.text:
                allExpressions.append(name)
    return allExpressions