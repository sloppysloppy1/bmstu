from random import *

a = ['lena','olga','nastya','masha','galya','sveta','ira', 'zhenya']
b = ['klyuge','nikitina','olova','zayceva','koneva','toporova','mishkina']
c = ['oleg','anton','vasya','petya','nikita','zhenya', 'abdul','kirill']
d = ['klyuge','nikitin','olov','zaycev','konev','toporov','mishkin']
e = ['solomonova','varshavshkoe sh.','venevskaya','antonova','pushkina','lermontovskiy pr.','gadjieva']
f = ['msu', 'mipt', 'bmstu', 'mspu','mitht']
g = ['lamborgini','ford','geely','mitsubishi','lada','mercedes']
h = ['russia','usa','china','japan','ukraine','france']
ii = ['red','blue','green','white','black']

def f1():
    
    for i in range (15):
        ew = ''

        for i in range (randint(1,3)):
            ew += str(choice(f)) + ", "
            
        print('student(fn("',choice(a),'","',choice(b),'"), ag(', randint(17,25), '), ph("+791',randint(1111111,67732232),
          '"), ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), ["', ew[:-2] ,'"]).',sep='')

        ew = ''

        for i in range (randint(1,3)):
            ew += str(choice(f)) + ", "
            
        print('student(fn("',choice(c),'","',choice(d),'"), ag(', randint(17,25), '), ph("+791',randint(1111111,67732232),
          '"), ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), ["', ew[:-2] ,'"]).',sep='')

def f2():
    
    for i in range (5):
        ew = ''

        for i in range (randint(1,3)):
            ew += str(choice(f)) + ", "
            
        print('student(fn("',choice(a),'","',choice(b),'"), ag(', randint(17,25), '), ph("+791',randint(1111111,67732232),
          '"), ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), uni("', choice(f) ,'")).',sep='')

        ew = ''

        for i in range (randint(1,3)):
            ew += str(choice(f)) + ", "
            
        print('student(fn("',choice(c),'","',choice(d),'"), ag(', randint(17,25), '), ph("+791',randint(1111111,67732232),
          '"), ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), uni("', choice(f) ,'")).',sep='')

def f4():
    
    for i in range (25):
            
        print('car(n("',choice(g),'"), ag(', randint(1,25), '), cl("',choice(ii),'"), c(', randint(100000,5000000),
              '), cn("', choice(h) ,'"), ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),')).',sep='')

      
def f3():
    
    for i in range (5):
            
        print('student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("',choice(a),'","',choice(b),'"), Age = ag(', randint(17,25), '), Ph_number = ph("+791',
              randint(1111111,67732232), '"), Addr = ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), Uni = uni("', choice(f) ,'")).',sep='')

        print('student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("',choice(c),'","',choice(d),'"), Age = ag(', randint(17,25), '), Ph_number = ph("+791',
              randint(1111111,67732232), '"), Addr = ad("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),'), Uni = uni("', choice(f) ,'")).',sep='')

f4()
