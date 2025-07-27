from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load the model and preprocessor
model_path = os.path.join('..', 'artifacts', 'model.pkl')
preprocessor_path = os.path.join('..', 'artifacts', 'preprocesssor.pkl')

model = pickle.load(open(model_path, 'rb'))
preprocessor = pickle.load(open(preprocessor_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        carat = float(request.form['carat'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']

        # Create DataFrame with correct column names
        input_df = pd.DataFrame([{
            'carat': carat,
            'depth': depth,
            'table': table,
            'x': x,
            'y': y,
            'z': z,
            'cut': cut,
            'color': color,
            'clarity': clarity
        }])

        # Apply preprocessing
        transformed_data = preprocessor.transform(input_df)

        # Make prediction
        prediction = model.predict(transformed_data)

        return render_template('index.html', prediction_text=f'Predicted Diamond Price: ${round(prediction[0], 2)}')

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
