🎓 College Enquiry Chatbot

A web-based College Enquiry Chatbot developed using Python and
Flask to provide students with quick and automated answers to common
college-related queries.

The application provides a chatbot interface along with student
registration/login, course information, chat history, and an admin panel
for managing college information.

📌 Project Overview

Students often need information about courses, admissions, departments,
facilities, and other college-related activities. Finding this
information manually can be time-consuming.

The College Enquiry Chatbot provides an automated solution where
users can ask questions through a web interface and receive relevant
responses.

The chatbot uses Natural Language Processing (NLP) and an
intent-based machine-learning approach to classify user queries and
return appropriate responses.

✨ Features

👨‍🎓 Student Features

Student registration and login

Interactive chatbot

Ask college-related questions

Automated responses

Chat history

Course information

User-friendly interface

👨‍💼 Admin Features

Admin login

Admin dashboard

Manage college information

Add and manage courses

Manage chatbot-related information

🤖 Chatbot Features

Natural Language Processing

Intent-based query classification

Machine-learning model

Automated responses

College-specific enquiries

🛠️ Technologies Used

Technology         Purpose

Python             Backend programming
Flask              Web framework
HTML5              Web page structure
CSS3               Interface styling
JavaScript         Frontend interaction
SQLite             Database
NLTK               Natural Language Processing
TensorFlow/Keras   Machine Learning
Git & GitHub       Version control

📂 Project Structure

College-enquiry-chatbot/
│
├── app.py
├── chatbot.py
├── database.py
├── db.py
├── train.py
├── intents.json
├── college.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── Admin.html
│
├── static/
│   ├── style.css
│   ├── image.png
│   ├── chatcol.jpg
│   └── Campus.jpg
│
├── .gitignore
├── README.md
└── requirements.txt

Generated files such as .venv, __pycache__, .pkl, and .h5 are
excluded from Git tracking using .gitignore.

⚙️ How to Run

1. Clone the repository

git clone https://github.com/Potphalev20/College-enquiry-chatbot.git

2. Open the project folder

cd College-enquiry-chatbot

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment on Windows

.venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

python app.py

7. Open the application

Open your browser and visit:

http://127.0.0.1:5000

🧠 How the Chatbot Works

User Query
    ↓
Text Preprocessing
    ↓
Tokenization
    ↓
Intent Classification
    ↓
Trained Model
    ↓
Identify User Intent
    ↓
Generate Response
    ↓
Display Response

For example:

User: What courses are available?
             ↓
      Course-related intent
             ↓
      Chatbot generates response

🗄️ Database

The application uses SQLite to store application data such as:

User accounts

Course details

Chat history

Admin information

College information

🎯 Objectives

Provide automated college enquiry services.

Reduce the time required to find college information.

Provide quick access to common college information.

Apply NLP and machine learning in a practical project.

Provide a simple and user-friendly chatbot.

Provide an admin interface for managing information.

🚀 Future Enhancements

Possible future improvements include:

Voice-based chatbot

Multilingual support

AI/LLM-based responses

WhatsApp chatbot integration

Cloud deployment

Mobile application

Advanced admin analytics

RAG-based knowledge retrieval

Integration with the official college website

👩‍💻 Developer

Vaishnavi Potphale

MCA Student | Python | Flask | Web Development | Machine Learning

📄 License

This project is developed for educational and academic purposes.

⭐ Acknowledgement

This project was developed as an academic project to demonstrate the
practical application of Python, Flask, Natural Language Processing,
Machine Learning, databases, and web development.
