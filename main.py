import functions as f

if __name__ == "__main__":
    s1 = f.SplitOnSentences(
        f.GetCleanUrlText(
            "https://www.wipo.int/about-ip/ru/artificial_intelligence/"
        ).action()
    ).action()[0]

    # s2 = f.GetCombOfWord(
    #     f.GetWordsTyped(
    #         f.RMStopWords(
    #             f.SplitOnWords(s1).action()
    #         ).action(),
    #         ["NOUN", "ADJF"]
    #     ).action()
    # ).action()

    s2 = f.RMStopWords(
        f.RMSymbolsWords(
            f.SplitOnToken(s1).action()).action()).action()
    s3 = f.GetConnectiablePares(f.GetTypedPares(f.GetCombOfWord(s2).action(), "NOUN", "ADJF").action()).action()
    print(*s3, sep="\n")
