def main():
    words_to_count = {}
    user_sentence = input("Enter a Sentence :")
    list_of_words = user_sentence.split()
    list_of_words.sort()
    for word in list_of_words:
        if word not in words_to_count:
            words_to_count[word] = 1
        else:
            words_to_count[word] += 1
    word_alignment = len(max(list_of_words, key=len))
    for word, count in words_to_count.items():
        print('{:<{}} : {}'.format(word, word_alignment, count))


if __name__ == '__main__':
    main()
