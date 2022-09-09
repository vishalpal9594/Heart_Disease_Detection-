import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("heart_disease_data.csv")

x = df.iloc[:,0:13]
y = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,stratify = y ,random_state=2)

model = LogisticRegression(solver='lbfgs', max_iter=1000)
model.fit(x_train.values,y_train)


from tkinter import *

top = Tk()  
top.geometry("400x500")
top.title("welocme to heart disease prediction system")



age = IntVar()
sex = IntVar()
cp = IntVar()
trestbps = IntVar()
chol = IntVar()
fbs = IntVar()
restecg = IntVar()
thalach = IntVar()
exang = IntVar()
oldpeak = IntVar()
slope = IntVar()
ca = IntVar()
thal = IntVar()
ans = StringVar()



def Prediction():
    
    result = model.predict([[age.get(),sex.get(),cp.get(),trestbps.get(),chol.get(),fbs.get(),restecg.get(),thalach.get(),exang.get(),oldpeak.get(),slope.get(),ca.get(),thal.get()]])

    if result[0] == 1:
        final = "You Have Heart Disease"
    else:
        final = "Congratulation You are Fine"


    user_name = Label(top,text = "",textvariable=ans).place(x = 70,y = 440)


    ans.set(final)
        

   
# the label for user_name
user_age = Label(top,text = "Enter Age").place(x = 40,y = 10) 
user_age_input_area = Entry(top,width = 30,textvariable=age).place(x = 130,y = 10) 


user_sex = Label(top,text = "Enter sex").place(x = 40,y = 40)
user_sex_entry_area = Entry(top,width = 30,textvariable=sex).place(x = 130,y = 40)


user_cp = Label(top,text = "Enter chest pain").place(x = 40,y = 70) 
user_cp_input_area = Entry(top,width = 30,textvariable=cp).place(x = 130,y = 70) 


user_trestbps = Label(top,text = "Enter trestbps").place(x = 40,y = 100)
user_trestbps_entry_area = Entry(top,width = 30,textvariable=trestbps).place(x = 130,y = 100) 


user_chol = Label(top,text = "Enter chol").place(x = 40,y = 130) 
user_chol_input_area = Entry(top,width = 30,textvariable=chol).place(x = 130,y = 130) 


user_fbs = Label(top,text = "Enter fbs").place(x = 40,y = 160)
user_fbs_entry_area = Entry(top,width = 30,textvariable=fbs).place(x = 130,y = 160)


user_restecg = Label(top,text = "Enter restecg").place(x = 40,y = 190) 
user_restecg_input_area = Entry(top,width = 30,textvariable=restecg).place(x = 130,y = 190) 


user_thalach = Label(top,text = "Enter thalach").place(x = 40,y = 220)
user_thalach_entry_area = Entry(top,width = 30,textvariable=thalach).place(x = 130,y = 220) 


user_exang = Label(top,text = "Enter exang").place(x = 40,y = 240) 
user_exang_input_area = Entry(top,width = 30,textvariable=exang).place(x = 130,y = 240) 


user_oldpeak = Label(top,text = "Enter oldpeak").place(x = 40,y = 270)
user_oldpeak_entry_area = Entry(top,width = 30,textvariable=oldpeak).place(x = 130,y = 270) 


user_slope = Label(top,text = "Enter slope").place(x = 40,y = 300) 
user_slope_input_area = Entry(top,width = 30,textvariable=slope).place(x = 130,y = 300) 

   
user_ca = Label(top,text = "Enter ca").place(x = 40,y = 330)
user_ca_entry_area = Entry(top,width = 30,textvariable=ca).place(x = 130,y = 330)


user_thal = Label(top,text = "Enter thal").place(x = 40,y = 360) 
user_thal_input_area = Entry(top,width = 30,textvariable=thal).place(x = 130,y = 360) 


Predict_button = Button(top,text = "Predict",command=Prediction).place(x = 90,y =400)




   

     
top.mainloop()
