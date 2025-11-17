def count_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words :
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency
sentence = "Python is fun , leaning and easy language ! "
print(count_frequency(sentence))