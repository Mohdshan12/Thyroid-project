import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import pickle

filename = "model.pkl"
classifier = pickle.load(open(filename, 'rb'))


st.markdown("""
<style>
body {
 background: #ff0099; 
 background: -webkit-linear-gradient(to right, #ff0099, #493240); 
 background: linear-gradient(to right, #ff0099, #493240); 
}
</style>
   """, unsafe_allow_html=True)

nav = st.sidebar.radio("Navigation",["Home","About me"])
if nav=="Home":
    st.title("THYROID DETECTION USING MACHINE LEARNING")
    html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">THYROID DETECTION ML APP </h2>
</div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.number_input("Enter you Age",1,100,step = 1)
    gender = st.selectbox('Select your Gender:',(" ","Male","Female"))
    st.write('Gender:',gender)
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    TSH = st.number_input("Enter thyroid-stimulating hormone (TSH) ",0.5,5.0,step = 0.25)
    T4U = st.number_input("Enter T4U ",0.25,1.55,step = 0.10)
    FTI = st.number_input("Enter FTI ",2.00,204.00,step = 1.0)
    TT4= st.number_input("Enter TT4 ",2.00,211.00,step = 1.0)
    T3 = st.number_input("Enter T3 ",0.50,4.20,step = 0.10)
    thyroid_surgery  = st.selectbox('thyroid surgery :',(" ","True","False"))
    st.write('You Select:',thyroid_surgery)
    if thyroid_surgery == "True":
        thyroid_surgery = 1
    else:
        thyroid_surgery = 0

    query_hypothyroid = st.selectbox('query_hypothyroid:',(" ","True","False"))
    st.write('You Select:',query_hypothyroid)
    
    if  query_hypothyroid == "True":
        query_hypothyroid = 1
    else:
        query_hypothyroid = 0

    on_thyroxine = st.selectbox('on_thyroxine:',(" ","True","False"))
    st.write('You Select:',on_thyroxine)
    if on_thyroxine == "True":
        on_thyroxine = 1
    else:
        on_thyroxine = 0

    data = np.array([[TSH,  FTI, TT4, T3, T4U, age, on_thyroxine, gender, query_hypothyroid, thyroid_surgery]])
    dic = {0:'negative',1:'compensated_hypothyroid',2:'primary_hypothyroid',3:'secondary_hypothyroid'}
    my_prediction = classifier.predict(data)
    if st.button("Predict"):
        st.write("Your Report : ")
        st.balloons()
        st.success(dic[my_prediction[0]])
    

    
if nav == "About me":
    html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">About me </h2>
</div>
"""
    st.markdown(html_temp,unsafe_allow_html=True)
    t = st.write(""" Hii , My name is Shaan and I am an undergraduate engineering
                     scholar who's a curious guy and loves coding specifically in Python
                     language along with genuine interest in Machine Learning and
                     Artificial Intelligence. I am a self learned enthusiastic coder
                     who is fond of completing challenging projects and thus I have
                     completed few major and minor projects using machine learning
                     framework along with dedication , hardwork and practical approach 
                     towards my learning. I am an interesting guy who loves to socialize 
                     and make new friends and follows practical approach to solve 
                     difficulties in life.
                     thank You""")
    #st.write("check out this [Linkdin](https://www.linkedin.com/in/mohd-shan/)")
    #st.write("check out this [Github](https://github.com/Mohdshan12)")
    st.markdown('''
    <a href="https://www.linkedin.com/in/mohd-shan/">
        <img src="https://img.flaticon.com/icons/png/512/174/174857.png?size=1200x630f&pad=10,10,10,10&ext=png&bg=FFFFFFFF" width="50" height="25"/>
    </a>   
    <a href="https://github.com/Mohdshan12">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="45" height="40"/>
    </a>
    
    ''',
    unsafe_allow_html=True
)

    
