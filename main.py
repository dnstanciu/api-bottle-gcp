from bottle import Bottle, request, response

import json

app = Bottle()

my_fruits = set()

@app.get('/')
def hello():
    return "Hello!"

@app.get('/api')
def get_fruits():
    return json.dumps({ "fruits" : list(my_fruits) }) 

@app.post('/api')
def add_fruit():
    try:
        data = request.json
        fruit = data["fruit"] 
    except (ValueError, KeyError):
        response.status = 400
        return

    my_fruits.add(fruit) # add to set

    return json.dumps({ "fruit" : fruit })

#app.run(host="localhost", port=8080)
