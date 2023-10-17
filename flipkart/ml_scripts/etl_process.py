import sqlite3
import numpy as np


def extract_data():
    connection = sqlite3.connect("flipkart.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM datum")
    data = cursor.fetchall()

    connection.close()

    return data

def transform_data(data):
    return np.array(data)

def load_data_for_training(data):
    X, y = data[:, 0].reshape(-1, 1).ravel(), data[:, 1].astype(float).astype(int)
    return X, y

data = extract_data()
data = transform_data(data)
X_train, y_train = load_data_for_training(data)