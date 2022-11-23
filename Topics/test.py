from typing import ClassVar


print("TEst File Only")
a = 1
b = 2
c = 1 + 2
print(c)
if c == 3:
    print("equal")


obj = {"name":"erewrew", "value":"ewrew"}
print(obj)
object1 = { "str": str(obj) }
print(object1)
print(type(object1))

def testFucntion(is_header, iv_contact):
    print(iv_contact)
    print(is_header)

oArgs = {"iv_contact":"Test one", "is_header": {"anem": "dsfsd", "dsf":"fdsf"}}
aArgs = ["Test one", {"anem": "dsfsd", "dsf":"fdsf"}]
testFucntion(**oArgs)
testFucntion(*aArgs)

class MyClass():
    def testDynamicMethod(self, iv_contact, is_header):
        print(iv_contact)
        print(is_header)

    @classmethod
    def testStaticDynamicMethod(cls, iv_contact, is_header):
        print(iv_contact)
        print(is_header)    


getattr(MyClass(), 'testDynamicMethod')(*[], **oArgs)