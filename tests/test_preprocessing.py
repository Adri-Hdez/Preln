from Preln.Preln.preprocessing import Preprocessing

def test_preprocessing():
    pipeline = Preprocessing()
    assert pipeline.pipeline('HoLa') == 'hola'