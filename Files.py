# Using a file object as part of a loop 

def read_file():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        #print(word)
        #print(line)
    
        # if len(word) >= 7:
        #     print(word, "\n")
        
        for char in word:
            if "e" in word:
                print(word)
            break

            
read_file()
            
def write_file():
    fout = open('words.txt', 'w')
    line1 = "This right here is the wattle, \n"
    fout.write(line1)
    line2 = "The emblem of our. \n" 
    fout.write(line2)
    fout.close()
    
write_file()




# THe Format Operator
"""
The argument of write has to be a string, so if we want to put other valurs in a file, we have to convert them to strings. The easiest way to do that is with str:
"""
# Writing to a file 
def write_file_2():
    fout = open('words.txt', 'w')
    x = 52
    fout.write(str(x))
    
    camels = 43
    print('%d' % camels)
    fout.write("\nI have spotted %d amels." % camels)
    
    """
    A format sequence can appear anywhere in the string 
    also if there is more than one format sequence in the string, the seconf argument has to be a tuple. Each format sequence is matched with an element of the tuple, in order.
    """
    line3 = "\nIn %d years I have spotted %g %s." %(3, 0.1, 'camels')
    fout.write(line3)
    
    dicki = dict(zip((1,2,3,4,5),('anjani', 'cadoga', 'smilokiva', 'jipeeta', 'karaskovich')))
    print('\n', dicki)
    
    fout.write("The inverted Dictionary is %s -> " %dicki)
    

write_file_2()






# Reading From a file 
def write_file_3():
    fin = open('input.txt')
    line1 = fin.readline().strip()
    print(line1)
    line2 = fin.readline().strip()
    print(line2)
    line3 = fin.readline().strip()
    print(line3)
    line4 = fin.readline().strip()
    print(line4)

    line = " " 
    i = 1
    while i <= 10:
        print(fin.readline().strip())
        i += 1
    

write_file_3()


def write_file_4():
    fout = open('FilesOut.txt', 'w')
    # Error 1 TypeError





write_file_4()

import os 
#Filenames and Paths 
def write_file_5():
    """
    Every running program has a "current directory", which is the default
    directory for most operations. 
    
    """
    CurrentWorkingDirectory = os.getcwd()
    print(CurrentWorkingDirectory,"\n") # prints -> C:\Users\Jasper Albert Nri\PycharmProjects\DS_and_Algo
    # The string that is printed out here that identifies the path or directory is called a PATH.
    """
    RELATIVE PATH 
    A Simple filename is also a path, but it is known as a RELATIVE PATH.
    e.g -> memo.txt on it's own is known as a RELATIVE PATH, because it relates to the current directory.
    If the current directory is /home/dinsdale, the filename memo.txt would refer to /home/dinsdale/memo.txt.
    
    ABSOLUTE PATH 
    A path that begins with / does not depenf on the current directory;
    it is called an ABSOLUTE PATH
    
    To find the absolute path to a file, you can use os.path.abspath:
    
    os.path provides other functions for working with filenames and paths. For example,
    os.path.exists checks whether a file or directory exists:
    """
    
    
    print(os.path.abspath('Memo.py'))
    print(os.path.exists('Recursion/MergeSort.py'))
    print(os.path.isdir('/Recursion/MergeSort.py'))
    print(os.path.exists('FilesOut.txt'))
    print(os.listdir(CurrentWorkingDirectory))
    
    
    # A Function That loops through all of the files and folders in a given directory and prints them 
    def walk(dirname):
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)
        
            if os.path.isfile(path):
                print(path)
            else:
                walk(path)
    
    
    walk(CurrentWorkingDirectory)


write_file_5()



# Catching Exceptions
def write_file_6():
    pass













write_file_6()













