#search a character
def search_from_left(text, char):
    i = 0
    while i < len(text):
        if text[i] == char:
            return i
        i += 1
    return -1

def search_from_right(text, char):
    i = len(text) - 1
    while i >= 0:
        if text[i] == char:
            return i
        i -= 1
    return -1

def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True