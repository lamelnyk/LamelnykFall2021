from flask import Flask, request, jsonify 
from blood_calculator import hdl_analysis

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"

@app.route("/info", methods=["GET"])
def info():
    my_output = "This server is for BME 547"
    return my_output

@app.route("/hdl/<hdl_value>", methods=["GET"])
def hdl_analysis_server(hdl_value):
    """
    Input should like {"hdl": 50, "patient_id": 200}
    return: 
    """
    #in_data = request.get_json()
    #hdl_value = in_data["hdl"]
    hdl_value = int(hdl_value)
    print("The hdl_value is {}" .format(hdl_value))
    answer = hdl_analysis(hdl_value)
    return jsonify(hdl_value) , 201


@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello, {}". format(input_name)


if __name__ == '__main__':
    app.run()

"""
www.google.com/maps
"""