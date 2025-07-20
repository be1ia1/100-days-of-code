class User:
    def __init__(self, user_id, username, age):
        self.age = age
        self.id = user_id
        self.name = username

    def yel(self, word):
        print(self.word.capitalize())


user1 = User(user_id='001', username='Andrii', age=43)

print(user1.name)
user1.yel('hello')