import docx2txt
import itertools
import pandas as pd
import re
from nltk.tokenize import PunktSentenceTokenizer
from IPython.core.display import display, HTML
import spacy
display(HTML("<style>.container { width:100% !important; }</style>"))


file = r"C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2021\405010721_TM_NCR\Translation\My_COPY.docx"
  

text = docx2txt.process(file)
text = text.lower()
sent_tokenizer = PunktSentenceTokenizer(text)
sents = sent_tokenizer.tokenize(text)
sents = list(set(sents))

anomls = []

nlp = spacy.load("en_core_web_lg")
for s in sents: 
    tokens = nlp(s)
    for token in tokens:
        if token.vector_norm == 0.0 and len(token.text.split()) > 0 and token.text not in []:
#             print(token.text)
            anomls.append(token.text)
            
anomls = sorted(list(set(anomls)))
anomls
