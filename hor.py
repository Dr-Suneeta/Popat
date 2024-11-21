# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:02:13 2024

@author: Admin
"""

import pandas as pd
import numpy as np
import pickle as pickle
import streamlit as st
from datetime import datetime

file1=open('Horoscope.pkl','rb')
model=pickle.load(file1)
file1.close()

st.title("Popat says")

Name=st.text_input("Enter your name")

Gender=st.selectbox("Gender",['Male','Female'])

Date_input=st.text_input("Enter your date of birth in yyyy-mm-dd format")

if Date_input:
    try:
        valid_date=datetime.strptime(Date_input,"%Y-%m-%d").date()
        st.success(f"You were born on{valid_date}")
    except ValueError:
        st.error("Invalid birth date.Read the instruction again")
        
Time_input=st.text_input("Enter time of your birth  in 00:00:00 format")

if Time_input:
    try:
        valid_time=datetime.strptime(Time_input,"%H:%M:%S").time()
        st.success(f"You were born on{valid_time}")
    except ValueError:
        st.error("Invalid birth time.Read the instructions again")
        
        
if st.button("Panditji's Popat says"):
    
    Sex=1 if Gender=='Female' else 0
    
    Month=pd.Timestamp(Date_input).month
    
    Day=pd.Timestamp(Date_input).day
    
    Num=((pd.to_datetime(Time_input,format='%H:%M:%S')-pd.to_datetime("00:00:00",format="%H:%M:%S")).total_seconds())/60
    
         
    query=np.array([Sex,Month,Day,Num]).reshape(1,-1)   
    
    try:
        prediction=model.predict(query)[0]  
    
        st.write(" So the Popat says " +
             str(prediction))
    except ValueError:
        st.error("Oops!Something went wrong! Are you sure you have entered the right information?")        
        
if st.button("Click if you agree with Popat"):     
    st.balloons()
    st.success("Thank you")



   
        
        
        
        
