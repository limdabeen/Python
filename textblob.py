from textblob import TextBlob

word = "resterant"

corrected_word = TextBlob(word).correct()
print("Original Word:", word)
print("Corrected Word:", corrected_word)