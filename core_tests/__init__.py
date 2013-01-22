import string
import random
from api import APIBase, check_connection_decorator
from nose.tools import istest


class TestShowAPI(APIBase):
    """Test the show API command"""        
    @check_connection_decorator
    def test_show_no_args(self):
        """Test the core show command with no arguments"""
        e = self.api('show')
        assert e.getBody().startswith('-USAGE:')
        
    @check_connection_decorator
    def show_args(self, args):
        """Test the core show command with one argument"""
        e = self.api('show', args)
        assert e.getBody().startswith('-USAGE:')
        
    @check_connection_decorator
    def test_show_rand_args(self):
       """Test the core show command with random arguments"""
       e = self.api('show', ['asdasdasdad', 'asdasdasdasd'])
       assert e.getBody().startswith('-USAGE:')
        
    def test_random_args(self):
        """Test show comamnd with random args"""
        for i in range(10):
            yield self.show_args, ''.join(random.choice(string.letters) for x in range(5))