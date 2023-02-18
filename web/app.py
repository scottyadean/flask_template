from flask import Flask, jsonify, request
from urllib.parse import urlparse
from pymongo import MongoClient


app = Flask(__name__)


client = MongoClient("mongodb://db:27017")
db = client.helloWorld
col = db["number_of_users"]

col.insert_one({
    "count": 0
})


@app.route("/")
def hello_world():
    """ return simple message to the req. """
    url = urlparse(request.base_url)
    uri = f"{url.scheme}://{url.netloc}"
    links = [ f"{uri}/get/example", f"{uri}/post/exampl",
              f"{uri}/put/example", f"{uri}/delete/example" ]
    return jsonify(links)


@app.route("/get/example")
def get_example():
    """ return json """
    cnt = col.find({})[0]['count']
    inc = cnt + 1
    col.update_one({}, { "$set": { "count" : inc }  })
    return jsonify({ "number of visits":  str(cnt) } )


@app.route("/post/example", methods=["POST"])
def post_example():
    """ handle post req  """
    data = request.get_json()
    data["endpoint"] = """
        @app.route('/post/example', methods=['POST'])
        def post_example():
            data = request.get_json()
            return jsonify(data)
    """
    return jsonify(data)


@app.route("/put/example", methods=["PUT"])
def put_example():
    """example put return json """
    return jsonify({ "message": "Put method example" } )

@app.route("/delete/example", methods=["DELETE"])
def delete_example():
    """example delete return json """
    return jsonify({ "message": "Delete method example" } )


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
