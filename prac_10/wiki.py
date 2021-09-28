import wikipedia

user_input = input('Enter phrase or title to search: ')
while user_input != '':
    try:
        page = wikipedia.page(user_input, auto_suggest=False)
        print('Title: {}'.format(page.title))
        print('Summary: {}'.format(page.summary))
        print('Url: {}'.format(page.url))
        user_input = input('Enter phrase or title to search: ')
    except wikipedia.PageError:
        print('{} does not match any pages. Please try again'.format(user_input))
        user_input = input('Enter phrase or title to search: ')
    except wikipedia.DisambiguationError as e:
        print( e.options)
        user_input = input('Enter phrase or title to search: ')
print('---Goodbye---')
