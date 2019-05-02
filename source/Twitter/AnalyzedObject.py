class AnalyzedObject(object):
    def __init__(self, raw_text, cleaned_text, polarity):
        self.rawText = raw_text
        self.cleanedText = cleaned_text
        self.polarity = polarity
