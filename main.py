from testTypesCode import assertionRoulette, conditionalTestLogic, duplicateAssert, emptyTest, magicNumber, redundantPrint, redundantAssertion, unknownTest
from testTypesCode import sensitiveEquality, sleepyTest, exceptionHandling, eagerTest, lazyTest, mysteryGuest, generalFixture, constructorInitialization
from testTypesCode import resourceOptimism
import glob, os

# assertionRoulette.assertRule("cachedir.c.xml")
# conditionalTestLogic.assertRule('decode_ecdsa_signature.c.xml')
# duplicateAssert.assertRule("cachedir.c.xml")
# emptyTest.assertRule("cachedir_empty.c.xml")
# magicNumber.assertRule("strip_pkcs1_2_padding.c.xml")
# redundantPrint.assertRule("strip_pkcs1_2_padding_print.c.xml")
# redundantAssertion.assertRule("cachedir.c.xml")
# unknownTest.assertRule("cachedir.c.xml")
# sensitiveEquality.assertRule("cachedir.c.xml")
# sleepyTest.assertRule("cachedir.c.xml")
# exceptionHandling.assertRule("cachedir.c.xml")
# eagerTest.assertRule("cachedir.c.xml")
# lazyTest.assertRule("cachedir_empty.c.xml")
# mysteryGuest.assertRule("cachedir.c.xml")
# generalFixture.assertRule("generalFixture.c.xml")
# constructorInitialization.assertRule('constructorInitialization.c.xml')
# resourceOptimism.assertRule('resourceOptimism.c.xml')
allRepos = glob.glob("repos/*")
for repo in allRepos:
    print(repo)
    if "XMLCode" in repo:
        continue
    os.system("mkdir ./" + repo + "XMLCode")
    allfiles = glob.glob(repo + "/**/tests/**/*.c", recursive=True)
    # print(allfiles)
    for singleFile in allfiles:
        path = os.path.basename(os.path.normpath(singleFile))
        os.system("srcml " + singleFile + " -o " + repo + "XMLCode/" + path + ".xml")