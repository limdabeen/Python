from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input  
from sklearn.model_selection import KFold
import pandas as pd

df = pd.read_csv('/Users/imdabin/Desktop/sonar3.csv', header=None)
X = df.iloc[:, 0:60]
y = df.iloc[:, 60]

k = 5
kfold = KFold(n_splits=k, shuffle=True, random_state=42)
acc_score = []

for train_index, test_index in kfold.split(X):
    X_train, X_test = X.iloc[train_index, :], X.iloc[test_index, :]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model = Sequential()
    model.add(Input(shape=(60,)))  
    model.add(Dense(24, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=200, batch_size=10, verbose=0)

    accuracy = model.evaluate(X_test, y_test, verbose=0)[1]
    acc_score.append(accuracy)

avg_acc_score = sum(acc_score) / k
print('정확도:', acc_score)
print('60231222_11_02_LDB : 정확도 평균:', avg_acc_score)