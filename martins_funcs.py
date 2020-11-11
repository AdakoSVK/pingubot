def f_martin(text,user):
    if text.author == user.user:
        return False

    if 'happy birthday' in text.content.lower():
        return 'Happy Birthday! 🎈🎉'

    elif 'ping' in text.content.lower():
        return 'pong :ping_pong: '
    return False

def chyba():
    print('nie chyba')

