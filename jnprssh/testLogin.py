import unittest
from jnprssh import login
from simplejson.tests.test_encode_basestring_ascii import CASES

class TestLogin(unittest.TestCase):
    """
    Basic test CASES
    """
    def testLogin(self):
        try:
            conn = login.JnprConn()
            handle = conn.login('root', 'Embe1mpls', 'contrail-config', 'sw-qfx-elit-02')
            print("Login test passed")
            login.JnprConn.logout(conn, handle)
        except Exception as e:
            s = str(e)
            print("Login failed %s", s)
    
        