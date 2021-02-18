# from user import User, AdminUser
# from mypackage.user import User, AdminUser
import mypackage.user


bob = mypackage.user.AdminUser("bob", 23)

print(bob.name)
bob.say_hello()
bob.say_hi()
