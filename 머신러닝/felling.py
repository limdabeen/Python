import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

docs = ["너무 재밌네요", "최고예요", "참 잘 만든 영화예요", "추천하고 싶은 영화입니다",
        "한번 더 보고싶네요", "글쎄요", "별로예요", "생각보다 지루하네요", "연기가 어색해요", "재미없어요"]
classes = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

token = Tokenizer()
token.fit_on_texts(docs)

print("단어 인덱스:", token.word_index)

x = token.texts_to_sequences(docs)
print("시퀀스 변환 결과:", x)