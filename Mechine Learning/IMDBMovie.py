# IMDB movie dataset is used to build one model to complete classification between description and trpes.

import kagglehub
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Download latest version
# path = kagglehub.dataset_download("adilshamim8/nlp-task")

# Load dataset
data_path =''
movies_genres = pd.read_csv(data_path + '/movies_genres.csv')
movies_overview = pd.read_csv(data_path + '/movies_overview.csv')

# Preprocess the data
movies_overview['overview'] = movies_overview['overview'].str.lower()
movies_overview['overview'] = movies_overview['overview'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

# Convert genre_ids to multi-label format
mlb = MultiLabelBinarizer()
y = mlb.fit_transform(movies_overview['genre_ids'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(movies_overview['overview'], y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)


# Train a RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train_vec, y_train)

# Predict on the test set
y_pred = clf.predict(X_test_vec)

# Evaluate the model
print(classification_report(y_test, y_pred, target_names=mlb.classes_))
