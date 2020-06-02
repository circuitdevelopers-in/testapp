
#from app.main import app 
  
#if __name__ == "__main__": 
#        app.run() 

from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(8080, EchoFactory())
reactor.run()
