import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    # print('---------')
    # print('for File:' + fileName)
    setupBlock = xmlReader.getSetupBlock(fileName)
    globalVals = xmlReader.getGlobalVariables(fileName)
    responseArray = []
    if globalVals is False:
        # print('atende ao Constructor Initialization')
        responseArray.append(False)
    elif setupBlock is False:
        # print('nao atende ao Constructor Initialization')
        responseArray.append(True)
    else: 
        variablesFromSetup = getAllVariableFromSetup(setupBlock)
        if set(variablesFromSetup) == set(globalVals):
            # print('atende ao Constructor Initialization')
            responseArray.append(False)
        else:
            # print('nao atende ao Constructor Initialization')
            responseArray.append(True)
    return responseArray

def getAllVariableFromSetup(setupBlock):
    allVariables = []
    if setupBlock is not None:
        expressions = setupBlock.find_all('expr_stmt')
        for expression in expressions:
            name = expression.find('name')
            allVariables.append(name.text)
    return allVariables