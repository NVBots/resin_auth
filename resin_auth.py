import os
import glob
import json
import hashlib
from resin import Resin
from resin.token import Token

RESIN_API_TOKEN_SALT = os.getenv("RESIN_API_TOKEN_SALT", 'default salt...beware!!')


class ResinAPIToken(object):

    def __init__(self, token_data=None):
        self.token_data = token_data
        self.last_check = None
        self.token = self.update_token()

    def update_token(self, token_data=None):
        if token_data is not None:
            self.token_data = token_data
        if self.token_data is not None:
            self.token = self.parse_token_data(token_data)

    def parse_token_data(self, token_data):
        token = Token()
        token.is_valid_token(self.token_data)
        return token

    def to_dict(self):
        return {
            'token_data': self.token_data,
            'last_check': self.last_check
            }
        
    def to_json(self):
        return json.dumps(self.to_dict())

    def load_from_dict(self, data):
        self.id = data['id']
        self.token_data = data['token_data']
        self.last_check = data['last_check']
        self.update_token()

    def load_from_json(self, string_data):
        self.load_from_dict(json.loads(string_data))


class ResinAPITokenStoreLoadException(Exception):
    pass


class ResinAPITokenStoreUpdateException(Exception):
    pass


class ResinAPITokenStore(object):

    def get_id(self, key, secret, salt=RESIN_API_TOKEN_SALT):
        return hashlib.sha256('{0}{1}{2}'.format(key, secret, salt))
    
    def get_token(self, key, secret, salt=RESIN_API_TOKEN_SALT):
        token_data = self._read_token(self.get_id(key, secret, salt))
        token = Token

    def put_token(self, key, secret, token, salt=RESIN_API_TOKEN_SALT):
        return self._write_token(self.get_id(key, secret, salt), token)

    def _parse_token(self, token_data):
        token = Token()
        token.is_valid_token(self.token_data)
        return token

    def list_tokens(self):
        raise Exception("Abstract class")

    def _read_token(self, id):
        raise Exception("Abstract class")

    def _write_token(self, id, token):
        raise Exception("Abstract class")


class ResinAPITokenFileSystemStore(ResinAPITokenStore):

    def __init__(self, path_to_datastore, file_type='token'):
        self.path_to_datastore = os.path.abspath(os.path.expanduser(path_to_datastore))
        self.file_type = file_type

    def token_file_path(self, id):
        return '{0}/{1}.{2}'.format(self.path_to_datastore, id, self.file_type)

    def list_tokens(self):
        return glob.glob('{0}/*.{1}'.format(self.path_to_datastore, self.file_type))

    def _read_token(self, id):
        token = Token()
        try:
            with open(self.token_file_path(id), 'r') as f:
                token.load_from_json(f.read())
        except Exception as e:
            raise ResinAPITokenStoreLoadException(e.msg)
        return token

    def _write_token(self, id, token):
        try:
            with open(self.token_file_path(id), 'w+') as f:
                f.write(token.to_json())
        except Exception as e:
            raise ResinAPITokenStoreUpdateException(e.msg)
