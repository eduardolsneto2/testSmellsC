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
            print(text + ' atende ao magic Number')
       else:
            print(text + ' não atende ao magic number')

def assertRuleForBlock(block):
    allConstantArguments = []
    lines = block.find_all('expr_stmt')
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if 'assert' in name.text:
                arguments = line.find_all('argument')
                for argument in arguments:
                    literals = argument.find_all('literal')
                    if len(literals) > 0:
                        allConstantArguments.append(literals)
    return len(allConstantArguments) == 0