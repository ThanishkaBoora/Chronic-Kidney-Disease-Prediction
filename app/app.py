import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/thani/OneDrive/Desktop/MP/trained_model.sav', 'rb'))

# Creating function for prediction
def ckd_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)

    # Impute missing values with the mean of the non-missing values
    input_data_as_numpy_array = np.nan_to_num(input_data_as_numpy_array, nan=np.nanmean(input_data_as_numpy_array))

    # Reshape the numpy array to match the expected shape for the model prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Assuming you have already defined and trained your model
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person does not have CKD disease."
    else:
        return "The person has CKD disease."

def main():
    st.title("CKD prediction web app")

    # Create a grid layout with 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        bp = st.text_input("BP")
    with col3:
        al = st.text_input("al")

    with col1:
        su = st.text_input("su")
    with col2:
        rbc = st.text_input("rbc")
    with col3:
        pc = st.text_input("pc")

    with col1:
        pcc = st.text_input("pcc")
    with col2:
        ba = st.text_input("ba")
    with col3:
        bgr = st.text_input("bgr")

    with col1:
        bu = st.text_input("bu")
    with col2:
        sc = st.text_input("sc")
    with col3:
        pot = st.text_input("pot")

    with col1:
        wc = st.text_input("wc")
    with col2:
        htn = st.text_input("htn")
    with col3:
        dm = st.text_input("dm")

    with col1:
        cad = st.text_input("cad")
    with col2:
        pe = st.text_input("pe")
    with col3:
        ane = st.text_input("ane")
        
    #code for prediction
    diagnosis= ''
        
    #creating button for prediction
    if st.button('CKD Test Results'):
        diagnosis= ckd_prediction([age,bp,al,su,rbc,pc,pcc,ba,bgr,bu,sc,pot,wc,htn,dm,cad,pe,ane])
        
    st.success(diagnosis)
        
if __name__== '__main__':
    main()
