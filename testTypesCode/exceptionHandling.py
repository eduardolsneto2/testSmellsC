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
       responseArray.append(response)
    #    if response:
    #         print(text + ' atende ao exception handling')
    #    else:
    #         print(text + ' não atende ao exception handling')
    return responseArray

def assertRuleForBlock(block):
    hasExceptionStatement = False
    if block is not None:
        lines = block.find_all('expr_stmt')
        allStatements = ['longjmp', 'setjmp', 'perror', 'strerror', 'stderr', 'error_at']
        for line in lines:
            names = line.find_all('name')
            for name in names:
                if name.text in allStatements:
                    hasExceptionStatement = True
    return not hasExceptionStatement
