# # Import spaCy
# import spacy

# # Create a blank English nlp object
# nlp = spacy.blank("en")

# # Created by processing a string of text with the nlp object
# doc = nlp("Hello world!")

# # Iterate over tokens in a Doc
# for token in doc:
#     print(token.text)

# doc = nlp("Hello world!")

# # Index into the Doc to get a single Token
# token = doc[1]

# # Get the token text via the .text attribute
# print(token.text)

# doc = nlp("Hello world!")

# # A slice from the Doc is a Span object
# span = doc[1:3]

# # Get the span text via the .text attribute
# print(span.text)

# doc = nlp("It costs $5.")
# print("Index:   ", [token.i for token in doc])
# print("Text:    ", [token.text for token in doc])

# print("is_alpha:", [token.is_alpha for token in doc])
# print("is_punct:", [token.is_punct for token in doc])
# print("like_num:", [token.like_num for token in doc])

"""
What are trained pipelines?
- Models that enable spaCy to predict linguistic attributes in context
    - Part-of-speech tags
    - Syntactic dependencies
    - Named entities
- Trained on labeled example texts
- Can be updated with more examples to fine-tune predictions

Donwloading trained pipeline:

# python -m spacy download en_core_web_sm

Contents:
- Binary weights
- Vocabulary
- Meta information
- Configuration file
"""
from os import sep
import spacy

nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("She golang python angular angularjs ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)

"""
Label	    Description     	    Example
nsubj	    nominal subject	        She
dobj	    direct object	        pizza
det	        determiner (article)	the
"""
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)


# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

# labels explanation
print(
    spacy.explain("GPE"),
    spacy.explain("NNP"),
    spacy.explain("dobj"),
    sep="\n",
)

