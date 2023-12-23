# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Lakshmi/Downloads/credicardfraud/trained_model.sav','rb'))
input_data =(12714,1.085132	,-0.284200,	1.227259,	0.994783,	-0.971597,	0.104091,	-0.842026	,0.172350	,2.309517	,-0.565225,	0.288409,	-2.856187,	0.321535,	1.446209,	0.316601,	0.076154,	0.759545,	0.040792	,-0.824541,	-0.187177,	-0.020988,	0.235961,	-0.030041,	0.044704,	0.194784,	0.458817,	-0.012930,	0.018620,	43.00	)

def predictions(input):
    if isinstance(input, str):
        # Convert the string to a list of numeric values
        input = input.split(',')
        input = [float(val.strip()) for val in input]
    elif isinstance(input, bytes):
        # Decode the bytes into a string and then to a list of numeric values
        input = input.decode('utf-8')
        input = input.split(',')
        input = [float(val.strip()) for val in input]
    else:
        return 'Invalid input type. Please provide a string or bytes.'

    array = np.asarray(input)
    reshaped = array.reshape(1,-1)
    new_pred = loaded_model.predict(reshaped)
    if(new_pred==0.0):
       return 'legit transaction'
    else:
        return 'fraud transaction'
        
def main():
    st.title('Credit card fraud system')
    input = st.text_area('Enter input data (comma-separated):', value="")
    preds = ''
    if st.button('transaction state:'):
        preds = predictions(input)
        st.success(preds)
    
    
if __name__ == '__main__':
    main()
