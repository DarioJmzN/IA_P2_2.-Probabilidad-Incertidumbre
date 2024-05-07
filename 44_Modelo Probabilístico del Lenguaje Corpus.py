#Pablo Dario Jimenez Nu*o 21310143

from collections import defaultdict
import nltk
nltk.download('punkt')

class ProbabilisticLanguageModel:
    def __init__(self, corpus):
        self.word_counts = defaultdict(int)
        self.total_words = 0
        self.build_model(corpus)

    def build_model(self, corpus):
        tokens = nltk.word_tokenize(corpus.lower())
        for token in tokens:
            self.word_counts[token] += 1
            self.total_words += 1

    def word_probability(self, word):
        return self.word_counts[word] / self.total_words

    def sentence_probability(self, sentence):
        tokens = nltk.word_tokenize(sentence.lower())
        probability = 1.0
        for token in tokens:
            probability *= self.word_probability(token)
        return probability

# Ejemplo de uso
corpus = "El gato está sobre la mesa. El perro está bajo la mesa."
model = ProbabilisticLanguageModel(corpus)

sentence = "El gato está sobre la mesa."
probability = model.sentence_probability(sentence)
print("Probabilidad de la oración '{}': {}".format(sentence, probability))























