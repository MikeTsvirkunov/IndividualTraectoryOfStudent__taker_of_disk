import spacy
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
russian_stopwords.extend(
    ['это', "который", 'он', 'например', 'которые', 'none']
)
