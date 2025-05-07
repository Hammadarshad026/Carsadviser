import pickle
import pandas as pd

class CarPricePredictor:
    def __init__(self,model_name,manufacturer,registered_in,model_date,fuel_type,transmission,color,body_type,engine_displacement,driven):
        self.model_name=model_name
        self.manufacturer=manufacturer
        self.registered_in=registered_in
        self.model_date=model_date
        self.fuel_type=fuel_type
        self.transmission=transmission
        self.color=color
        self.body_type=body_type
        self.engine_displacement=engine_displacement
        self.driven=driven
        self.model_path ='model/model2.pkl'
        self.model2 = self.get_model()
        self.car_data=self.car_data()
    def car_data(self):
      new_data = {
        'Model Name': [self.model_name],
        'Manufacturer': [self.manufacturer],
        'Registered In': [self.registered_in],
        'Model Date': [int(self.model_date)],
        'Fuel Type': [self.fuel_type],
        'Transmission': [self.transmission],
        'Color': [self.color],
        'Body Type': [self.body_type],
        'Engine Displacement': [int(self.engine_displacement)],
        'Driven': [int(self.driven)] 
        }
      return new_data

    def get_model(self):
        with open(self.model_path, 'rb') as f:
            model2 = pickle.load(f)
        return model2

    def get_price(self):
        if not isinstance(self.car_data, pd.DataFrame):
            new_data = pd.DataFrame(self.car_data)

        
        for col in ['Model Name', 'Manufacturer', 'Registered In', 'Fuel Type', 
                    'Transmission', 'Color', 'Body Type']:
            new_data[col] = new_data[col].astype('category')

        predictions = self.model2.predict(new_data)

        return predictions[0]
    

# car_data = {
#     'Model Name': [Model_name_input],
#     'Manufacturer': [Manufacturer_input],
#     'Registered In': ['punjab'],
#     'Model Date': [2021],
#     'Fuel Type': ['Petrol'],
#     'Transmission': ['Automatic'],
#     'Color': ['Black'],
#     'Body Type': ['Sedan'],
#     'Engine Displacement': [1800],
#     'Driven': [11300]  
# }

# predictor = CarPricePredictor('Corolla GLi 1.3 VVTi','Toyota','punjab',2018,'Petrol','Manual','White','Sedan',1300,160177)
# predicted_price = predictor.get_price()
# print(f'Predicted Price: {predicted_price}')
