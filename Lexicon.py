__author__ = 'Syd'
import re


def file_opener(file_name):
    try:
        file_handle = open(file_name)
    except FileNotFoundError:
        print('File not found, please make sure the file is in your directory')
        file_handle = 'swallow'
    return file_handle


def file_reader_lines(file_handle):
    lines = []
    for line in file_handle:
        lines.append(line)
    return lines


def word_list(lines):
    true_vocab = []
    for line in lines:
        words = line.split()
        for word in words:
            true_vocab.append(word)
    return true_vocab


def clean_words(words):
    new_vocab = []
    for word in words:
        word = re.sub('\([A-Z]*[0-9]*[a-z]*\)', ' ', word)
        word = re.sub('\[[A-Z]*[0-9]*[a-z]*\]', ' ', word)
        word = re.sub(r'[!$#%*\(\)\{\}\[\]\+\"=|/:;~`\\]', ' ', word)
        word = word.lower()
        word = word.strip()
        word = word.strip('.')
        word = word.strip(',')
        new_vocab.append(word)
    return new_vocab


def vocab_cleanse(subject):
    clean_vocab = dict()
    subject = clean_words(subject)
    while len(subject) != 0:
        word = subject.pop()
        if word in clean_vocab:
            clean_vocab[word] += 1
        else:
            clean_vocab[word] = 1
    return clean_vocab


def printer(data, values=False):
    counter = 0
    for term in data:
        if term != '':
            counter += 1
        if values:
            print(term, data[term])
        else:
            print(term)

    return counter

def input_screen():
    f_name = input("Enter a file name: ", )
    if f_name == 'quit': exit()    
    f_hand = file_opener(f_name)
    if f_hand == 'swallow': input_screen()
    else: return f_hand, f_name

f_hand, f_name = input_screen()
vocab = word_list(file_reader_lines(f_hand))
fin_vocab = vocab_cleanse(vocab)

print("The file " + f_name + " has a vocabulary of the words: ")
count = printer(fin_vocab, values=True)
print("There are " + str(count) + " unique word in " + f_name)
