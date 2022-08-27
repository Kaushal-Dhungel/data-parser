text = "hello there, whatsup and how you doing?"

def calculate_ngrams(text,n):
    words=[word for word in text.split(" ")]  
    result = []

    for i in range(len(words)-(n-1)):
        temp = ' '.join([str(elem) for elem in words[i:i+n]])
        result.append(temp)
    return result

print(calculate_ngrams(text,n=5))