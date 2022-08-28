from data_parser.ngrams import calculate_ngrams

def test_calculate_ngrams():
    text = "hello world whatsup"
    n = 2
    output = ['hello world','world whatsup']

    assert calculate_ngrams(text,n) == output

