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
            print(text + ' atende ao redundant assertion')
       else:
            print(text + ' não atende ao redundant assertion')

def assertRuleForBlock(block):
    isAllEqual = False
    lines = block.find_all('expr_stmt')
    for line in lines:
        names = line.find_all('name')
        for name in names:
            if 'assert' in name.text:
                arguments = line.find_all('argument')
                allValues = []
                print('-------')
                for argument in arguments:
                    value = argument.find(['literal', 'name'])
                    print(value)
                    allValues.append(value)
                if not isAllEqual and len(allValues) > 1:
                    isAllEqual = all_equal(allValues)
                    print(all_equal(allValues))
    print(not isAllEqual)
    return not isAllEqual

def all_equal(iterator):
    return len(set(iterator)) <= 1