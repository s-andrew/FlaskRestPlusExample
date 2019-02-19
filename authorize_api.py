from flask_restplus import Namespace, Resource, reqparse, fields
from flask import request

from user_dao import user_dao as users


ns = Namespace('auth_demo', doc='/swagger', description='Authorize and authentication demo', path='/auth_demo')

user_auth_data = ns.model('UserData', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})


@ns.route('/registration')
class UserRegistration(Resource):

    @ns.expect(user_auth_data)
    def post(self):
        data = ns.payload
        user_id = users.create_user(data)
        return user_id


@ns.route('/login')
@ns.expect(user_auth_data)
class UserLogin(Resource):
    def post(self):
        username = ns.payload['username']
        user_ = None
        for user in users.get_users():
            if user['username'] == username:
                user_ = user
        if user_ is None:
            return {'message': 'Bad username.'}

        password = ns.payload['password']
        if password != user_['password']:
            return {'message': 'Bad password.'}

        return {'message': 'Login success.'}


@ns.route('/logout/access')
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout.'}


@ns.route('/logout/refresh')
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout.'}


@ns.route('/token/refresh')
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh.'}
    
    
@ns.route('/users1')
class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users.'}
    
    def delete(self):
        return {'message': 'Delete all users.'}
    
    
@ns.route('/secret')
class SecretResource(Resource):
    def get(self):
        return {'answer': 42}

