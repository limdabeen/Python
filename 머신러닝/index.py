text = "오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"

token = Tokenizer()
token.fit_on_texts([text])

print(token.word_index)

x = token.texts_to_sequences([text])
print("정수 시퀀스:", x)

from tensorflow.keras.utils import to_categorical

word_size = len(token.word_index) + 1
x = to_categorical(x, num_classes=word_size)

print("원-핫 인코딩:\n", x)