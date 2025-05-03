import flask_restful as Rest
import flask_jwt_extended as jwt

from repositories import UsersRepository

class AbstractRoutes (Rest.Resource):
    __users_repository = UsersRepository()

    @property
    def logged_user_uuid(self):
        return jwt.get_jwt_identity()

    @property
    def logged_user(self):
        return self.__users_repository.get_by_uuid(self.logged_user_uuid)