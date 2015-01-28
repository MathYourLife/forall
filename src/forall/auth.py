
def greeting(session, stream, accts):
    session.name = stream.input('Hi. what is your name? ')
    check_login(session.name, accts, stream)
    stream('\nHi %s.\nHere we go...\n\n' % session.name)

def check_login(name, accts, stream):
    if name.lower() not in accts:
        stream("I don't know %s.\nI know\n" % name)
        for acct in accts:
            stream("  %s\n" % acct)
        exit(0)

