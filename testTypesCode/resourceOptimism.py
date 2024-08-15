from bs4 import NavigableString, Tag
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
            print(text + ' atende ao resource Optimism')
       else:
            print(text + ' não atende ao resource Optimism')
    return responseArray

def assertRuleForBlock(block):
    allFilePossibilities = ['fclose', 'fopen', 'fread', 'fwrite']
    hasAccess = False
    hasFileHandle = False
    for line in block.contents:
        if isinstance(line, NavigableString):
            continue
        expressions = line.find_all('call')
        for expression in expressions:
            name = expression.find('name')
            print('name:' + name.text)
            if 'access' in name.text:
                hasAccess = True
            if name.text in allFilePossibilities:
                hasFileHandle = True
    return isResourceOptimism(hasAccess, hasFileHandle)

def isResourceOptimism(hasAccess, hasFileHandle):
    print(hasAccess)
    print(hasFileHandle)
    if hasFileHandle and hasAccess:
        return True
    elif not hasFileHandle:
        return True
    return False
