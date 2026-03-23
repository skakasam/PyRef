"""Python Properties Protocol Practice Module"""


class PersonV1:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        print("** Accessor **")
        return self._name

    def set_name(self, new_name: str) -> None:
        print("** Mutator **")
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        elif not new_name:
            raise ValueError("Name cannot be empty")
        elif not new_name.strip():
            raise ValueError("Name cannot be whitespaces")
        else:
            self._name = new_name

    def del_name(self) -> None:
        print("** Deleter **")
        del self._name

    name = property(
        get_name,
        set_name,
        del_name,
        "The person's name",
    )


class PersonV2:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        print("** Accessor **")
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        elif not new_name:
            raise ValueError("Name cannot be empty")
        elif not new_name.strip():
            raise ValueError("Name cannot be whitespaces")
        else:
            message = "** Mutator ("
            message += f"old: {self._name if hasattr(self, '_name') else 'Undefined'}, "
            message += f"new: {new_name}"
            message += ") **"
            print(message)
            self._name = new_name

    @name.deleter
    def name(self) -> None:
        print("** Deleter **")
        del self._name


print(f"{type(PersonV2.name)=}")
person = PersonV2("Alice")
print(f"{person.name=}")
person.name = "Annie"
print(f"{person.name=}")
del person.name
print(f"{hasattr(person, '_name')=}")
person.name = "Bob"
print(f"{hasattr(person, '_name')=}")
