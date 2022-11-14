# coding: utf-8

from distutils.log import debug
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from flask import Flask, request, render_template
import pickle
import re
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__,template_folder='template')

df_1=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

@app.route("/")
def loadPage():
	return render_template('homepage.html')


@app.route("/", methods=['GET','POST'])
def predict():
    
    '''
    Contract
    MonthlyCharges
    TotalCharges
    tenure

    '''
    #Reading Form Input
      
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']


    if request.form.get('SUBMIT') == 'SUBMIT':
      
    #Validate Contract Input

     if inputQuery1 =="":
         query1Error ="please select the contract period"  
     else:
         query1Error =""

    #Validate MonthlyCharges Input

     if inputQuery2 =="":
         query2Error ="This field is required"  
     elif not re.match("^[0-9 ]+$", inputQuery2):
         query2Error ="This field takes only numbers as Input"
     elif  int(inputQuery2)<18 or int(inputQuery2)>119:
         query2Error ="The input is not in the range[18-119]"
     else:
         query2Error =""

    #Validate TotalCharges Input

     if inputQuery3 =="":
         query3Error ="This field is required"  
     elif not re.match("^[0-9 ]+$", inputQuery3):
         query3Error ="This field takes only numbers as Input"
     elif  int(inputQuery3)<18 or int(inputQuery3)>8684:
         query3Error ="The input is not in the range[18-8684]"
     else:
         query3Error =""


    #Validate Tenure Input

     if inputQuery4 =="":
         query4Error ="please select the tenure period"  
     else:
         query4Error =""
    

     if query1Error == "" and query2Error =="" and query3Error == "" and query4Error =="":

       model = pickle.load(open("churn.pkl", "rb"))
    
       data = [[int(inputQuery1),int(inputQuery2),int(inputQuery3),int(inputQuery4)]]
          
       churn = model.predict(data)
   
    
       if churn==1:
          o1 = "This customer is likely to be churned!!"
        
       else:
          o1 = "This customer is likely to continue!!"
       

     else:
         o1 = ""

     return render_template('homepage.html', output1=o1,  
                           query1 = inputQuery1,
                           query2 = inputQuery2,
                           query3 = inputQuery3,
                           query4 = inputQuery4,
                           query1Error=query1Error,
                           query2Error=query2Error,
                           query3Error=query3Error,
                           query4Error=query4Error,
                           )
  
    else :
     o1=""
     inputQuery1=""
     inputQuery2=""
     inputQuery3=""
     inputQuery4=""  
     query1Error=""
     query2Error=""
     query3Error=""
     query4Error=""
  
     return render_template('homepage.html', output1=o1,  
                           query1 = inputQuery1,
                           query2 = inputQuery2,
                           query3 = inputQuery3,
                           query4 = inputQuery4,
                           query1Error=query1Error,
                           query2Error=query2Error,
                           query3Error=query3Error,
                           query4Error=query4Error,
                           )

     

if __name__ == '__main__':              
   app.run(debug=True)
