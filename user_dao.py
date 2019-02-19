


class UserDAO:
    def __init__(self):
        with open('users.txt') as file:
            users = [eval(row) for row in file.readlines()]
            self.users = {user.get('id'): user for user in users}

    def get_users(self, limit=None, offset=None):
        from_ = 0 if offset is None else offset
        to = None if limit is None else from_ + limit
        return list(self.users.values())[from_: to]

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def create_user(self, user):
        new_id = max(self.users.keys()) + 1
        user['id'] = new_id
        self.users[new_id] = user
        return new_id

    def update_user(self, user_id, user):
        self.users[user_id] = user
        return user

    def delete_user(self, user_id):
        self.users.pop(user_id)
        return


user_dao = UserDAO()