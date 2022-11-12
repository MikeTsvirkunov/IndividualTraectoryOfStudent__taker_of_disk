class SplitOnSentences:
    def __init__(self, text):
        self.text = text

    def action(self):
        return self.text.split(". ")


class SplitOnWords:
    def __init__(self, text):
        self.text = text

    def action(self):
        return self.text.split(" ")
