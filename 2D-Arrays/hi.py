class User:
    def __init__(self,name,email,contact_no):
        self.name = name
        self.email = email
        self.phone = contact_no

    def greet(self,user):
        print(f"Hi {user.name}. My name is {self.name}")


user1 = User("akash","abc@gmail.com",1234)

user2 = User("nimrah","oih@gmail.com",567)

user1.greet(user2)

