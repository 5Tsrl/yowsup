from etaLayer import EtaLayer
#from echoLayer import EchoLayer
from yowsup.layers.auth                        import YowAuthenticationProtocolLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.protocol_iq                 import YowIqProtocolLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStack, YOWSUP_CORE_LAYERS
from yowsup import env

#raf
import logging

logging.basicConfig(filename='wapper.log',level=logging.INFO, format='%(asctime)s %(message)s')
logging.info('Wapper started...')


msgLogger = logging.getLogger("MSG")
msgLogger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s, %(message)s")
handler = logging.FileHandler("messaggi.log")
handler.setFormatter(formatter)
msgLogger.addHandler(handler)


#muletto
#CREDENTIALS = ("393666538819", "hVN5mCgraHfB+bdQotTpP2Jrg78=") # replace with your phone and password
#salaregia
#CREDENTIALS = ("393421884433", "EXJUWBtJfbgEkya/83bCG5zBAIQ=") # replace with your phone and password
#c3
CREDENTIALS = ("393666536772", "RqM5uSnbC88FFJeHMefrPzfJ1xo=") # replace with your phone and password

if __name__==  "__main__":
    layers = (
        EtaLayer,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer, YowIqProtocolLayer)
    ) + YOWSUP_CORE_LAYERS

    stack = YowStack(layers)
    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)              
    stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())          #info about us as WhatsApp client

    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal

    stack.loop() #this is the program mainloop
