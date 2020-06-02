
#from app.main import app 
  
#if __name__ == "__main__": 
#        app.run() 

from twisted.internet import protocol, reactor
import os
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

port = int(os.environ.get('PORT', 8012))
reactor.listenTCP(port, EchoFactory(), interface = '0.0.0.0')
reactor.run()
