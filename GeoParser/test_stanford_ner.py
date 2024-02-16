
from nltk.parse import CoreNLPParser
def test_stanford_ner(s):
    ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
    return(list(ner_tagger.tag((s.split()))))

