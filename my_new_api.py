from flask import Flask, request, jsonify
import joblib
import pandas as pd
app = Flask(__name__)

# Creating API routing call
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON Request
    feat_data=request.json
    # Convert JSON request to Pandas DataFrame
    df=pd.DataFrame(feat_data)
    # Match Column Na,es
    df=df.reindex(columns=column_name)
    # Get prediction
    prediction=list(model.predict(df))
    # Return JSON version of Prediction
    return jsonify({'prediction': str(prediction)})


if __name__ == '__main__':
    # LOADS MODEL AND FEATURE COLUMNS
    model=joblib.load("toxicity_classifier.pkl")
    column_name=joblib.load("column_names.pkl")

    app.run(debug=True)