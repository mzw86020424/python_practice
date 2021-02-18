# class User:
#     pass

# tom = User()
# tom.name = "tom"
# tom.score = 20

# bob = User()
# bob.name = "bob"
# bob.level = 5

# print(tom.name)
# print(bob.level)

class User:
    def __init__(self, name):
        self.name = name


tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
