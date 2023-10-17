import joblib
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer
from store_data import x


_test=[]
f = open('sampleInput.txt')
for i in range(int(f.readline())):
    s=f.readline().rstrip()
    idx=s.find("\t")
    _test.append(s[:idx])
f.close()

# x =  ['axe deo', 'best-seller books', 'calvin klein', 'camcorder', 'camera', 'chemistry', 'chromebook', \
#      'c programming', 'data structures algorithms', 'dell laptops', 'dslr canon', 'mathematics', \
#      'nike-deodrant', 'physics', 'sony cybershot', 'spoken english', 'timex watch', 'titan watch', \
#      'tommy watch', 'written english']


def predict(X):
    model = joblib.load("model_svm.pkl")
    transformer = HashingVectorizer(stop_words='english')
    test = transformer.transform(X)
    return model.predict(test)

test_label = predict(_test)
for e in test_label:
    print(x[e])