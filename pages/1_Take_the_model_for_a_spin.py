"""
P001 Take the model for a spin

"""
import streamlit as st
from utils import create_pipe, get_preds


st.title('My Sentiment Analysis Model:')

st.subheader('Drumroll please :drum_with_drumsticks:...')

# Create a pipeline object for inference
pipe = create_pipe()

review = st.text_area(
    label='Write a short review about an eatery '
          'to get a sentiment prediction.',
    placeholder='Enter your review here...'
)

predict_click = st.button('Predict Sentiment :crystal_ball:')

if predict_click:
    sentiment, confidence = get_preds(pipe, review)

    if sentiment == 'POSITIVE':
        st.header(f':thumbsup: {sentiment}')

    if sentiment == 'NEGATIVE':
        st.header(f':thumbsdown: {sentiment}')

    st.write(f'Confidence: {confidence}')
