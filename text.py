import copiah

class Signature:
    
    def __init__(self, assog):
        self.average_word_length = assog[0]
        self.type_token = assog[1]
        self.hapax_legomena = assog[2]
        self.average_sentence_length = assog[3]
        self.sentence_complexity = assog[4]
        self.average_phrase_length = assog[5]
    
class Text:

    def __init__(self, text):
        self.text = text
        self.assog = copiah.calculate_signature(text)
        self.signature = Signature(self.assog)

    def evaluate(self, texts):
        return copiah.evaluate_texts(texts, self.assog)