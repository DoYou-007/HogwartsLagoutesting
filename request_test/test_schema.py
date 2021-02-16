import json

import requests
from jsonschema import validate

def test_schema():
    url = 'https://testerhome.com/api/v3/topics.json'
    data = requests.get(url,params={"limit":2}).json()
    schema = json.load(open('topic_schema.json'))
    validate(data,schema=schema)

test_schema()