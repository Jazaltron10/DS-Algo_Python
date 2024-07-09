
a = ['Annie', 'Bonnie', 'Connie', 'Donnie', 'Emmie']
b = [1991, 1992, 1993, 1994, 1995]

print ('Demonstrating tuples')

def comb_tupl (x, y):
    c = list (zip (x, y))
    print (c)
    return c

comb_tupl (a, b)
print ('\nDemonstrating list')

def comb_lst (x, y):
    c = []
    for i in x:
        index = x.index (i)
        d = [i, y[index]]
        c.append (d)
    print (c)
    return c

comb_lst (a, b)
print ('\nDemonstrating dictionary')

def comb_dict (x, y):
    c = dict ()
    for i in x:
        index = x.index (i)
        c[i] = y[index]
    print (c)
    return c


comb_dict (a, b)


def second():
    print ('\nDemonstrating tuples')

    def sep_tupl (x, y):
        c = comb_tupl(x, y)
        name, year = zip (*c)
        name, year = list (name), list (year)
        print ('Name =', name)
        print ('Year =', year)
        return name, year
    
    sep_tupl (a, b)
    
    print ('\nDemonstrating list')
    
    def sep_lst (x, y):
        name = []
        year = []
        c = comb_lst (x, y)
        for i in c:
            for j in i:
                index = i.index (j)
                if index == 0:
                    name.append (j)
                else:
                    year.append (j)
        print ('Name =', name)
        print ('Year =', year)
        return name, year
    
    sep_lst (a, b)
    
    print ('\nDemonstrating dictionary')
    
    def sep_dict (x, y):
        name = []
        year = []
        c = comb_dict (x, y)
        for i in c:
            name.append (i)
            year.append (c[i])
        print ('Name =', name)
        print ('Year =', year)
        return name, year
    
    sep_dict (a, b)






def third():
    a = ['Annie', 'Bonnie', 'Connie', 'Donnie', 'Emmie']

    print ('Demonstrating tuples')

    def count_tupl (x):
        b = ()
        for i in enumerate (x):
            b = b + (i,)
        print (b)
        return b

    count_tupl (a)

    print ('\nDemonstrating list')

    def count_lst (x):
        b = ()
        for i in x:
            index = x.index (i)
            c = index, x[index]
            b = b + (c,)
        print (b)
        return b

    count_lst (a)

    print ('\nDemonstrating dictionary')

    def count_dict (x):
        b = dict ()
        for i in x:
            index = x.index (i)
            b[index] = i
        print (b)
        return b

    count_dict (a)


def fourth():
    d = {'Annie': 1991, 'Bonnie': 1992, 'Connie': 1993, 'Donnie': 1994, 'Emmie': 1995}
    c = d.items ()
    print (c)
    
    def dict_items (a):
        name = ()
        year = ()
        for key, value in a.items ():
            name = name + (key,)
            year = year + (value,)
        print ('Name =', name)
        print ('Year =', year)
        return name, year
    
    dict_items (d)

    
    
import os

cwd = os.getcwd()

try:
    fin = open(cwd, 'r')
    print('Reading file succeeded')
except IsADirectoryError:
    print('Is a directory')
except FileNotFoundError:
    print('No such file exists')
except PermissionError:
    print('Not your business')
except:
    print('Some other bug')

try:
    fin = open('test_dir', 'r')
    print('Reading file succeeded')
except IsADirectoryError:
    print('Is a directory')
except FileNotFoundError:
    print('No such file exists')
except PermissionError:
    print('Not your business')
except:
    print('Some other bug')

try:
    fin = open(cwd +'/test_dir', 'r')
    print('Reading file succeeded')
except IsADirectoryError:
    print('Is a directory')
except FileNotFoundError:
    print('No such file exists')
except PermissionError:
    print('Not your business')
except:
    print('Some other bug')

try:
    fin = open('/test_dir', 'r')
    print('Reading file succeeded')
except IsADirectoryError:
    print('Is a directory')
except FileNotFoundError:
    print('No such file exists')
except PermissionError:
    print('Not your business')
except:
    print('Some other bug')