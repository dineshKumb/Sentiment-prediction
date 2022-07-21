import numpy as np
import pickle
import streamlit as st
import sklearn
# from flask import Flask, request, render_template



# app=Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template()


st.title("Sentiment Prediction")

st.header('Select the category from the dropdown below')

choice=st.selectbox("Choose a category", ("Books","DVD","Electronics","Kitchen"))
st.write(choice)

if choice=="Books":
    filename="book_model.pkl"
    loaded_model = pickle.load(open(filename, 'rb'))
    user_input = st.text_input("Write your review here.....")
    if st.button('Check sentiment'):
        if (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])>50:
            st.write("The given review is Positive and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0]))
        else:
            st.write("The given review is Negative and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,0][0]))
        # "%2.1f%% Confidence score" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])

elif choice=="DVD":
    filename="dvd_model.pkl"
    loaded_model = pickle.load(open(filename, 'rb'))
    user_input = st.text_input("Write your review here.....")
    if st.button('Check sentiment'):
        if (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])>50:
            st.write("The given review is Positive and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0]))
        else:
            st.write("The given review is Negative and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,0][0]))
        # "%2.1f%% Confidence score" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])

elif choice=="Electronics":
    filename="electronic_model.pkl"
    loaded_model = pickle.load(open(filename, 'rb'))
    user_input = st.text_input("Write your review here.....")
    if st.button('Check sentiment'):
        if (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])>50:
            st.write("The given review is Positive and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0]))
        else:
            st.write("The given review is Negative and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,0][0]))
       
        #"%2.1f%% Confidence score" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])

elif choice=="Kitchen":
    filename="kitchen_model.pkl"
    loaded_model = pickle.load(open(filename, 'rb'))
    user_input = st.text_input("Write your review here.....")
    if st.button('Check sentiment'):
        if (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])>50:
            st.write("The given review is Positive and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0]))
        else:
            st.write("The given review is Negative and the confidence score is %2.1f%%" % (100 * loaded_model.predict_proba([user_input])[0:1][:,0][0]))     
       # "%2.1f%% Confidence score" % (100 * loaded_model.predict_proba([user_input])[0:1][:,1][0])
