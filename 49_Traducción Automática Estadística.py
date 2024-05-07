#Pablo Dario Jimenez Nu*o 21310143

import nltk
from nltk.translate import IBMModel1

# Corpus de entrenamiento
bitexts = [
    [['I', 'love', 'cats'], ['j\'aime', 'les', 'chats']],
    [['cats', 'are', 'cute'], ['les', 'chats', 'sont', 'mignons']],
    [['dogs', 'are', 'loyal'], ['les', 'chiens', 'sont', 'fidèles']]
]

# Entrenar el modelo IBM Model 1
ibm1 = IBMModel1(bitexts, 10)

# Traducir una oración nueva
new_sentence = ['I', 'like', 'dogs']
translation_probabilities = ibm1.translation_table[new_sentence[0]]
for word in new_sentence[1:]:
    translation_probabilities = translation_probabilities * ibm1.translation_table[word]
best_translation = max(translation_probabilities, key=lambda x: translation_probabilities[x])

print("Oración original:", new_sentence)
print("Traducción:", best_translation)




























