import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_log_in = False

    def _encrypt_pw(self, password):
        hash_string = self.username + password
        hash_string = hash_string.encode('utf8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

class AuthException(Exception):
    def __init__(self, username, user = None):
        super().__init__(username)
        self.username = username
        self.user = user

class UserNameExist(AuthException):
    pass

class PasswordError(AuthException):
    pass


class PermissionError(AuthException):
    pass

class LoginError(AuthException):
    pass

class Auth:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserNameExist(username)
        if len(password) < 6:
            raise PasswordError(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise UserNameExist(username)

        if not user.check_password(password):
            raise PasswordError(username, user)

        user.is_log_in = True
        return True

    def is_log_in(self, username):
        if username in self.users:
            return self.users[username].is_log_in
        return False
    
class Authz:
    def __init__(self, auth):
        self.auth = auth
        self.permissions = {}

    def add_permission(self, per_name):
        try:
            per_set = self.permissions[per_name]
        except KeyError:
            self.permissions[per_name] = set()
        else:
            raise PermissionError('Permission Exist')

    def permit_user(self, per_name, username):
        try:
            per_set = self.permissions[per_name]
        except KeyError:
            raise PermissionError('Permission does not exist')
        else:
            if username not in self.auth.users:
                raise UserNameExist(username)
            per_set.add(username)

    def check_permission(self, per_name, username):
        if not self.auth.is_log_in(username):
            raise LoginError(username)
        try:
            per_set = self.permissions[per_name]
        except KeyError:
            raise PermissionError('Permission does not exist')
        else:
            if username not in per_set:
                raise PermissionError(username)
            else:
                return True


auth = Auth()
authz = Authz(auth)

