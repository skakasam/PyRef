"""Python Truthiness and Falsiness Practice Module"""


###############################################################################
# Truthy vs Falsy Values
# 1. The following values are interpreted as false
#    - False
#    - None
#    - 0
#    - 0.0
#    - '' (empty string)
#    - [] (empty list)
#    - () (empty tuple)
#    - {} (empty dictionary)
# 2. All other values are interpreted as true
# 3. User-defined objects can customize their truthiness
#    by implementing the __bool__() or __len__() methods.
#    If both are defined, __bool__() takes precedence.
#    If neither is defined, the object is considered truthy.
###############################################################################
class Name:
    pass  # Always true in boolean contexts


class OtherName:
    def __init__(self, email_id):
        self.email_id = email_id

    def __len__(self):  # Takes precedence in boolean contexts
        return len(self.email_id.strip())


class YetAnotherName:
    def __init__(self, name):
        self.name = name

    def __bool__(self):  # Takes precedence over __len__ in boolean contexts
        return bool(self.name)

    def __len__(self):
        return len(self.name.strip())


obj_1 = Name()
email_1, email_2, email_3 = (
    OtherName(""),
    OtherName("  "),
    OtherName("jdoe@novus.com"),
)
username_1, username_2, username_3 = (
    YetAnotherName(""),
    YetAnotherName("  "),
    YetAnotherName("jdoe"),
)

print("Truthiness vs Falsiness:")
print(f"    Is False Truthy or Falsy? {bool(False)}")
print(f"    Is None Truthy or Falsy? {bool(None)}")
print(f"    Is 0 Truthy or Falsy? {bool(0)}")
print(f"    Is 0.0 Truthy or Falsy? {bool(0.0)}")
print(f"    Is empty string '' Truthy or Falsy? {bool('')}")
print(f"    Is empty list [] Truthy or Falsy? {bool([])}")
print(f"    Is empty tuple () Truthy or Falsy? {bool(())}")
print(f"    Is empty dictionary {{}} Truthy or Falsy? {bool({})}")
print(f"    Is obj_1 (no __bool__ or __len__ defined) Truthy or Falsy? {bool(obj_1)}")
print(f"    Is email_1 (__len__ defined, but not __bool__) Truthy or Falsy? {bool(email_1)}")
print(f"    Is email_2 (__len__ defined, but not __bool__) Truthy or Falsy? {bool(email_2)}")
print(f"    Is email_3 (__len__ defined, but not __bool__)) Truthy or Falsy? {bool(email_3)}")
print(f"    Is username_1 (both __bool__ and __len__ defined) Truthy or Falsy? {bool(username_1)}")
print(f"    Is username_2 (both __bool__ and __len__ defined) Truthy or Falsy? {bool(username_2)}")
print(f"    Is username_3 (both __bool__ and __len__ defined)Truthy or Falsy? {bool(username_3)}")
