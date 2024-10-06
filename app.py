from flask import Flask, request, render_template
import numpy as np
import scipy.io as sio

# Load model weights and biases
model_data = sio.loadmat('model_weights.mat')
weights = model_data['weights'][0]  # Assuming weights are in a suitable shape
biases = model_data['biases'][0]      # Adjust as needed

app = Flask(__name__)

def predict_price(inputs):
    inputs = np.array(inputs).reshape(1, -1)
    # Simple linear regression prediction (for example)
    prediction = np.dot(inputs, weights) + biases
    return prediction.item()  # Use item() to convert to a scalar

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            inputs = [
                int(request.form['size']),
                int(request.form['rooms']),
                int(request.form['age']),
                int(request.form['garage_size']),
                int(request.form['location_quality'])
            ]
            prediction = predict_price(inputs)
            return render_template('home.html', prediction=prediction)
        except ValueError:
            return render_template('home.html', prediction="Invalid input. Please enter numerical values.")
    return render_template('home.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
