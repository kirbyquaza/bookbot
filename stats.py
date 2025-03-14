from operator import itemgetter

def get_book_wordcount(str):
    num_words=len(str.split())
    return (f'Found {num_words} total words')

def get_char_count (str):
    char_dict={}
    word_string=str.lower()
    for i in range (0, len(word_string)):
        if word_string[i] not in char_dict:
            char_dict[word_string[i]] = 1
        else:
            char_dict[word_string[i]] += 1
    return char_dict

def dict_to_list (dict):
    new_dict_list = [{'char': x, 'count': y} for x, y in dict.items()]
    new_dict_list.sort(reverse=True, key=itemgetter('count'))
    return new_dict_list