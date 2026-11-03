import flask

app = flask.Flask(__name__)


@app.route('/healthy')
def healthy():
    return '', 200


@app.route('/channels/<channel>', methods=['POST'])
def publish(channel):
    # should return okay
    return {}


@app.route('/channels/<channel>', methods=['GET'])
def get(channel):
    # paginated messages
    return {
        'messages': ['msg_1', 'msg_2']
    }


@app.route('/')
def index():
    # return all channels
    return {
        'channels': ['channel1', 'channel2']
    }
