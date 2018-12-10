# Installation

```
pip install botv
```

# Usage

```
from botv.output import Output

message = Output()
message.as_dict
```
```
> {'entities': {}, 'output': {'response': None, 'templates': [], 'quickReplies': []}}
```

### Entities
```
message.add_entity(entity1="value1", entity2="value2")
```
```
> {'entities': {'entity1':'value1', 'entity2':'value2'}, 'output': {'response': None, 'templates': [], 'quickReplies': []}}
```
### Response

```
message.add_response('some response')
```
```
> {'entities': {'entity1':'value1', 'entity2':'value2'}, 'output': {'response': 'some response', 'templates': [], 'quickReplies': []}}
```
```
# Or when instantiating the object message

new_message = Output("Hello World !")
```

### Facebook quick Replies
```
quick_replies = [{
    "targetIntent":"intentName",
    "type":"text",
    "title":"someTitle",
    "text":"some text"
}]

message.add_qr(quick_replies)
```
### Facebook Templates

```
templates = [{
  "action_url":"https://go.to.this.url",
  "image_url":"https://image.png",
  "title":"someTitle",
  "subtitle":"some sub title"
}]

message.add_template(templates)
```


## Flask

```
from flask import Flask, jsonify
from botv.output import Output

app = Flask(__name__)

@app.route('/')
def home():
    message = Output()
    message.add_entity(ent1="val1")
    message.add_response("Hello from Flask")
    return jsonify(message.as_dict)
    
```

## Flask Restful

```
from flask_restful import Resource, Api
from flask import Flask
from botv.output import Output

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        message = Output("Hello")
        message.add_entity(solde="5544")
        return message.as_dict

api.add_resource(Home, '/')
    
```

    
