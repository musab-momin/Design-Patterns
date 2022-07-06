from user_module import User
from account_module import Account
from email_module import EmailSender
from inheritance_module import Button, TextField
from polymorphism_module import Orchids, Owl

# user_obj = User('Musab')
# print(user_obj.name)


#Encapsulaiton 
#I can't directly access the variable of Account class bcoz of encapsulation

# account = Account();
# account.deposite(200)
# print(account.getBalance()) #output: 200
# account.deposite(100) #account balance is now 300
# account.withdraw(200)
# print('remaining balance', account.getBalance())


#Abstraction
# obj = EmailSender()
# obj.send_email()


#Inheritance
#as here TextField and Button class inherit focus and border method from behaviour class 
# this is inheritance

# name_field = TextField()
# name_field.focus()
# name_field.border()
# name_field.write()

# print('')
# print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
# print('')

# submit_button = Button()
# submit_button.focus()
# submit_button.border()
# submit_button.click()


#Polypormishm
#In this case fly have different forms in orchid fly is use for can not fly but in owl 
#it is used for flying like as we One object/fucntion have many forms
# orchid = Orchids()
# orchid.wings()
# orchid.fly()

# print('')
# print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
# print('')

# owl = Owl()
# owl.wings()
# owl.fly()

