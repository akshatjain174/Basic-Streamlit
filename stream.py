import streamlit as st
import pandas as pd 
import numpy as np 
import time
import os

st.title("Akshat Jain")
st.header("Testing Streamlit and Its Functions")
st.subheader("Let's Start")
st.write("Streamlit is an open-source framework for building web applications, particularly for data science and machine learning projects. It allows developers to create interactive and visually appealing applications quickly, using only Python. ")
st.markdown("This is a markdown")
st.caption("Captions are generally like this. 😄")


# a=str(st.write(os.getcwd()))
# str(os.getcwd()).replace("\","/"")
st.image("C:/Users/HP/OneDrive/Desktop/Streamlit/hi.jpeg")
st.video("C:/Users/HP/OneDrive/Desktop/Streamlit/Eren-Yeager-Wallpapers-4k.jpg .mp4")
st.audio("d:/SONGS/the-chainsmokers-you-owe-me.mp3")
# st.write(c)
#st.image(c)
# st.image("c:/Users/HP/OneDrive/Desktop/Streamlit/hi.jpeg")
 


st.checkbox("Visited my site?")

st.button('Click button')
st.radio('Pick your city',['Pune','Mumbai','Delhi','Surat','Jabalpur','Indore','Bhopal'])
st.selectbox('Pick your city',['Pune','Mumbai','delhi','surat'])
st.multiselect('Pick favourite sports',['cricket', 'football', 'basketball',"table tennis","hockey"])
st.select_slider('Give a Remark', ['Bad', 'Good',"Average", 'Excellent',"Outstanding"])
st.slider('Your Marks', 0,100)

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("Hi , What's Up?")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
