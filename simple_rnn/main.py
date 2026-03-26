# Step 1: Import Libraries & load the model
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load the IMDB dataset word index
word_index=imdb.get_word_index()
reverse_word_index={value:key for key, value in word_index.items()}


# Load the pre-trained model with relu activation

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "simple_rnn_imdb.h5")

model = load_model(MODEL_PATH)
model.summary()

# Step 2: Helper function
# Function to decode reviews
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i-3, '?') for i in encoded_review])

# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review=[word_index.get(word,2) + 3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review], maxlen=500) # same length we used while training the model
    return padded_review


# Step 3: Prediction fucntion
## Prediction function

def predict_sentiment(review):
    preprocess_text_input=preprocess_text(review) 
    prediction=model.predict(preprocess_text_input)
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment, prediction[0][0]


# Design streamlit application

import streamlit as st

st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as Positive or Negative')

user_input=st.text_area('Movie Review')

if(st.button('Classify')):
    preprocess_input=preprocess_text(user_input)

    # Make prediction
    prediction=model.predict(preprocess_input)
    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'

    # Display result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review')