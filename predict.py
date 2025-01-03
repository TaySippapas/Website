from flask import render_template,Blueprint,request,jsonify
from joblib import load
import pandas as pd
predict_bp=Blueprint('predict',__name__)
model = load('models/model.joblib')
def preprocessed_data(data):
    if data["Promotion"]=="Yes":
        data["Promotion"]=1
    else:
        data["Promotion"]=0
    if data["SpecialEvent"]=="Yes":
        data["SpecialEvent"]=1
    else:
        data["SpecialEvent"]=0
    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=['Season', 'Weather'])
    day_order = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    time_order = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
    df['DayOfWeek'] = df['DayOfWeek'].map(day_order)
    df['TimeSlot'] = df['TimeSlot'].map(time_order)
    column_list = [
    'DayOfWeek',
    'TimeSlot',
    'SpecialEvent',
    'Promotion',
    'Season_Cool',
    'Season_Dry',
    'Season_Rainy',
    'Weather_Clear',
    'Weather_Cloudy',
    'Weather_Rainy'
    ]
    df=df.reindex(columns=column_list,fill_value=0)
    return df
@predict_bp.route('/predict', methods=['GET'])
def predict_html():
    return render_template('predict.html')
@predict_bp.route('/predict', methods=['POST'])
def predict():
    data=request.get_json()
    preprocessed_df = preprocessed_data(data)
    prediction=model.predict(preprocessed_df)
    return jsonify({'Prediction': prediction.tolist()})
    