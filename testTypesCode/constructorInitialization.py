import sys
sys.path.append("..")
import xmlReader

def assertRule(fileName):
    blocks = xmlReader.getCodeFromXmlFile(fileName)
    print('---------')
    print('for File:' + fileName)
    setupBlock = xmlReader.getSetupBlock(fileName)
    globalVals = xmlReader.getGlobalVariables(fileName)
    if globalVals is False:
        print('atende ao Constructor Initialization')
    elif setupBlock is False:
        print('nao atende ao Constructor Initialization')
    else: 
        variablesFromSetup = getAllVariableFromSetup(setupBlock)
        if set(variablesFromSetup) == set(globalVals):
            print('atende ao Constructor Initialization')
        else:
            print('nao atende ao Constructor Initialization')

def getAllVariableFromSetup(setupBlock):
    expressions = setupBlock.find_all('expr_stmt')
    allVariables = []
    for expression in expressions:
        name = expression.find('name')
        allVariables.append(name.text)
    return allVariables