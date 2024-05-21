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
            print(text + ' atende ao redundant print')
       else:
            print(text + ' não atende ao redundant print')

def assertRuleForBlock(block):
    hasPrintStatement = False
    lines = block.find_all('expr_stmt')
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if 'print' in name.text:
                hasPrintStatement = True
    return not hasPrintStatement