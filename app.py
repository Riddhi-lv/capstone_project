import streamlit as st
import joblib
import pandas as pd 
import numpy as np


pipeline=joblib.load("model_pipeline1.joblib")

def main():
    st.title("Drilling Optimization")     
    
    
    dict={}
    result=[]
    drill_speed=st.number_input("drill speed", step=0.1)
    fluid_vol=st.number_input("fluid vol", step=0.1)
    bit_type=st.selectbox("Select an option", ["Roller Cone", "PDC", "Button"])
    formation_type=st.selectbox("Select an option", ["Sandstone", "Limestone", "Shale"])

    dict1={
    'Drill_Speed':drill_speed,
    'Bit_Type':str(bit_type),
    'Drilling_Depth':2518.684009,
    'Formation_Type':str(formation_type),
    'Formation_Density':2.027941032,
    'Bit_Wear':6,
    'Temperature':14.91703737,
    'Pressure':110.871765,
    'Fluid_Volume':fluid_vol,
    'binned_Environmental_Imapact':"Good"}    
    
    user_df=pd.DataFrame(dict1,index=['row1'])
    # pipeline=joblib.load("model_pipeline1.joblib")

       
    if st.button("Predict"):
        st.write(user_df)
        result=pipeline.predict(user_df)
        st.write(f"Predicted Operation Time : {result[:,0][0]} hrs")
        st.write(f"Predicted Cost per Operation is: Rs.{result[:,1][0]}")
        st.write(f"Predicted Resource Yield: {result[:,2][0]}")
        st.write(f"Predicted Emission Cost: {result[:,3][0]}")
    
if __name__=="__main__":
    main()

