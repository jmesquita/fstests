import ESL
from functools import wraps
from nose.tools import make_decorator

HOST = '192.168.200.1'
PORT = '8021'
PASSWORD = 'ClueCon'

class APIBase(object):
    """Base class from which all API based tests will run under"""
    def setup(self):
        """Setup each one of the tests"""
        self._connection = ESL.ESLconnection(HOST, PORT, PASSWORD)
        assert self._connection.connected(), 'Connection could not be established to %s:%s!' % (HOST, PORT)
            
        
    def teardown(self):
        """Teardown connection to ESL"""
        self._connection.disconnect()
        
    def api(self, command, args=[]):
        """Test a random API and returns the event running common checks on the event"""
        e = self._connection.api(command, ' '.join(args))
        assert (e is not None), 'Event returned is NULL!'
        return e
        
        

def check_connection_decorator(fn):
    """Decorator used to check connection"""
    @wraps(fn)
    def wrapper(self, **kwargs):
        """Decorator used to check connection"""
        assert self._connection.connected(), 'Connection could not be established to %s:%s!' % (HOST, PORT)
    return wrapper
        