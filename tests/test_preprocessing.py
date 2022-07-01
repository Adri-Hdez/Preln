from Preln.preprocessing import Preprocessing

def test_preprocessing():
    pipeline = Preprocessing(date=True, date_format='complete', lowercasing=False, punctuation=False, stopwords=False)
    assert pipeline.pipeline('11-02-2022') == 'Viernes 11 de Febrero de 2022'
    
    pipeline = Preprocessing(lowercasing=False, punctuation=False, stopwords=False)
    assert pipeline.pipeline('Ì b LóVe a hôlä NLp') == 'I b LoVe a hola NLp'
    
    pipeline = Preprocessing(punctuation=False, stopwords=False)
    assert pipeline.pipeline('I LoVe NLp') == 'i love nlp'
    
    pipeline = Preprocessing(stopwords=False)
    assert pipeline.pipeline('I LoVe NLp{}[]?¿¡!;,:._-^*·#') == 'i love nlp'
    
    pipeline = Preprocessing()
    assert pipeline.pipeline('I b LoVe a hola NLp{}[]?¿¡!;,:._-^*·#') == 'love nlp'
    