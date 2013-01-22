from api import APIBase, check_connection_decorator
from nose.tools import istest


class TestShowAPI(APIBase):
    """Test the show API command"""        
    @check_connection_decorator
    def test_show_no_args(self):
        """Test the core show command with no arguments"""
        e = self.api('show')
        assert e.getBody().startswith('-USAGE:')
        