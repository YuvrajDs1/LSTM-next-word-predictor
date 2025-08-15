import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import pad_sequences

# load model
model = load_model('next_word_lstm.h5')
