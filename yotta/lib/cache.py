# Copyright 2014 ARM Limited
#
# Licensed under the Apache License, Version 2.0
# See LICENSE file for details.

# standard library modules, , ,
import logging
import os
#import threading 

# fsutils, , misc filesystem utils, internal
import fsutils

# constants
cache_file = os.path.expanduser('~/.yotta/cache.json')

if os.name == 'nt':
    cache_file += [
        os.path.expanduser(os.path.join(folders.prefix(),'cache.json'))
    ]

# public API

def get(section):
    logging.debug("getting %s" %section)
    with open(cache_file,'r') as f:
        x = json.load(f)
        if section in x:
            logging.debug("value = %s" % x.section)
            return x.section
        else:
            return []

def getProperty(section, name):
    logging.debug("getting property %s.%s" % (section , name))
    return get(section + '.' + name)

def set(section, value):
    logging.debug("setting section %s to value %s" % (section,value))
    with open(cache_file,'rw') as f:
        x = json.load(f)
        x.section = value
        json.dump(x,f)
    
def setProperty(section, name, value):
    logging.debug("setting property section %s, name %s, value %s" % (section,name,value))
    set(section+'.'+name, value)

