from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/sayname')
def hello_world():
    request_data = request.args
    json_object = request_data.get('json', '')
    url_arg = json.loads(json_object)
    user_detail={}
    user_detail['First_Name'] = url_arg['fname']
    return 'First name is = ' + user_detail['First_Name']


if __name__ == '__main__':
    app.run(port=8000,host='127.200.0.5',debug=True)
