import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    print('---------')
    print('for File:' + fileName)
    for index, block in enumerate(blocks):
       response = assertRuleForBlock(block)
       text = 'bloco ' + str(index)
       if response:
            print(text + ' atende ao eager Test')
       else:
            print(text + ' não atende ao eager Test')

def assertRuleForBlock(block):
    numberOfAsserts = 0
    lines = block.find_all('expr_stmt')
    for line in lines:
        expressions = line.find_all('call')
        for expression in expressions:
            name = expression.find('name')
            if 'assert' not in name.text:
                numberOfAsserts += 1
    return numberOfAsserts <= 1