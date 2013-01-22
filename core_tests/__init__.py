import string
import random
from lxml import etree
import json

from api import APIBase, check_connection_decorator
from nose.tools import istest




class TestShowAPI(APIBase):
    """Test the show API command"""        
    commands = ['codec', 'endpoint', 'application', 'api', 'dialplan', 'file', 'timer', 'calls', 'channels', 'calls', \
        'detailed_calls', 'bridged_calls', 'detailed_bridged_calls', 'aliases', 'complete', 'chat', 'management',\
        'modules', 'nat_map', 'say', 'interfaces', 'interface_types', 'tasks', 'limits', 'status']
        
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
        return e
        
    @check_connection_decorator
    def show_args_xml(self, args):
        """Test all show commands as XML and parse it"""
        e = self.api('show', args)
        assert (not e.getBody().startswith('-USAGE:'))
        assert(not e.getBody().startswith('INVALID')), 'FreeSWITCH states this (show %s) is an invalid command!' % (' '.join(args))
        try:
            etree.fromstring(e.getBody())
        except etree.XMLSyntaxError:
            assert False, 'XML Parser failed on\n%s' % e.getBody()
            
    @check_connection_decorator
    def show_args_json(self, args):
        """Test all show commands as JSON and parse it"""
        e = self.api('show', args)
        assert (not e.getBody().startswith('-USAGE:'))
        assert(not e.getBody().startswith('INVALID')), 'FreeSWITCH states this (show %s) is an invalid command!' % (' '.join(args))
        try:
            json.loads(e.getBody())
        except ValueError:
            assert False, 'JSON Parser failed on\n%s' % e.getBody()
            
    def test_random_args(self):
        """Test show comamnd with random args"""
        for i in range(10):
            s = ''.join(random.choice(string.letters) for x in range(5))
            yield self.show_args, s
            
    def test_xml_output(self):
        """Test all XML output"""
        for s in self.commands:
            yield self.show_args_xml,[s, 'as', 'xml']
            
    def test_json_output(self):
        """Test all JSON output"""
        for s in self.commands:
            yield self.show_args_json,[s, 'as', 'json']