#Importing essential libraries.
import nltk 
import random
import json
import pickle
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import load_model
nltk.download('wordnet')
#The chatbot is going to use a JSON file to learn how to answer different types of similar questions.
#In the intents.JSON file we can see how different similar questions have same answer.
print(nltk.__version__)
print(np.__version__)
print(tf.__version__)
#Lemmatizer init & loading intents, words, classes and the trained model we have saved.
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('app\model\intents.json').read())
words = pickle.load(open('app\model\words.pkl', 'rb'))
classes = pickle.load(open('app\model\classes.pkl', 'rb'))
model = load_model('app\model\chatbot_model.h5')


#This function cleans up each sentence given to it following these steps:
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence) #Tokenizes the input sentence into a list of words using NLTK.
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words] #Lemmatizes each word in the list using the WordNet lemmatizer.
    return sentence_words #Returns the list of lemmatized words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence) #Calls clean_up_sentence to get a list of lemmatized words from the input sentence.
    bag = [0] * len(words)
    for w in sentence_words: #Creates a bag-of-words representation of the sentence, where each element in the bag is 1 if the word is present in the sentence, and 0 otherwise.
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag) #Returns a NumPy array representing the bag-of-words.


#This function is tricker to understand but the comments make each step straightforward.
def predict_class(sentence):
    #Get the bag-of-words representation of the input sentence.
    bow = bag_of_words(sentence)
    #Use the pre-trained model to predict probabilities for each class.
    res = model.predict(np.array([bow]))[0]
    #Set a threshold to filter results based on probability.
    ERROR_THRESHOLD = 0.25
    #Create a list of intent and probability pairs above the threshold.
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    #Sort the results by probability in descending order.
    results.sort(key=lambda x: x[1], reverse=True)
    #Create a list of dictionaries with intent and probability information.
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    #Return the list of predicted intents and their probabilities.
    return return_list
    

#This function is used so that the bot answers user's messages.
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
# Function searches the intents JSON for the corresponding tag and randomly selects a response from the available responses for that intent.    
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result #Returns the selected response.


#Chat with Syby!
print("GO! Bot is running!")
while True:
    message=input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
