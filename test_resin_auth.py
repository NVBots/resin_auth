import pytest
import os
import glob
import json
import hashlib
from resin import Resin
from resin.token import Token
import resin_auth
import jwt


@pytest.fixture()
def token_data():
    return {
        'test':data
    }

@pytest.fixture()
def token_string(token_data):
    return jwt.encode(token_data, 'test')

@pytest.fixture(scope="session")
def token(token_string):
    t = Token()
    t.set(token_string)
    return t

@pytest.fixture()
def key():
    return "test key"

@pytest.fixture()
def secret():
    return "test secret"

@pytest.fixture()
def salt():
    return "test_salt"

@pytest.fixture()
def resin_api_token_store(key):


class TestResinAPITokenStore(object):

    def test_get_id(self, key, secret, salt):
        assert 0
    
    def test_get_token(self, key, secret, salt):
        assert 0

    def test_put_token(self, key, secret, token, salt):
        assert 0

    def test_list_tokens(self):
        assert 0

    def test__read_token(self, id):
        assert 0

    def test__write_token(self, id, token):
        assert 0


class TestResinAPITokenFileSystemStore(object):

    def test__init__(self, path_to_datastore, file_type='token'):
        assert 0

    def test_token_file_path(self, id):
        assert 0

    def test_list_tokens(self):
        assert 0
    def test__read_token(self, id):
        assert 0

    def test__write_token(self, id, token):
        assert 0
