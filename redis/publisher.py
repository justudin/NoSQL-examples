# Publisher

import redis
publisher = redis.Redis(host = 'localhost', port = 6379)
message=""
channel = "bigdataclass"
while(message!="exit"):
    message = input("")
    send_message = message
    publisher.publish(channel, send_message)