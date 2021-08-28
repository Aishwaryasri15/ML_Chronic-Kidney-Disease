import numpy as np
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
model = pickle.load(open('kid1.pkl', 'rb'))
#json_file = open('model.json', 'r')

#loaded_model_json = json_file.read()
#json_file.close()

#loaded_model = model_from_json(loaded_model_json)

#loaded_model.load_weights("model9954.h5")
#print("Loaded model from disk")

@app.route('/')
@app.route('/first') 
def first():
	return render_template('first.html')
@app.route('/index') 
def index():
	return render_template('index.html')    
@app.route('/abstract') 
def abstract():
	return render_template('abstract.html') 
@app.route('/future') 
def future():
	return render_template('future.html')     
 
@app.route('/chart') 
def chart():
	return render_template('chart.html')  
@app.route('/pie') 
def pie():
	return render_template('pie.html')      
@app.route('/upload') 
def upload():
	return render_template('upload.html') 
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)    

 
@app.route('/home')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    '''
    For rendering results on HTML GUI
    '''

    # if("text" == "M"):
    #     text = 0
    # else:
    #     text =1

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
   # prediction = model.predict_proba(final_features)
    prediction =  model.predict(final_features)


    output = prediction[0]
    if output<0.5:
        output1='Normal'
    elif output>0.5:
        output1='Chronic Kidney Disease'


    return render_template('index2.html', prediction_text='The Patient has {}'.format(output1))
    
if __name__ == "__main__":
    app.run(debug=True) 