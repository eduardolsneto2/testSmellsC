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
            print(text + ' atende ao duplicate assert')
       else:
            print(text + ' não atende ao cduplicate assert')

def assertRuleForBlock(block):
    allFirstArguments = []
    lines = block.find_all('expr_stmt')
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if 'assert' in name.text:
                firstArgument = line.find('argument')
                value = firstArgument.find('name')
                allFirstArguments.append(value)
    return len(allFirstArguments) == len(set(allFirstArguments))
