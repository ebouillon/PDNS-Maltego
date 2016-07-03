#############################################
# PDNS API DNS Name to IP
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
        domain = sys.argv[1]
        mt = MaltegoTransform()
        mt.addUIMessage("[INFO] " + domain + " to IP")
        try:
            retrieveIP(mt, domain)
        except Exception as e:
            mt.addUIMessage("[Error] " + str(e))
        mt.returnOutput()


