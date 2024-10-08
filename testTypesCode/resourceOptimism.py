from bs4 import NavigableString, Tag
import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    # print('---------')
    # print('for File:' + fileName)
    responseArray = []
    for index, block in enumerate(blocks):
       response = assertRuleForBlock(block)
       text = 'bloco ' + str(index)
       responseArray.append(not response)
    #    if response:
    #         print(text + ' atende ao resource Optimism')
    #    else:
    #         print(text + ' não atende ao resource Optimism')
    return responseArray

def assertRuleForBlock(block):
    allFilePossibilities = ['fclose', 'fopen', 'fread', 'fwrite']
    hasAccess = False
    hasFileHandle = False
    if block is not None:
        for line in block.contents:
            if isinstance(line, NavigableString):
                continue
            expressions = line.find_all('call')
            for expression in expressions:
                name = expression.find('name')
                if name is not None and 'access' in name.text:
                    hasAccess = True
                if name.text in allFilePossibilities:
                    hasFileHandle = True
    return isResourceOptimism(hasAccess, hasFileHandle)

def isResourceOptimism(hasAccess, hasFileHandle):
    if hasFileHandle and hasAccess:
        return True
    elif not hasFileHandle:
        return True
    return False
