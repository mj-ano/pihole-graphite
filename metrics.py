#! /usr/bin/python


import requests
import socket
import time
import platform

HOSTNAME = "a6f130f9-3b08-4e40-886b-90dab9a41368.pi-hole"
CARBON_SERVER = "d3024505.carbon.hostedgraphite.com"
CARBON_PORT = 2003
DELAY = 60 # seconds

def send_msg(message):
    print ('sending message:\n%s' % message)
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(message)
    sock.close()

if __name__ == '__main__':

          api = requests.get('http://192.168.0.111/admin/api.php')
          API_out = api.json()

          domains_blocked = (API_out['domains_being_blocked']).replace(',', '')
          dns_queries_today = (API_out['dns_queries_today']).replace(',', '')
          ads_percentage_today = (API_out['ads_percentage_today'])
          ads_blocked_today = (API_out['ads_blocked_today']).replace(',', '')

          timestamp = int(time.time())

          lines = [
                '%s.domains_blocked %s' % (HOSTNAME, domains_blocked),
                '%s.dns_queries_today %s' % (HOSTNAME, dns_queries_today),
                '%s.ads_percentage_today %s' % (HOSTNAME, ads_percentage_today),
                '%s.ads_blocked_today %s' % (HOSTNAME, ads_blocked_today)
          ]
          message = '\n'.join(lines) + '\n'
          send_msg(message)
