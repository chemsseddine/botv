# Installation

```
pip install botv
```

# Usage

```
from botv.output import Output

message = Output()

message.as_dict

> {'entities': {}, 'output': {'response': None, 'templates': [], 'quickReplies': []}}

# To Add Entities

message.add_entity(entity1="value1", entity2="value2")

> {'entities': {'entity1':'value1', 'entity2':'value2'}, 'output': {'response': None, 'templates': [], 'quickReplies': []}}

# To Add Response

message.add_response('some response')

> {'entities': {'entity1':'value1', 'entity2':'value2'}, 'output': {'response': 'some response', 'templates': [], 'quickReplies': []}}

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

templates = [{
  "action_url":"https://go.to.this.url",
  "image_url":"https://image.png",
  "title":"someTitle",
  "subtitle":"some sub title"
}]

message.add_template(templates)

```


