from Preln.preprocessing import Preprocessing

def test_preprocessing():
    pipeline = Preprocessing(punctuation=False)
    assert pipeline.pipeline('I LoVe NLp') == 'i love nlp'
    
    pipeline = Preprocessing()
    assert pipeline.pipeline('I LoVe NLp{}[]?¿¡!;,:._-^*·#') == 'i love nlp'
    