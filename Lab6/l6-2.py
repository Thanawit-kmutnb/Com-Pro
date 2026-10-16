def countChar(target_char, text):
    count = 0
    i = 0
    while i < len(text):
        if text[i] == target_char:
            count += 1
        i += 1

    return count

print(countChar("a", "Thailand"))

def countVowels(text):
    total_vowels = 0
    for vowel in "aeiouAEIOU":
        total_vowels += countChar(vowel, text)

    return total_vowels

print(countVowels("Bangkok"))