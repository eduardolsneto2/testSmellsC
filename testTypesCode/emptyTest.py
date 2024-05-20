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
            print(text + ' atende ao empty test')
       else:
            print(text + ' não atende ao empty test')

def assertRuleForBlock(block):
    lines = []
    for line in block:
        if line.name != 'comment' and line.name != None:
            lines.append(line)
    return len(lines) > 0
