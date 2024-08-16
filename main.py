from testTypesCode import assertionRoulette, conditionalTestLogic, duplicateAssert, emptyTest, magicNumber, redundantPrint, redundantAssertion, unknownTest
from testTypesCode import sensitiveEquality, sleepyTest, exceptionHandling, eagerTest, lazyTest, mysteryGuest, generalFixture, constructorInitialization
from testTypesCode import resourceOptimism
import glob, os

def runAssertionForAllFiles(allFiles, repo):
    assertionRouletteResponses = []
    conditionalTestLogicResponses = []
    duplicateAssertResponses = []
    emptyTestResponses = []
    magicNumberResponses = []
    redundantPrintResponses = []
    redundantAssertionResponses = []
    unknownTestResponses = []
    sensitiveEqualityResponses = []
    sleepyTestResponses = []
    exceptionHandlingResponses = []
    eagerTestResponses = []
    lazyTestResponses = []
    mysteryGuestResponses = []
    generalFixtureResponses = []
    constructorInitializationResponses = []
    resourceOptimismResponses = []
    if len(allFiles) == 0:
        return
    for singleFile in allFiles:
        path = os.path.basename(os.path.normpath(singleFile))
        xmlPath = repo + "XMLCode/" + path + ".xml"
        os.system("srcml " + singleFile + " -o " + xmlPath)
        assertionRouletteResponses += assertionRoulette.assertRule("./" + xmlPath)
        conditionalTestLogicResponses += conditionalTestLogic.assertRule("./" + xmlPath)
        duplicateAssertResponses += duplicateAssert.assertRule("./" + xmlPath)
        emptyTestResponses += emptyTest.assertRule("./" + xmlPath)
        magicNumberResponses += magicNumber.assertRule("./" + xmlPath)
        redundantPrintResponses += redundantPrint.assertRule("./" + xmlPath)
        redundantAssertionResponses += redundantAssertion.assertRule("./" + xmlPath)
        unknownTestResponses += unknownTest.assertRule("./" + xmlPath)
        sensitiveEqualityResponses += sensitiveEquality.assertRule("./" + xmlPath)
        sleepyTestResponses += sleepyTest.assertRule("./" + xmlPath)
        exceptionHandlingResponses += exceptionHandling.assertRule("./" + xmlPath)
        eagerTestResponses += eagerTest.assertRule("./" + xmlPath)
        lazyTestResponses += lazyTest.assertRule("./" + xmlPath)
        mysteryGuestResponses += mysteryGuest.assertRule("./" + xmlPath)
        generalFixtureResponses += generalFixture.assertRule("./" + xmlPath)
        constructorInitializationResponses += constructorInitialization.assertRule("./" + xmlPath)
        resourceOptimismResponses += resourceOptimism.assertRule("./" + xmlPath)
    print("AssertionRoulette: " + str(assertionRouletteResponses.count(True)/len(assertionRouletteResponses)))
    print("conditionalTestLogicResponses: " + str(conditionalTestLogicResponses.count(True)/len(conditionalTestLogicResponses)))
    print("duplicateAssertResponses: " + str(duplicateAssertResponses.count(True)/len(duplicateAssertResponses)))
    print("emptyTestResponses: " + str(emptyTestResponses.count(True)/len(emptyTestResponses)))
    print("magicNumberResponses: " + str(magicNumberResponses.count(True)/len(magicNumberResponses)))
    print("redundantPrintResponses: " + str(redundantPrintResponses.count(True)/len(redundantPrintResponses)))
    print("redundantAssertionResponses: " + str(redundantAssertionResponses.count(True)/len(redundantAssertionResponses)))
    print("unknownTestResponses: " + str(unknownTestResponses.count(True)/len(unknownTestResponses)))
    print("sensitiveEqualityResponses: " + str(sensitiveEqualityResponses.count(True)/len(sensitiveEqualityResponses)))
    print("sleepyTestResponses: " + str(sleepyTestResponses.count(True)/len(sleepyTestResponses)))
    print("exceptionHandlingResponses: " + str(exceptionHandlingResponses.count(True)/len(exceptionHandlingResponses)))
    print("eagerTestResponses: " + str(eagerTestResponses.count(True)/len(eagerTestResponses)))
    print("lazyTestResponses: " + str(lazyTestResponses.count(True)/len(lazyTestResponses)))
    print("mysteryGuestResponses: " + str(mysteryGuestResponses.count(True)/len(mysteryGuestResponses)))
    print("generalFixtureResponses: " + str(generalFixtureResponses.count(True)/len(generalFixtureResponses)))
    print("constructorInitializationResponses: " + str(constructorInitializationResponses.count(True)/len(constructorInitializationResponses)))
    print("resourceOptimismResponses: " + str(resourceOptimismResponses.count(True)/len(resourceOptimismResponses)))
    print("-----------------------------------------")

allRepos = glob.glob("repos/*")
for repo in allRepos:
    print(repo)
    if "XMLCode" in repo:
        continue
    os.system("mkdir ./" + repo + "XMLCode")
    allFiles = glob.glob(repo + "/**/*test*/**/*.c", recursive=True)
    # print(allFiles)
    runAssertionForAllFiles(allFiles, repo)

