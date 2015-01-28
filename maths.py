import os
import sys
import time
import json
import traceback
import numpy as np

class std_out(object):
    def __call__(self, msg, lf=True):
        sys.stdout.write(msg)
        sys.stdout.flush()

    def input(self, prompt):
        return input(prompt)

class Question(object):
    prompt = None
    solution = None
    answer = None
    def __init__(self, question, solution):
        self.prompt = question
        self.solution = solution

    def json(self):
        return {
            'prompt': self.prompt,
            'solution': self.solution,
            'answer': self.answer,
        }

def explain(session, tracker, stream, question):
    time.sleep(1)
    stream(question.prompt)
    time.sleep(1)
    stream("%d" % question.solution)
    time.sleep(3)


def check(session, tracker, stream, question):
    if question.answer == question.solution:
        session.correct()
        tracker.correct(session, question)
        congratulate(session, tracker, stream)
    else:
        session.notyet()
        tracker.notyet(session, question)
        encourage(session, tracker, stream)
        explain(session, tracker, stream, question)

def play(session, tracker, stream, pool):
    while True:
        try:
            skills = list(pool.keys())
            np.random.shuffle(skills)
            skill = skills[0]
            kwargs = pool[skill]
            question = skill(**kwargs)
            repl = stream.input(question.prompt)
            try:
                repl = int(repl)
            except ValueError:
                repl = None
            question.answer = repl
            check(session, tracker, stream, question)
            stream('\n\n')
        except KeyboardInterrupt:
            break

def main():
    try:
        with open('config.json') as f:
            cfg = json.load(f)
        accts = {
            0: {
                'name': 'ian',
            },
            1: {
                'name': 'dominic',
            },
        }
        SKILLS = {
            'ian': {
                addition: {'limit': 8}
            },
            'dominic': {
                addition: {'limit': 20},
                subtraction: {'limit': 20},
                multiplication: {'limit': 5}
            },
        }

        logfile = os.path.join(cfg['logdir'], 'maths.log')
        with open(logfile, 'a') as f:
          tracker = Tracker(f)
          session = Session()
          stream = std_out()
          greeting(session, stream, [acct['name'] for acct in accts.values()])
          pool = SKILLS[session.name.lower()]
          play(session, tracker, stream, pool)

    except Exception as err:
        errfile = os.path.join(cfg['logdir'], 'maths.err')
        with open(errfile, 'a') as f:
            f.write("%f" % time.time())
            f.write("%s" % traceback.format_exc())


def congratulate(session, tracker, stream):
    opt = np.random.rand()
    if opt < 0.1:
        stream('Nice work %s!' % session.name)
    elif opt < 0.2:
        stream('CORRECT!')
    elif opt < 0.3:
        stream('WooHoo!')
    elif opt < 0.35:
        stream('Harry Potter is proud of you')
    elif opt < 0.45:
        stream(':)')
    elif opt < 0.5:
        stream('Awesome work')
    elif opt < 0.52:
        stream("""
             O_      __)(
           ,'  `.   (_".`.
          :      :    /|`
          |      |   ((|_  ,-.
          ; -   /:  ,'  `:(( -\\
         /    -'  `: ____ \\\\\\-:
        _\__   ____|___  \____|_
       ;    |:|        '-`      :
      :_____|:|__________________:
      ;     |:|                  :
     :      |:|                   :
     ;______ `'___________________:
    :                              :
    |______________________________|
     `---.--------------------.---'
         |____________________|
         |                    |
         |____________________|
         |SSt                 |
       _\|_\|_\/(__\__)\__\//_|(_""")
    elif opt < 0.54:
        stream("""
           (:)_
         ,'    `.
        :        :
        |        |              ___
        |       /|    ______   // _\\
        ; -  _,' :  ,'      `. \\\\  -\\
       /          \/          \ \\\\  :
      (            :  ------.  `-'  |
   ____\___    ____|______   \______|_______
           |::|           '--`           SSt
           |::|
           |::|
           |::|
           |::;
           `:/""")
    elif opt < 0.56:
        stream("""
               ,-.
             .:\ '`-.
             |:|  __ b
              `;-(
             ,'  |
            ( \|||_
     ,-----(.-''--``-------.
    /_______`'______________\\
   /                      SSt\\""")
    elif opt < 0.58:
        stream(""" Hi Five!
       _.-._
     _| | | |
    | | | | |
    | | | | |
    | _.-'  | _
    ;_.-'.-'/`/
    |   '    /
     \  '.  /
      |    | jgs""")
    elif opt < 0.60:
        stream("""
                ."";._   _.---._   _.-"".
               /_.'_  '-'      /`-` \\_   \\
             .'   / `\\         \\   /` \\   '.
           .'    /    ;    _ _  '-;    \\   ;'.
        _.'     ;    /\\   / \\ \\    \\    ;  '._;._
     .-'.--.    |   /  |  \\0|0/     \\   |        '-.
    / /`    \\   |  /  .'             \\  | .---.     \\
   | |       |  / /--'   .-\"\"\"-.      \\ \\/     \\     |
   \\ \\      /  / /      (  , ,  )     /\\ \\      |    /
    \\ '----' .' |        '-(_)-'     |  | '.   /    /
     `'----'`   |                    '. |   `'----'`
            jgs \\                      `/
                 '.         ,         .'
                   `-.____.' '.____.-'
                          \\   /
                           '-'""")
    elif opt < 0.63:
      stream("""( ͡° ͜ʖ ͡°) """)
    elif opt < 0.66:
      stream(""".·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>  """)
    elif opt < 0.69:
      stream("""_̴ı̴̴̡̡̡ ̡͌l̡̡̡ ̡͌l̡*̡̡ ̴̡ı̴̴̡ ̡̡͡|̲̲̲͡͡͡ ̲▫̲͡ ̲̲̲͡͡π̲̲͡͡ ̲̲͡▫̲̲͡͡ ̲|̡̡̡ ̡ ̴̡ı̴̡̡ ̡͌l̡̡̡̡.___ """)
    else:
        stream('✓')


def encourage(session, tracker, stream):
    opt = np.random.rand()
    if opt < 0.1:
        stream("""
|     ,-'                `-._      |
|   ,'   _       _  _  _  _  `.    |
|  /    / \|_|  /__/ \/ \| \   \   |
| :     \_/| |, \_/\_/\_/|,'    :  |
| :        _  _    _  _         ;  |
|  \      /__|,' ||_ |_ |      /   |
|   `.    \_/|`. ||_ |  .    ,'    |
|     `.                  _.'      |
|       \(`--..._____..-''         |
|        `\  _____                 |
|          ,' _  _`.               |
|         /  ,' _ `.\              |
|        :    ' _)'  :             |
|       (_           ;)            |
|         \  ..---. /              |
|          `..__ _.'               |
|            ,'._(_                |
|           ,'`' `-'               |
|          /    _   \              |
|---------/__,)/)\._|\-------------|
|---------(   _,.'   ;-------------|
|_________|`-'\_/`--'|__________SSt|
""")
    elif opt < 0.2:
        stream("""
          _.-----._
  \)|)_ ,'         `. _))|)
   );-'/             \`-:(
  //  :               :  \\\\   .
 //_,'; ,.         ,. |___\\\\
 `---':(  `-.___.-'  );----'
       \`. `'-'-'' ,'/
        `.`-.,-.-.','
          ``---\` :
                `.'
""")
    if opt < 0.3:
        stream("""
    |.==============================,|
    ||  I WILL NOT TALK IN CLASS.   ||
    ||  I WILL NOT TALK IN CLASS.   ||
    ||  I WILL NOT TALK IN CLASS.   ||
    ||  I .----.OT T,               ||
    ||   / ><   \  /                ||
    ||  |        |/\                ||
    ||   \______//\/                ||
    ||   _(____)/ /                 ||
    ||__/ ,_ _  _/__________________||
    '===\___\_) |===================='
         |______|
         |  ||  |
         |__||__|
    jgs  (__)(__)""")

    else:
        stream("oops  ")


if __name__ == "__main__":
    main()

