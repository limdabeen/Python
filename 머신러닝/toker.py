from tensorflow.keras.preprocessing.text import Tokenizer

docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
        '텍스트의 단어로 토큰화해야 딥러닝에서 인식됩니다.',
        '토큰화한 결과는 딥러닝에서 사용할 수 있습니다.']

token = Tokenizer()
token.fit_on_texts(docs)

print("단어 카운트:", token.word_counts)
print("문장 수:", token.document_count)
print("문장 포함 단어 수:", token.word_docs)
print("단어 인덱스:", token.word_index)