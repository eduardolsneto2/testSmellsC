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
            print(text + ' atende ao sleep Test')
       else:
            print(text + ' não atende ao sleep Test')

def assertRuleForBlock(block):
    hasSleepStatement = False
    lines = block.find_all('expr_stmt')
    allStatements = ['sleep']
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if name.text in allStatements:
                hasSleepStatement = True
    return not hasSleepStatement
