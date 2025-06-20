from models.user_model import UserModel

class GetUsersQuery:
    def __init__(self, model):
        self.model = model

    def execute(self):
        return self.model.get_users()