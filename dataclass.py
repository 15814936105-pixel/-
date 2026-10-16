from dataclasses import dataclass
@dataclass
class user:
    username:str
    user_account:str
    user_password:str
users = []
users.append(user("kekaiyang", "1234", "1234"))
users.append(user("mike", "ss", "ee"))
print(users)
print(users[0])
