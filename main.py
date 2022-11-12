import spacy
import ParseToken
import ParseTokens
nlp = spacy.load("ru_core_news_sm")

# text = "нейронные сети используются для решения нечётких и сложных проблем"
# a = nlp(text)
# s1 = ParseToken.ParseTokenOnTags(a[0]).action()
# s2 = ParseToken.ParseTokenOnMorphs(a[0]).action()
# print({**s1, **s2})
# print(ParseToken.ParseTokenOnAll(a[0]).action())

# print(ParseTokens.ParseTokensOnAll(a).action())




