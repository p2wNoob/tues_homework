from random import randrange


# Добавете думи тук
words = [
    'apple',
    'banana',
    'romanreigns',
    'vincemcmahon',
    'word',
    'anotherword',
    'royalgiant',
    'elitebarbs'
]

def get_random_word():
    word_index=randrange(0,len(words))
    return words[word_index]   
  


def fill_char(char, word, original_word):
    """
    Дефинирайте функция, която добавя познатата буква към думата `word`.
    Напр.:
        >>> original_word = 'apple'
        >>> word = '_____'
        >>> word = fill_char('p', word, original_word)
        >>> word
        _pp__
    """
    pass


if __name__ == '__main__':
    original_word = get_random_word()
    word = '_' * len(original_word)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in original_word:
            word = fill_char(char, word, original_word)
            print(word)
