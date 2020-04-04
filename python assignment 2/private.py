#example of private access modifier
class Modifiers:

    def __init__(self, name):
        self.__private_member = name                                          # Private Attribute

print("___________Output_____________")
m = Modifiers("PYTHON")
print(m._Modifiers__private_member)
m._Modifiers__private_member = "Github"
print(m._Modifiers__private_member)
