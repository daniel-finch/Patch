import base64
import unittest
import requests
import requests_ntlm
import warnings

from test_utils import domain, username, password


class TestRequestsNtlm(unittest.TestCase):

    def setUp(self):
        self.test_server_url        = 'http://localhost:5000/'
        self.test_server_username   = '%s\\%s' % (domain, username)
        self.test_server_password   = password
        self.auth_types = ['ntlm','negotiate','both']

    def test_requests_ntlm(self):
        for auth_type in self.auth_types:
            res = requests.get(\
                url  = self.test_server_url + auth_type,\
                auth = requests_ntlm.HttpNtlmAuth(
                    self.test_server_username,\
                    self.test_server_password))

            self.assertEqual(res.status_code,200, msg='auth_type ' + auth_type)