def remove_vowels(s):
    vowels=set("AEIOUaeiou")
    result=''.join([ch for ch in s if ch not in vowels])
    return result
text="Have A Beautiful Day Today"
print("Original String :",text)
print("String without vowels :",remove_vowels(text))