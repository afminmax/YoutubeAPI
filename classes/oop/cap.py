def cap_text(text):
    '''
    Input a string \n
    Capitalizes the first letter of a string
    '''
    try:
        return text.title()
    except:
        print('boo, bad error!')
