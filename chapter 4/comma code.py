# comma code
spam = ['apples', 'bananas', 'tofu', 'cats']
'''
def commaCode(lst):
    lst.insert(-1, 'and')
    #for i in range (1, len(lst)):
    print(", ".join(lst[:-2]))
    
commaCode(spam)
'''

def list_thing(list):
    new_string=', '.join(list).rsplit(',', 1)    
    new_string=' and'.join(new_string)
    print(new_string)

list_thing(spam)