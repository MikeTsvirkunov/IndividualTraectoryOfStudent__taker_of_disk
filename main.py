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
# s.update({"w": 1})
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
                    # print(CheckersOfWord.CompareRoleOfPaireInPercents(*i).action())
                    if CheckersOfWord.ConectiablePercentsOfPaire(*i).action() > 40 and CheckersOfWord.CompareRoleOfPaireInPercents(*i).action() < 70:
                        # w = sorted(list(map(lambda w: max(morph.parse(w.text), key=lambda z: z.score), i)))
                        # k = tuple([w[0].normal_form, w[1].normal_form])
                        k = tuple(i)
                        # print(type(k[0]))
                        try:
                            f = True
                            # print(Levenshtein.ratio(k[1], k[0]))
                            # print(k)
                            for j in s.keys():
                                # print(k[0])
                                # print(Levenshtein.ratio(j[0], k[0]) )
                                if Levenshtein.ratio(j[0], k[0]) > 0.5 and Levenshtein.ratio(j[1], k[1]) > 0.5:
                                    s[k] += 1
                                    f = False
                            if f:
                                # print(k)/
                                # print("added")
                                s[k] = 1
                        except:
                            pass
                            # print("err")
                        # if k not in s:
                        #     s[k] = 1
                        # else:
                        #     s[k] += 1
                            
                        # print(*i)
                        # if " ".join(i) not in s.keys():
                        #     if " ".join(i[::-1]) not in s.keys():
                        #         s[" ".join(i)] = 1
                        #     else:
                        #         s[" ".join(i)[::-1]] += 1
                        # else:
                        #     s[" ".join(i)] += 1
                except:
                    pass
                    # print

print(len(s))
for i in s:
    if s[i] > 1:
        print(i)
