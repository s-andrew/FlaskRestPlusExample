from flask import request, session
from flask_restplus import Namespace, Resource, reqparse
from flask_restplus import fields

from user_dao import user_dao as users

ns = Namespace('users', doc='/swagger', description='User REST API')

pagination = reqparse.RequestParser()
pagination.add_argument('page', type=int, required=False, default=1, help='Page number', location='args')
pagination.add_argument('per_page', type=int, required=False, choices=[10, 20, 30, 40, 50], default=10, location='args')

header_arguments = reqparse.RequestParser()
header_arguments.add_argument('X-User-Agent', help='User agent header', type=str, required=False, location='header')

user_model = ns.model('User', {
    'title': fields.String(description='User title'),
    'surname': fields.String(description='User surname'),
    'name': fields.String(description='User name'),
    'email': fields.String(description='User email'),
    'username': fields.String(description='User username'),
    'password': fields.String(description='User password')
})


@ns.route('/')
class UserCollection(Resource):

    @ns.marshal_list_with(user_model)
    @ns.expect(pagination, validate=True)
    def get(self):
        '''
        Get users collection

        Full description
        '''
        args = pagination.parse_args(request)
        page = args['page']
        per_page = args['per_page']
        print(*dir(session), sep='\n')
        headers = header_arguments.parse_args(request)
        user_agent = headers['X-User-Agent']

        return users.get_users(per_page, per_page*(page-1))

    @ns.expect(user_model)
    def post(self):
        '''
        Create new user

        Full description
        '''
        user = ns.payload
        users.create_user(user)
        return 'create users'


@ns.route('/<int:user_id>')
@ns.response(404, 'User not found.')
@ns.param('user_id', 'User id')
class UserItem(Resource):

    @ns.marshal_with(user_model)
    def get(self, user_id):
        '''
        Get user by id

        Full description
        '''
        return users.get_user(user_id)

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        '''
        Update user by id

        Full description
        '''
        user = ns.payload
        user = users.update_user(user_id, user)
        return user, 200

    @ns.response(204, 'User successfully deleted.')
    def delete(self, user_id):
        '''
        Delete user by id

        Full description
        '''
        users.delete_user(user_id)
        return None, 204

