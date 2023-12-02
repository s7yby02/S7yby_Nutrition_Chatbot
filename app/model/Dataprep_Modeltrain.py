#Importing essential libraries.
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

#You may also need to download punkt and wordnet from nltk using: nltk.download('punkt') & nltk.download('wordnet').


#In this section we're going to prepare the training data using basic NLP techniques and library: nltk.
#Lemmatizer initialization & Loading the JSON file.
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

#Lists to store words, classes and documents and the letters to ignore while storing ...
words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',']

# Tokenize each pattern into words, add them to the 'words' list.
# Create a tuple (wordList, intent['tag']) and append it to 'documents'.
# If the intent tag is not in 'classes', add it to the 'classes' list.
for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#Cleaning from ignore letters, this line removes duplicates and sorts the words.
words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))

#This line removes duplicate classes and sorts them.
classes = sorted(set(classes))

#The processed words and classes are saved as pickled files ('words.pkl' and 'classes.pkl').
#Pickling is a way to serialize Python objects into a format that can be saved to a file.
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))


# Iterate through documents, creating a "bag of words" representation for each pattern.
# For each word in 'words', append 1 to the bag if the word is present in the pattern, and 0 otherwise.
# 'outputRow' is a one-hot encoded representation of the intent class, appended to the bag.
# The resulting data is added to the 'training' list.
training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)

    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

#The data is ready!
random.shuffle(training)
training = np.array(training)

trainX = training[:, :len(words)]
trainY = training[:, len(words):]


#Model training.
#The model is a feed forward neural network, with two hidden layer and a softmax activation function on the output layer.
#The use of softmax is for the sake of giving a probability to each answer given the question.
#Dropout layers are used to create a model capable of generalizing to all possible scenarios.
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation = 'tanh'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(64, activation = 'tanh'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
model.fit(trainX, trainY, epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5')