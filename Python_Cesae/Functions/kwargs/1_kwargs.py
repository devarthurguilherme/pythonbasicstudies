#Kwargs are "keyword arguments", they are like args, but it returns a Dictionary wit several KEYS and their values, so when to think of KEYS and VALUES, use KWARGS
#Args when to think of Tuples(List without accepting new values, like "Constant Lists")

def emptyExample(**kwargs):
    print(kwargs)
    print(type(kwargs))

emptyExample()