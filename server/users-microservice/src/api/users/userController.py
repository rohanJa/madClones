from flask_restful import Resource

from api.users.userSchema import UserSchema
from models.userModel import UserModel

class UserController(Resource):
    
    def get(self):
        user_schema = UserSchema(many=True)
        result = user_schema.dump(list(UserModel.query.all()))

        return result.data, 200