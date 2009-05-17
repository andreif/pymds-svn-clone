import socket
import random

from utils import *

_netmask = None
_cache = None

def init(netmask):
    global _netmask, _cache
    _cache = {}
    if netmask[:2] == '0x':
        base = 16
        netmask = netmask[2:]
    else:
        base = 10
    _netmask = int(netmask,base)

def filter(query, qtype, qclass, src_addr, an_resource_records):
    if qtype != 1 or len(an_resource_records) < 2:
        return an_resource_records
    src_ip = ipstr2int(src_addr[0])
    result = []    
    if _netmask:
        key = str(src_ip & _netmask) + "_" + query
        resource = None
        if key in _cache:
            resource = _cache[key]
            if resource in an_resource_records:
                result.append(resource)
                rest = [x for x in an_resource_records if x != resource]
                result.extend(rest)
            else:
                del _cache[key]
    if not result:
        result = an_resource_records[:]
        random.shuffle(result)
        if _netmask:
            if key not in _cache:
                _cache[key] = result[0]
    return result
