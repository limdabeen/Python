import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Sequential 모델 정의
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# 모델 요약 출력
model.summary()

# 모델 컴파일
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])