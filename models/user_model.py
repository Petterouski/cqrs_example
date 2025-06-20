class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, name):
        self.users.append(name)

    def get_users(self):
        return self.users