from testTypesCode import assertionRoulette, conditionalTestLogic, duplicateAssert, emptyTest

assertionRoulette.assertRule("cachedir.c.xml")
conditionalTestLogic.assertRule('decode_ecdsa_signature.c.xml')
duplicateAssert.assertRule("cachedir.c.xml")
emptyTest.assertRule("cachedir_empty.c.xml")