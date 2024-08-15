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
    for singleFile in allFiles:
        path = os.path.basename(os.path.normpath(singleFile))
        xmlPath = repo + "XMLCode/" + path + ".xml"
        os.system("srcml " + singleFile + " -o " + xmlPath)
        assertionRouletteResponses.append(assertionRoulette.assertRule("./" + xmlPath))
        assertionRouletteResponses.append(conditionalTestLogic.assertRule("./" + xmlPath))
        duplicateAssertResponses.append(duplicateAssert.assertRule("./" + xmlPath))
        emptyTestResponses.append(emptyTest.assertRule("./" + xmlPath))
        magicNumberResponses.append(magicNumber.assertRule("./" + xmlPath))
        redundantPrintResponses.append(redundantPrint.assertRule("./" + xmlPath))
        redundantAssertionResponses.append(redundantAssertion.assertRule("./" + xmlPath))
        unknownTestResponses.append(unknownTest.assertRule("./" + xmlPath))
        sensitiveEqualityResponses.append(sensitiveEquality.assertRule("./" + xmlPath))
        sleepyTestResponses.append(sleepyTest.assertRule("./" + xmlPath))
        exceptionHandlingResponses.append(exceptionHandling.assertRule("./" + xmlPath))
        eagerTestResponses.append(eagerTest.assertRule("./" + xmlPath))
        lazyTestResponses.append(lazyTest.assertRule("./" + xmlPath))
        mysteryGuestResponses.append(mysteryGuest.assertRule("./" + xmlPath))
        generalFixtureResponses.append(generalFixture.assertRule("./" + xmlPath))
        constructorInitializationResponses.append(constructorInitialization.assertRule("./" + xmlPath))
        resourceOptimismResponses.append(resourceOptimism.assertRule("./" + xmlPath))

allRepos = glob.glob("repos/*")
for repo in allRepos:
    print(repo)
    if "XMLCode" in repo:
        continue
    os.system("mkdir ./" + repo + "XMLCode")
    allFiles = glob.glob(repo + "/**/tests/**/*.c", recursive=True)
    runAssertionForAllFiles(allFiles, repo)

