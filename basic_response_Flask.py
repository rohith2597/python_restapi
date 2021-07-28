from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def upload_file():  
    
        image = request.data
        print(type(image))
        print(image)
        response=True
              
        response_body = {
            "response":response,    
        }
        res = (jsonify(response_body), 200) #Response
        return res

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(threaded=True)
