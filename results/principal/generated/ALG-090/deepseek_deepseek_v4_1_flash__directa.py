def longest_word_length(s):
    return max((len(word) for word in s.split()), default=0)
