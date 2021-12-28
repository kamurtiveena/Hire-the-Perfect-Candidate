from flask import Flask, render_template, request
import pickle
import numpy as np
from processing import train_data,test_data,job_req,cleaned_text
from pdfminer import high_level

model = pickle.load(open('tfidf.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/read', methods=['POST'])
def home():
	job_file = cleaned_text(high_level.extract_text("../dataset/"+str(request.form['userfile'])))
	#tf_vector = model.transform(job_file).shape
	return render_template('after.html', data=job_file)
	'''
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)
    '''


if __name__ == "__main__":
    app.run(debug=True)
