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
# json, , read / write cache as json 
import json
# checklocation, , used to translate paths using cygpath if you're running cygwin
import subprocess

# constants
cache_location = os.path.expanduser('~/.yotta/cache/')

#cygwin
if (os.name == 'posix') and os.environ['OS'] == 'Windows_NT':
    logging.debug("Cygwin Detected, translating cache_location")
    cache_location = subprocess.check_output(['cygpath','-a','-w',cache_location])
    cache_location = cache_location.replace('\n','')


# public API used to access the "cache"

def get(fname):
    logging.debug("getting file %s" %fname)
    #if file exists, return contents
    if(os.path.isfile((cache_location+fname))):
        with open(cache_location+fname,'r') as f:
            x = json.load(f)
            logging.debug("Got values: %s" %x)
            return x
    # file doesnt exist, return empty dictionary
    else:
        logging.debug("file "+fname+" doesnt exist, returning empty dictionary")
        return []

def set(fname, value):
    if not os.path.exists(cache_location):
        os.mkdir(cache_location)
        logging.debug("cache directory didn't exist at <%s> so I created it" %cache_location)
    logging.debug("setting cache file %s with contents %s" % (fname,value))
    with open((cache_location+fname),'w+') as f:
        json.dump(value,f)
    return


    


