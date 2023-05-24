from flask import Flask, Methods, jsonify
import pandas as pd

from pands1 import get_highest_male_population

df = pd.read_csv('Book1.csv')
a =get_highest_male_population(df)

b=a['City']




app = Flask(__name__)

@app.route('/api/population', Methods ==['Get'] )

def simple_endpoint():
    data = {"mesage": get_highest_male_population()}

    return jsonify(data)


if __name__ == "__main()__":
    simple_endpoint()'''

