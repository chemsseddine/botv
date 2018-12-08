# Installation

```
pip install botv
```

# Usage

```
from botv.output import Output

message = Output()

> {'entities': {}, 'output': {'response': None, 'templates': [], 'quickReplies': []}}

# To Add Entities

message.add_entity(entity1=value1, entity2=value2)

# To Add Response

message.add_response('some response')

# Or when instantiating the object message

new_message = Output("Hello World !")

# To add Facebook quick Replies

quick_replies = [{
"targetIntent":"intentName",
"type":"text",
"title":"someTitle",
"text":"some text"
}]

message.add_qr(quick_replies)

# To add Facebook Templates
['action_url', 'image_url', 'subtitle', 'title']

templates = [{
  "action_url":"https://go.to.this.url",
  "image_url":"https://image.png",
  "title":"someTitle",
  "subtitle":"some sub title"
}]

message.add_template(templates)

```


