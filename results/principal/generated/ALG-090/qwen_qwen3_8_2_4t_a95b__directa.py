def find_longest_word_length(text):
    words = text.split()
    return max((len(word) for word in words), default=0)
