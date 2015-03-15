#!/usr/bin/env python

import requests, logging
#from BeautifulSoup import BeautifulSoup

msgLogger= logging.getLogger('MSG')

def response(oadc, message):
    
    #stub
    #return "ok, funge"
    #r = requests.get('http://tomduck:8080/ws/eta.jsp?n='+message)
    r = requests.get('http://priapo:8080/wap/eta.jsp?n='+message)
    #print r.url
    if r.status_code == 200:
      #soup = BeautifulSoup(r.text)
      resp = r.text.encode('utf-8')
      msgLogger.info('"%s","%s","%s"',oadc,message,resp.replace("\n"," ").replace("   ",""))
      return resp
    else:
      return 'Servizio momentaneamente non disponibile'
