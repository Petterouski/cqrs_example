from models.user_model import UserModel

class AddUserCommand:
    def __init__(self, model):
        self.model = model

    def execute(self, name):
        self.model.add_user(name)