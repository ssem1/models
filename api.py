from flask import Flask
from flask_restful import Resource, Api
from regression import(
    forecast
)
from prophet import Predict

app = Flask(__name__)
api = Api(app)

timeframe1 = '5y
length1 = 365
ticker1 = 'AAPL'

class LinearRegression(Resource):
    def get(self):
        pred = forecast(ticker1, length1)
        return {'Prediction': pred}

class Prophet(Resource):
    def get(self):
        fore = forecast(ticker1, timeframe1, length1)
        return {'Forecast': fore}

api.add_resource(LinearRegression, '/')
api.add_resource(Prophet, '/')

if __name__ == '__main__':
    app.run(debug=True)
