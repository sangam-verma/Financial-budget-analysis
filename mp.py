from flask import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result/',methods =["GET", "POST"])
def data():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       year = request.form.get("year")
       data = pd.read_csv(year+".csv")
       
       df = pd.DataFrame(data)
       X = list(df.iloc[:, 0])
       Y = list(df.iloc[:, 1])
       l=[]
       y=Y[-1]
       for i in range(len(X)-1):
           s=(Y[i]/y)*100
           l.append(s)

       plt.bar(X[:-1],l)
       plt.title("Budget analysis of "+year+"\nGrand Total: "+str(y))
       plt.xlabel("Department /Ministry")
       plt.ylabel("Fund allotted(in ₹crores)")
       plt.xticks(range(len(X)),X,rotation='vertical')
       plt.show()

       plt.pie(l)
       plt.title("Budget analysis of "+year+"\nGrand Total: "+str(y))
       labels = [f'{l}, {s:0.1f}%' for l, s in zip(X, l)]
       plt.legend(labels=labels, fontsize=5, loc='lower left', 
           bbox_to_anchor=(1,0.5), ncol=2)
       plt.show() 

       return render_template('index.html')
       

if __name__=="__main__":
    app.run()