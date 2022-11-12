import spacy
import ParseToken

text = "нейронные сети используются для решения нечётких и сложных проблем"
s1 = ParseToken.P
print(*ParseToken.ParseTokensOnAll(text).action(), sep="\n")




