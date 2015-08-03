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
# call, , used to translate paths using cygpath if you're running cygwin
from subprocess import call

# constants
cache_location = os.path.expanduser('~/.yotta/cache/')

<<<<<<< HEAD
#if (os.name == 'posix') and os.environ['OS'] == 'Windows_NT':
#    print("Cygwin Detected, translating cache_location")
#    #TODO: need to redirect stdout to cache_location to capture the path for cygwin posix conversions
#    cache_location =  call(["cygpath","-a","-w", cache_location])
=======
#if os.name == 'posix':
#    cache_location = 
>>>>>>> d3c918ad8bbbe05da58ff8fd612f953352eab901

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
    logging.debug("setting cache file %s with contents %s" % (fname,value))
    with open((cache_location+fname),'w+') as f:
        json.dump(value,f)
    return


    


