from flask import Flask
from flask_restful import Resource, Api
from regression import(
    forecast
)

app = Flask(__name__)
api = Api(app)

length1 = int(90)
ticker1 = "WIKI/GOOG"
class LinearRegression(Resource):
    def get(self):
        conf = forecast(ticker1, length1)
        return {'confidence': conf}

api.add_resource(LinearRegression, '/')

if __name__ == '__main__':
    app.run(debug=True)
