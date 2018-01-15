import string
import random

book_name = 'emma.txt'
book_file = open(book_name)

#create a shingle based on the word length
#return a single shingle
def shingleCreator(base_index, prefix_len, words_list):
    one_shingle = ''
    if base_index + prefix_len >= len(words_list):
        return ''
    else:
        for i in range(prefix_len):
            #create a first shingle
            if len(one_shingle) != 0:
                one_shingle += ' '
            one_shingle += words_list[base_index + i]
    return one_shingle



#process the words
book_file_str = book_file.read()
raw_words = book_file_str.split()
processed_word = list()
for single_word in raw_words:
    single_word = single_word.strip(string.whitespace + string.punctuation)
    words = single_word.split('-')
    for single_word_r in words:
        for single_punc in string.punctuation + string.whitespace:
            single_word_r = single_word_r.replace(single_punc, '')
        if len(single_word) != 0:
            processed_word.append(single_word_r.lower())

#After Processing the text
#print('After the processing: \n', processed_word)
#the base case is the prefix of length one
prefix_one_dic = dict() # a dictionary key: word    value: a list
prefix_len = 4
shingle_prev = ''   #this is a single word
for word_index in range(len(processed_word)):
    if word_index == 0:
        shingle_prev = shingleCreator(0, prefix_len, processed_word)
        prefix_one_dic[shingle_prev] = list()
    if word_index > prefix_len - 1:
        current_word = processed_word[word_index]
        #if current_word not in prefix_one_dic[shingle_prev]: # not in word prev's list
        prefix_one_dic[shingle_prev].append(current_word)
        shingle_prev = shingleCreator(word_index - prefix_len + 1, prefix_len, processed_word)
        if shingle_prev not in prefix_one_dic and word_index < len(processed_word):     #if word prev is not in the dictionary
            prefix_one_dic[shingle_prev] = list()
list_of_shingles = list(prefix_one_dic.keys())
#print the dictionary
#print(prefix_one_dic)

#Generate random text

def shingle_updater(old_shingle, word):
    old_words = old_shingle.split()
    new_shingle = ''
    for i in range(1, len(old_words)):
        if i != 1:
            new_shingle += ' '
        new_shingle += old_words[i]
    return new_shingle + ' ' + word

round_num = 100
current_shingle = random.choice(list_of_shingles)
random_text = current_shingle[:]

for i in range(round_num):
    if current_shingle not in prefix_one_dic:
        current_shingle = random.choice(list_of_shingles)
        random_text += ' ' + current_shingle
    next_word = random.choice(prefix_one_dic[current_shingle])
    random_text += ' ' + next_word
    current_shingle = shingle_updater(current_shingle, next_word)
print(random_text)










