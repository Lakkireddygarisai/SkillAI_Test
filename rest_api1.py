import csv
from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint to get the city with the highest population of males and the female population in that city
@app.route('/highest_population_male_city', methods=['GET'])
def get_highest_population_male_city():
    with open('Book1.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    max_male_population = 0
    max_male_city = None
    female_population = 0
    
    for row in data:
        if row['Gender'] == 'Male':
            population = int(row['Population'])
            if population > max_male_population:
                max_male_population = population
                max_male_city = row['City']
        elif row['Gender'] == 'Female' and row['City'] == max_male_city:
            female_population += int(row['Population'])
    
    result = {
        'city': max_male_city,
        'male_population': max_male_population,
        'female_population': female_population
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()
