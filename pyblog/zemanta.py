#!/usr/bin/env python

"""zemanta.py: Get suggestions from zemanta.

Last modified: Sat Jan 18, 2014  05:01PM

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2013, Dilawar Singh"
__license__          = "GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@iitb.ac.in"
__status__           = "Development"
import urllib

import urllib
import simplejson
from pprint import pprint

def getZemantaSuggestion(key, text):
    gateway = 'http://api.zemanta.com/services/rest/0.0/'
    args = {'method': 'zemanta.suggest',
            'api_key': '{}'.format(key),
             'text' : '{}'.format(text)
            'return_categories': 'dmoz',
            'format': 'json'}            
    args_enc = urllib.urlencode(args)
    raw_output = urllib.urlopen(gateway, args_enc).read()
    output = simplejson.loads(raw_output)
    return output
