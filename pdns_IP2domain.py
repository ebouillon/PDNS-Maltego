#############################################
# PDNS API IP to DNS Name
# 
# Author: Emmanuel Bouillon
# Email:  emmanuel.bouillon.sec@gmail.com
# Date: 11/06/2015
#############################################
import sys
import json
import pypdns
from pdns_util import *

if __name__ == '__main__':
        ip = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage("[INFO] " + ip + " to DNS Name")
        try:
            retrieveDomain(mt, ip)
        except Exception as e:
            mt.addUIMessage("[Error] " + str(e))
        mt.returnOutput()


