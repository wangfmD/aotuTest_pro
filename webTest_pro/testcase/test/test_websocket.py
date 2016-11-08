from websocket import create_connection

ws = create_connection("ws://10.1.0.56:8232/interactbusiness/websocket")
print "Sending 'Hello, World'..."
ws.send("Hello, World")
print "Sent"
print "Receiving..."
result = ws.recv()
print "Received '%s'" % result
ws.close()
