# PDNS-Maltego
Set of Maltego transforms to interface with CIRCL Passive DNS

# Prerequisites
- Python Library to access CIRCL Passive DNS (see https://www.circl.lu/services/passive-dns/)

# INSTALL

- Edit pdns_util.py and set LOGIN and PASSWORD variables.

- Import transforms in Maltego:
   * pdns_IP2domain.py: [CIRCL] IP to domain / Returns domains for IP
   * pdns_domain2IP.py: [CIRCL] Domain to IP / Returns IPs seen resolving domain
