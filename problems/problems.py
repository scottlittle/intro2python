import itertools

### Fill in each function below. Each function should be a one-liner.

def word_lengths1(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Example:
    >>> word_lengths1("Welcome to Intro to Python!")
    [7, 2, 5, 2, 7]
    '''


def word_lengths2(phrase):
    '''
    INPUT: string
    OUTPUT: list of integers

    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.
    '''

def even_odd1(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    
    Example:
    >>> even_odd([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''

def even_odd2(L):
    '''
    INPUT: list of integers
    OUTPUT: list of strings
    
    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.
    '''


def shift_on_character(string, char):
    '''
    INPUT: string, string
    OUTPUT: string
    
    Find the first occurence of the character char and return the string witth
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.
    
    This function may use more than one line.
    
    Example:
    >>> shift_on_character("perfect", "f")
    'fectper'
    '''


def is_palindrome(string):
    '''
    INPUT: string
    OUTPUT: boolean
    
    Return whether the given string is the same forwards and backwards.
    
    Example:
    >>> is_palindrome("rats live on no evil star")
    True
    '''


def alternate(L):
    '''
    INPUT: list
    OUTPUT: list
    
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.
    
    Example:
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''


def shuffle(L):
    '''
    INPUT: list
    OUTPUT: list
    
    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.
    
    Example:
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''


def filter_words(word_list, letter):
    '''
    INPUT: list of words, string
    OUTPUT: list of words

    Use filter to return the words from word_list which start with letter.

    Example:
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''

def factors(num):
    '''
    INPUT: integer
    OUTPUT: list of integers

    Use filter to return all of the factors of num.
    '''

def acronym(phrase):
    '''
    INPUT: string
    OUTPUT: string

    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Example:
    >>> acronym("good job")
    'GA'

    Hint: You can do this on one line using list comprehension and the join
    method. Python has a builtin string method to uppercase strings.
    '''


def sort_by_ratio(L):
    '''
    INPUT: list of 2-tuples of integers
    OUTPUT: None
    
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.
    
    Example:
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    


def count_match_index(L):
    '''
    INTPUT: list of integers
    OUTPUT: integer
    
    Use enumerate and other skills from above to return the count of the number
    of items in the list whose value equals its index.
    
    Example:    
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    

def only_sorted(L):
    '''
    INPUT: list of list of integers
    OUTPUT: list of list of integers
    
    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.
    
    Example:
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''


def concatenate(L1, L2, connector=""):
    '''
    INPUT: list of strings, list of strings
    OUTPUT: list of strings
    
    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.
    
    Example:
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada',
    'Los Angeles, California']
    '''


def transpose(mat):
    '''
    INPUT: 2 dimensional list of integers
    OUTPUT: 2 dimensional list of integers
    
    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.
    '''


def invert_list(L):
    '''
    INPUT: list
    OUTPUT: dictionary
    
    Use enumerate and other skills from above to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.
    
    Example:
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''


def digits_to_num(digits):
    '''
    INPUT: list of integers
    OUTPUT: integer
    
    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.
    
    Example:
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''


def intersection_of_sets(list_of_sets):
    '''
    INPUT: list of sets
    OUTPUT: set
    
    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.
    
    Example:
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''


def combinations(alphabet, n):
    '''
    INPUT: string, integer
    OUTPUT: list of strings
    
    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.
    
    Example:
    >>> combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
  

def permutations_in_dict(string, words):
    '''
    INPUT: string, set
    OUTPUT: list of strings
    
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.
    
    Example:
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''

