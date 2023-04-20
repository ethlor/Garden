import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences =["The complex houses married and single soldiers and their families.",
                       "The horse raced past the barn fell", "Mary gave the child a Band-Aid.", 
                       "That Jill is never here hurts.", "The cotton clothing is made of grows in Mississippi"]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(i, i.label_, i.label) for i in doc.ents])
    

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

entity_person = spacy.explain("PERSON")
print(f"PERSON:{entity_person}")
""""""
entity_GPE = spacy.explain("GPE")
print(f"GPE:{entity_GPE}")
"""
GPE is country so in example it was Missipi, this doesnt make sense as grows in not a type of material and is used often as a verb so it could mean that it is made of 'grow in Missisipi' or that it grows there
PERSON is people so names like Mary and Jill, Mary made sense as the first letter was capitalised and it had possetion in the folloiwing words. Jill however was more confusing as is could be an objecy called jill 
the garden paths had no named recognition come up
"""


    

