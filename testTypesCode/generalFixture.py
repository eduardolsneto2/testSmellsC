import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    print('---------')
    print('for File:' + fileName)
    setupBlock = xmlReader.getSetupBlock(fileName)
    responseArray = []
    if setupBlock is False:
        print('não atende ao general Fixture')
        responseArray.append(False)
    else: 
        variablesFromSetup = getAllVariableFromSetup(setupBlock)
        allBlocksAreOK = True
        for index, block in enumerate(blocks):
            response = assertRuleForBlock(block, variablesFromSetup)
            if response == False:
                allBlocksAreOK = False
        if allBlocksAreOK:
                print('atende ao general Fixture')
                responseArray.append(True)
        else:
                print('não atende ao general Fixture')
                responseArray.append(False)
    return responseArray

def getAllVariableFromSetup(setupBlock):
    expressions = setupBlock.find_all('expr_stmt')
    allVariables = []
    for expression in expressions:
        name = expression.find('name')
        allVariables.append(name.text)
    return allVariables

def assertRuleForBlock(block, variablesFromSetup):
    lines = block.find_all(['expr_stmt','decl_stmt'])
    allResponses = []
    for variable in variablesFromSetup:
        hasVariable = False
        for line in lines:
            names = line.find_all('name')
            for name in names:
                if variable == name.text:
                    hasVariable = True
        allResponses.append(hasVariable)
    return (len(set(allResponses)) == 1) and (allResponses[0] == True)