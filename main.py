from stats import get_book_wordcount, get_char_count, dict_to_list
import sys

def get_book_text (path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()
    return str(file_contents)



def main():
    if len(sys.argv)<2:
        sys.exit("Usage: python3 main.py <path_to_book>")
    path_to_file=sys.argv[1]
    #print(get_book_text(path_to_file))
    res = (get_char_count(get_book_text(path_to_file)))
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path_to_file}...')
    print("----------- Word Count ----------")
    print(get_book_wordcount(get_book_text(path_to_file)))
    print("--------- Character Count -------")
    sorted_list = dict_to_list(res)
    #print (sorted_list)
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: " + f"{i['count']}")
    print("============= END ===============")
    print(sys.argv)
    #print(dict_to_list(res))
    #print (res)



main()