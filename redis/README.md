# Redis python example 

Real-time Pub/Sub system using Redis (key-value store): https://redis.io/download

![image.png](https://dashbird.io/wp-content/uploads/2021/01/pub-sub-messaging.png)
*Source: https://dashbird.io/wp-content/uploads/2021/01/pub-sub-messaging.png*

## library

- Python3, can install miniconda or anaconda
- Python Redis client: pip install redis



```python
!pip install redis
```

## Key Value Example


```python
# Set a key-value
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('bigdatakey', 'Hey, It is working!')
```


```python
# Getting a value from a key
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.get('bigdatakey')
```

### From terminal, you can type: 
*redis-cli get bigdatakey*

## Pub-Sub Example


```python
# Publisher

import redis
publisher = redis.Redis(host = 'localhost', port = 6379)
message=""
channel = "bigdataclass"
while(message!="exit"):
    message = input("")
    send_message = message
    publisher.publish(channel, send_message)
```


```python

```

## Pub-Sub Example


```python
# Subscriber

import redis
subscriber = redis.Redis(host = 'localhost', port = 6379)
channel = 'bigdataclass'
p = subscriber.pubsub()
p.subscribe(channel)
while True:
    message = p.get_message()
    if message and not message['data'] == 1:
        message = message['data'].decode('utf-8')
        print(message)
```


```python

```
