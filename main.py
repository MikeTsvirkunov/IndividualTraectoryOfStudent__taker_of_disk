import spacy
import ParseToken
import ParseTokens
import CheckersOfWord
import Spliters
import Cleaners
import GetFromUrl
import re
import Levenshtein
import pymorphy2
import pandas
from pathlib import Path
morph = pymorphy2.MorphAnalyzer()
nlp = spacy.load("ru_core_news_sm")

artificial_intelligence = [
    "https://ru.m.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82",
    "https://www.tadviser.ru/index.php/%D0%9F%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82:%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82_(%D0%98%D0%98,_Artificial_intelligence,_AI)",
    # "https://www.wipo.int/about-ip/ru/artificial_intelligence/",
    # "https://www.oracle.com/cis/artificial-intelligence/what-is-ai/",
    # "https://aws.amazon.com/ru/machine-learning/what-is-ai/",
    # "https://plus-one.ru/economy/2020/06/16/10-faktov-ob-iskusstvennom-intellekte",
    # "https://platforms.su/articles/1522https://platforms.su/articles/1522",
    # "https://habr.com/ru/post/416889/",
    # "https://openedu.ru/course/hse/INTRAI/"
]

# text = "нейронные сети используются для решения нечётких и сложных проблем"
# a = nlp(text)
# s1 = ParseToken.ParseTokenOnTags(a[0]).action()
# s2 = ParseToken.ParseTokenOnMorphs(a[0]).action()
# print({**s1, **s2})
# print(ParseToken.ParseTokenOnAll(a[0]).action())

# print(*ParseTokens.ParseTokensOnAll(a).action(), sep="\n")

# a2 = CheckersOfWord.GetCombOfWord(a).action()

# for i in a2:
#     if all(map(lambda k: k.text not in ParseToken.russian_stopwords, i)):
#         print(*i, " -- ", CheckersOfWord.ConectiablePercentsOfPaire(*i).action(),
#               " / ", CheckersOfWord.CompareRoleOfPaireInPercents(*i).action())


# print(bool(re.match(Cleaners.rm_short, 'l.')))
# url = "https://ru.m.wikipedia.org/wiki/%D0%98%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D0%BB%D0%BB%D0%B5%D0%BA%D1%82"

s = dict()
for url in artificial_intelligence:
    text = GetFromUrl.GetCleanUrlText(url).action()
    senteces_of_text = Spliters.SplitOnSentences(text).action()
    for sentece in senteces_of_text:
        comb_of_words_in_sentece = CheckersOfWord.GetCombOfWord(nlp(sentece)).action()
        for i in comb_of_words_in_sentece:
            if not(re.match(Cleaners.rm_short, i[1].text) or 
                re.match(Cleaners.rm_short, i[0].text) or 
                re.match(Cleaners.rm_spaces, i[0].text) or 
                re.match(Cleaners.rm_spaces, i[1].text)):
                try:
                    if CheckersOfWord.ConectiablePercentsOfPaire(*i).action() > 40 and CheckersOfWord.CompareRoleOfPaireInPercents(*i).action() < 70:
                        # w = sorted(list(map(lambda w: max(morph.parse(w.text), key=lambda z: z.score), i)))
                        # k = tuple([w[0].normal_form, w[1].normal_form])
                        
                        k = tuple(sorted(map(lambda a: a.text, i)))
                        try:
                            f = True
                            for j in s.keys():
                                if Levenshtein.ratio(j[0], k[0]) > 0.7 and Levenshtein.ratio(j[1], k[1]) > 0.7:
                                    s[k] += 1
                                    f = False
                            if f:
                                if len(list(filter(lambda a: a not in ParseToken.russian_stopwords and a not in Cleaners.punctuation, k))) ==2:
                                    s[k] = 1
                        except:
                            pass
                except:
                    pass

print(len(s))
k = {"words_pair": [], "nums": []}
for i in s:
    if s[i] > 1:
        k["words_pair"].append(" ".join(i))
        k["nums"].append(s[i])


df = pandas.DataFrame(k)
filepath = Path('./out.csv')
# filepath.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(filepath)
# df = pandas.DataFrame(s)
# df.to_csv()
# compression_opts = dict(method='zip',
#                         archive_name='out.csv')
# df.to_csv('out.zip', index=False, compression=compression_opts)
