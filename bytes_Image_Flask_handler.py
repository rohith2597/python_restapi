"""This is a basic REST API handler using FLask which receives bytes and convert it to the image using Pillow(Python library) 
and then we can save or process the image according to the requirement and a simple JSON response is sent back to the client. 
You can test it using Postman(Tool for testing API).
"""

from flask import Flask, request,jsonify
from PIL import Image
import io

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def upload_file():  
    
        image = request.data
        print(type(image))
        print(image)
        img=Image.open(io.BytesIO(image))
        img.save("test_v1.jpg")
        response=True
        response_body = {
            "response":response,    
        }
        res = (jsonify(response_body), 200) #Response
        return res

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(threaded=True)

