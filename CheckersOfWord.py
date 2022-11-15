from ParseToken import *
from itertools import combinations
import Cleaners


# Проверяет связность слов по их свойствам (род, число, падеж...)
class ConectiablePercentsOfPaire:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def action(self):
        return DiscriptPercentCompare(
            dict(
                sorted(
                    ParseTokenOnMorphs(
                        self.word1).action().items()
                )
            ),
            dict(
                sorted(
                    ParseTokenOnMorphs(
                        self.word2).action().items()))).action()


# Сравнивает роли слов (вид, часть речи ...)
class CompareRoleOfPaireInPercents:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def action(self):
        return DiscriptPercentCompare(
            dict(
                sorted(
                    ParseTokenOnTags(
                        self.word1).action().items()
                    )
                ), 
            dict(
                sorted(
                    ParseTokenOnTags(
                        self.word2).action().items()))).action()


# Возвращает комбинации слов
class GetCombOfWord:
    def __init__(self, words, size=2):
        self.words = words
        self.size = size

    def action(self):
        return combinations(self.words, self.size)


# Полная туфта, не работает
class GetCleanCombOfWord:
    def __init__(self, words, size=2):
        self.words = words
        self.size = size

    def action(self):
        return combinations(filter(lambda k: k.text not in russian_stopwords 
                                             and 
                                             k.text not in Cleaners.punctuation
                                             and len(k.text) > 1
                                             , self.words), self.size)


# Сравнивает дискрипторы (словари)
class DiscriptPercentCompare:
    def __init__(self, v1, v2):
        self.v1 = min(v1, v2, key=len)
        self.v2 = max(v2, v1, key=len)

    def action(self):
        return sum(map(lambda a: self.v1[a] == self.v2.get(a), self.v1)) / len(self.v2) * 100


class IsBadWordPairs:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
    
    def action(self):
        return any(map(lambda a: a in Cleaners.punctuation + Cleaners.russian_stopwords, [self.word1, self.word2]))
    
