_netmask
_cache = {}

def init(netmask):
    global _netmask
    _netmask = netmask

def filter(query, qtype, qclass, src_addr, an_resource_records):
    
