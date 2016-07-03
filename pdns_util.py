#############################################
# PDNS API miscellaneous functions.
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2016
#############################################

# BASE URL (CIRCL)
BASE_URL = 'https://www.circl.lu/pdns/query'
# Login (basic auth)
LOGIN = '<YOUR LOGIN>'
# Password (basic auth)
PASSWORD = '<YOUR PASSWORD>'
# Max nb of results (otherwise Maltego gets sick)
MAX = 50

import pypdns
import json
import re
import datetime
from MaltegoTransform import *

def init():
    return pypdns.PyPDNS(url=BASE_URL, basic_auth=(LOGIN, PASSWORD))

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def retrieveIP(mt, domain):
    pdns = init()
    result = pdns.query(domain)
    for r in result:
        record = json.loads(json.dumps(r, default=date_handler))
        if record['rrtype'] == 'A':
            first = record['time_first'].split('T')[0]
            last = record['time_last'].split('T')[0]
            me = MaltegoEntity('maltego.IPv4Address',record["rdata"].rstrip('.'));

            me.addAdditionalFields('link#maltego.link.label', 'linklabel', False, first + ' - ' + last)
            mt.addEntityToMessage(me);
    return

def retrieveDomain(mt, ip):
    pdns = init()
    result = pdns.query(ip)
    for r in result:
        record = json.loads(json.dumps(r, default=date_handler))
        if record['rrtype'] == 'A':
            first = record['time_first'].split('T')[0]
            last = record['time_last'].split('T')[0]
            me = MaltegoEntity('maltego.Domain',record["rrname"].rstrip('.'));

            me.addAdditionalFields('link#maltego.link.label', 'linklabel', False, first + ' - ' + last)
            mt.addEntityToMessage(me);
    return

