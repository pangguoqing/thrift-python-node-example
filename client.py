#!/usr/bin/env python
import sys

from genpy.user import UserStorage
from genpy.user.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
	#Make a socket
	transport = TSocket.TSocket('localhost', 9090)

	transport = TTransport.TFramedTransport(transport)

	protocol = TBinaryProtocol.TBinaryProtocol(transport)

	client = UserStorage.Client(protocol)

	transport.open()

	user = UserProfile()
	user.uid = 1000
	user.name = "Jeff Gonzalez"
	user.blurb = "Python Thrift"

	client.store(user)
	something = client.retrieve(1000)

	transport.close()

except Thrift.TException, tx:
	print '%s' % (tx.message)
