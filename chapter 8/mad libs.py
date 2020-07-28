'''
mad libs

INPUT
file 'madlibs' containing:
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

OUTPUT
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

'''

import re

file = open('madlibs')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for i in regex.findall(text):
    for j in i:
        if j != '':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter a %s: ' %j)
            text = reg.sub(inp_text, text, 1)

print(text)

file = open('madlibs_answer', 'w')
file.write(text)
file.close()