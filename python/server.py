from ai import AI
from flask import Flask, request, jsonify
from io import BytesIO
import base64
from PIL import Image
from numpy import save
from photo import ImageNoiser


app = Flask(__name__)


@app.route('/image', methods=['POST'])
def hello():
    print(request.files)
    file = request.files['image']
    img = ImageNoiser(file)
    # img.savefig("hello.png")
    print(img)

    my_stringIObytes = BytesIO()
    img.savefig(my_stringIObytes, format='jpg')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return jsonify({'msg': 'success', 'size': str(my_base64_jpgData)})


@app.route('/ai', methods=['GET'])
def ai():
    mode = request.args.get('mode')
    country = request.args.get('country')
    print(mode, country)
    img = AI(mode, country)
    my_stringIObytes = BytesIO()
    img.savefig(my_stringIObytes, format='png')
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    return jsonify({'msg': 'success', 'size': str(my_base64_jpgData)})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
