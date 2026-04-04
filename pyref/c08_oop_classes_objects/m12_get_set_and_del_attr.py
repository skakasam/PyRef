"""Python getattr, setattr, and delattr Usage Practice"""

################################################################################
# 1. def _getattr__(self, name) -> Any:
#    This method is called when the requested attribute is not found in the
#    usual places (i.e., the instance's __dict__ and the class's __dict__).
# 2. def _getattribute__(self, name) -> Any:
#    This method is called unconditionally when any attribute is accessed.
# 3. def _setattr__(self, name, value) -> None:
#    This method is called when an attribute is set.
# 4. def _delattr__(self, name) -> None:
#    This method is called when an attribute is deleted.
################################################################################


class Catcher:
    def __getattr__(self, attr):
        print("Get:", attr)

    # Same as __getattr__, works on all attribute fetches
    # But prone to loops in general
    def __getattribute__(self, attr):
        print("Getattribute:", attr)

    def __setattr__(self, attr, value):
        print("Set:", attr, value)


X = Catcher()
X.job
X.pay
X.pay = "bread"


class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attr):
        print("Getattr:", attr)
        return getattr(self.wrapped, attr)


X = Wrapper([1, 2, 3])
X.append(4)
print(X.wrapped)


# Practical Example
class Label:
    def __init__(self, text: str):
        self._text = text  # Triggers __setattr__

    def __getattr__(self, attr):
        print("get:", attr)
        if attr == "text":
            return self._text
        else:
            raise AttributeError(f"'Label' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        print("set:", attr, value)
        if attr == "text":
            attr = "_text"
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print("del:", attr)
        if attr == "text":
            attr = "_text"
        del self.__dict__[attr]

    def __str__(self):
        return f"Label: {self._text}"


label = Label("Hello")
print(label.text)  # Triggers __getattr__
label.text = "World"  # Triggers __setattr__
print(label.text)  # Triggers __getattr__
del label.text  # Triggers __delattr__
# print(label.text)  # This would raise an AttributeError
