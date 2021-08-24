""" This a basic Flask server(REST API handler) which handler the requests coming to this server. It receives the data and send JSON response """


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

    
""" Flask server to handle the incoming JSON format messages """
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/json', methods=['POST'])
def upload_file():  
    
        print(request.is_json)
        data = request.get_json()
        print(data['room'])
        temp = data['Temperature']
        print(temp)
        humi = data['Humidity']
        print(humi)
        response=True
        response_body = {
            "response":response,    
        }
        res = (jsonify(response_body), 200) #Response
        return res

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(threaded=True)


    
    
