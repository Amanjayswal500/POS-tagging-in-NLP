import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK data (only need to do this once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to perform POS tagging
def pos_tag_sentence(sentence):
    # Tokenize the sentence into words
    tokens = word_tokenize(sentence)
    
    # Perform POS tagging
    tagged_tokens = pos_tag(tokens)
    
    return tagged_tokens

# Example sentence
sentence = "Aman is intelligent boy." # paste your corpus

# Get POS tags
tagged_sentence = pos_tag_sentence(sentence)

# Print the sentence with POS tags
print("Sentence with POS tags:")
for word, tag in tagged_sentence:
    print(f"{word}: {tag}")