from flask import Flask, request, jsonify
import util
from flask_cors import CORS
import streamlit as st

app = Flask(__name__)
CORS(app)
@app.route('/hello')
def hello():
    return 'hi'
@app.route('/get_location_name')
def get_location_name():
    response=jsonify({
        'location':util.get_locations_name()
    })
    return response  # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    sqft=float(request.form['total_sqft'])
    location =request.form['location']
    bath = float(request.form['bath'])
    bhk = int(request.form['bhk'])
    response=jsonify({
        'estimated_price':round(util.predict_price(location, sqft, bath, bhk),2)
    })
    print('predict price ',util.predict_price(location, sqft, bath, bhk))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.write(""""
    My first app """)
    print('Starting app')
    app.run()