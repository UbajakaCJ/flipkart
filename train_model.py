from sklearn.feature_extraction.text import HashingVectorizer
from etl_process import load_data_for_training, data
from sklearn.svm import LinearSVC
import joblib

def train_model(X, y):

    transformer = HashingVectorizer(stop_words='english')
    X = transformer.fit_transform(list(X))
    svm=LinearSVC(dual=True)
    svm.fit(X, y)
    joblib.dump(svm, "model_svm.pkl")

# Use the ETL process to get data
# In a real scenario, you'd modularize and import the ETL process
# Here we're assuming X_train and y_train are already populated
X_train, y_train = load_data_for_training(data)
train_model(X_train, y_train)