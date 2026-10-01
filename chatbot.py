import random
import json
import pickle
import numpy as np
import nltk
from tensorflow.keras.models import load_model
from nltk.stem import WordNetLemmatizer
from database import log_chat, get_courses

lemmatizer = WordNetLemmatizer()

model = load_model("chatbot_model.h5")
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)

def predict_class(sentence):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]

def get_response(msg):
    msg_lower = msg.lower()
    if "course" in msg_lower or "program" in msg_lower:
        courses = get_courses()
        response = "We offer the following courses:\n"
        for c in courses:
            response += f"- {c[1]} ({c[2]}) Fees: {c[3]}\n"
        log_chat(msg, response)
        return response
    if "admission" in msg_lower or "apply" in msg_lower:
        response = "Admissions are open! Fill the form online or visit the college office."
        log_chat(msg, response)
        return response
    if "fees" in msg_lower:
        courses = get_courses()
        response = "Course Fees:\n"
        for c in courses:
            response += f"- {c[1]}: {c[3]}\n"
        log_chat(msg, response)
        return response
    if "contact" in msg_lower or "phone" in msg_lower or "email" in msg_lower:
        response = "Contact: info@abccollege.edu.in | +91-1234567890"
        log_chat(msg, response)
        return response

    ints = predict_class(msg)
    if len(ints) == 0:
        response = "Sorry, I didn't understand. Can you rephrase?"
        log_chat(msg, response)
        return response

    tag = ints[0]['intent']
    list_of_responses = [i['responses'] for i in intents['intents'] if i['tag']==tag][0]
    response = random.choice(list_of_responses)
    log_chat(msg, response)
    return response