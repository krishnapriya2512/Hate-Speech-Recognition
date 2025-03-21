# Hate-Speech-Recognition
Hate Speech Recognition using Jupyter Notebook, Flask and SQLite3

**Aim:** Deploy a NLP program on a (simulated) Web page.

### Steps: 
1. **Intialization:** Importing train dataset and doing Exploratory Data Analysis on the dataset using basic commands.
2. **Data cleaning:** Building a preprocessor to remove user handles, punctuations, greek symbols and stopwords. Also for better predictability using tokenization and lemmtizer for cleaning. 
3. **Model Training:** Splitting of dataset into train test split and using logistic Regression, Random Classifier and SDGClassifier for model prediction.
4. **Prediction:** Predicting the model trained on a test dataset.
5. **Serializing and deserializing of objects:** using pickle to serialize stopwords, countvectorizer and classifier and Deserializing it to check if the objects are working fine.
6. **Setting up SQLite Connection**: Setting up an SQL connectio to store the records and use them to simultaneously train the model.


**Note:** I used Visual studio code for running the Flask program. 
The file folder sequence for Flask process should be as below
**create a main folder HatespeechDetection -** pkl_objects and vectorizer.py will be created automatically when the serialiser code is runned. We need to create two folders - static and templates. A python files (used Visual studio) main.py. 
- In templates folder- -formhelpers, results,reviewform and thanks should be placed.
- in static folder - style.css should be placed.

** Feel free to make changes accordingly **


