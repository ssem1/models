from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
from regression import(
    forecast
)
from prophet import Predict

app = Flask(__name__)
api = Api(app)

timeframe1 = '5y'
length1 = 365
ticker1 = 'AAPL'

class LinearRegression(Resource):
    @app.route('/')
    def get(self):
        pred = forecast(ticker1, length1)
        return {'Prediction': pred}

class Prophet(Resource):
    def get(self):
        args = request.args
        #parser = reqparse.RequestParser()
        ticker = request.args.get('ticker', default = 'AAPL', type = str)
        timeframe = request.args.get('timeframe', default = '1y', type = str)
        length = request.args.get('length',default = 1, type = int)
        #parser.add_argument('ticker', type=str)
        #parser.add_argument('timeframe', type=str)
        #parser.add_argument('length', type=int)
        #parser.parse_args()
        fore = Predict(ticker, timeframe, length)
        return {'Forecast': fore}

api.add_resource(LinearRegression, '/LinearRegression')
api.add_resource(Prophet, '/Prophet')

if __name__ == '__main__':
    app.run(debug=True)
