
from flask import Flask, render_template, request, jsonify
from advisor import get_car_advice
from model.pridicter import CarPricePredictor

app = Flask(__name__)

# Price prediction helper
def get_car_class(Model_Name, Manufacturer, Registered_In, Model_Date,
                  Fuel_Type, Transmission, Color, Body_Type, Engine_Displacement, Driven):
    predictor = CarPricePredictor(Model_Name, Manufacturer, Registered_In, Model_Date,
                                  Fuel_Type, Transmission, Color, Body_Type,
                                  Engine_Displacement, Driven)
    return predictor.get_price()


# Home Page
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')


# Car Price Prediction Page
@app.route('/price_pridicter', methods=['GET', 'POST'])
def price_pridicter():
    car_price = None
    if request.method == 'POST':
        Model_Name = request.form.get('Model_Name')
        Manufacturer = request.form.get('Manufacturer')
        Registered_In = request.form.get('Registered_In')
        Model_Date = request.form.get('Model_Date')
        Fuel_Type = request.form.get('Fuel_Type')
        Transmission = request.form.get('Transmission')
        Color = request.form.get('Color')
        Body_Type = request.form.get('Body_Type')
        Engine_Displacement = request.form.get('Engine_Displacement')
        Driven = request.form.get('Driven')

        car_price = get_car_class(Model_Name, Manufacturer, Registered_In, Model_Date,
                                  Fuel_Type, Transmission, Color, Body_Type,
                                  Engine_Displacement, Driven)

    return render_template('price_pridicter.html', car_price=car_price)


# Chatbot AJAX Endpoint
@app.route('/ask_bot', methods=['POST'])
def ask_bot():
    user_question = request.form.get('question')
    bot_answer = get_car_advice(user_question)
    return jsonify({'answer': bot_answer})


if __name__ == "__main__":
    app.run(debug=True)
