import pytest
import os
import glob
import json
import hashlib
from resin import Resin
from resin.token import Token
import resin_auth
@pytest.fixture()
def resin_token():


class TestResinAPIToken(object):

    def test__init(self, key, secret, resin_token_string):
        assert 0

    def test_update_token(self, resin_token_string):
        assert 0

    def test_parse_token_data(self, resin_token_string):
        assert 0

    def test_to_dict(self, token):
        assert 0
        
    def test_to_json(self, token):
        assert 0

    def test_load_from_dict(self, dict_token):
        assert 0

    def test_load_from_json(self, json_token):
        assert 0


class TestResinAPITokenStore(object):

    def test_get_id(self, key, secret, salt=RESIN_API_TOKEN_SALT):
        return hashlib.sha256('{0}{1}{2}'.format(key, secret, salt))
    
    def test_get_token(self, key, secret, salt=RESIN_API_TOKEN_SALT):
        return self._read_token(self.get_id(key, secret, salt))

    def test_put_token(self, key, secret, token, salt=RESIN_API_TOKEN_SALT):
        return self._write_token(self.get_id(key, secret, salt), token)

    def test_list_tokens(self):
        raise Exception("Abstract class")

    def test__read_token(self, id):
        raise Exception("Abstract class")

    def test__write_token(self, id, token):
        raise Exception("Abstract class")


class TestResinAPITokenFileSystemStore(ResinAPITokenStore):

    def __init__(self, path_to_datastore, file_type='token'):
        self.path_to_datastore = os.path.abspath(os.path.expanduser(path_to_datastore))
        self.file_type = file_type

    def test_token_file_path(self, id):
        return '{0}/{1}.{2}'.format(self.path_to_datastore, id, self.file_type)

    def test_list_tokens(self):
        return glob.glob('{0}/*.{1}'.format(self.path_to_datastore, self.file_type))

    def test__read_token(self, id):
        token = Token()
        file_path = 
        try:
            with open(self.token_file_path(id), 'r') as f:
                token.load_from_json(f.read())
        except Exception as e:
            raise ResinAPITokenStoreLoadException(e.msg)
        return token

    def test__write_token(self, id, token):
        try:
            with open(self.token_file_path(id), 'w+') as f:
                f.write(token.to_json())
        except Exception as e:
            raise ResinAPITokenStoreUpdateException(e.msg)
