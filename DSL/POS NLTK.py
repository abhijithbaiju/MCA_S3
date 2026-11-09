import nltk

# Step 1: Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Step 2: Enter the input sentence
sentence = "The students are learning natural language processing."

# Step 3: Tokenize the sentence
words = nltk.word_tokenize(sentence)

print("Tokens:")
print(words)

# Step 4: Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Step 5: Display the POS tags
print("\nPart-of-Speech Tags:")

for word, tag in pos_tags:
    print(word, "->", tag)

