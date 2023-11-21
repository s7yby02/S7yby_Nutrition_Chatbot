#Importing essential libraries
import nltk 
import random
import json
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow. keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model

#The chatbot is going to use a JSON file to learn how to answer different types of similar questions
#In the intents.JSON file we can see how different similar questions have same answer

