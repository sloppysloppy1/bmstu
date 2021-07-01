from random import *

a = ['lena','olga','nastya','masha','galya','sveta','ira', 'zhenya']
b = ['klyuge','nikitina','olova','zayceva','koneva','toporova','mishkina']
c = ['oleg','anton','vasya','petya','nikita','zhenya', 'abdul','kirill']
d = ['klyuge','nikitin','olov','zaycev','konev','toporov','mishkin']
e = ['solomonova','varshavshkoe sh.','venevskaya','antonova','pushkina','lermontovskiy pr.','gadjieva']
f = ['moscow','saint-petersburg','kiev','volgograd','ryazan','kasimov','tula']
g = ['lamborgini','ford','geely','mitsubishi','lada','mercedes']
h = ['russia','usa','china','japan','ukraine','france']
ii = ['red','blue','green','white','black']
bb = ['sberbank','alphabank','tinkoff']
by = ['credit', 'payment', 'savings']

def f1():
    for i in range (5):
    # print('person(full_name("',choice(a),'","',choice(b),'"), phone_number("+791',randint(1111111,67732232), '"), address("', choice(e), '", ', randint(1,100),', ', randint (1, 1337),')).',sep='')
        print('person("',choice(d),'", "+791',randint(1111111,67732232),
          '", ad("', choice(f), '", "', choice(e), '", ', randint(1,100),', ', randint (1, 1337),')).',sep='')

def f4():
    
    for i in range (5):
            
        print('car("', choice(b),'", "', choice(g), '", "', choice(ii), '", ', randint(100000,67732232), ', ',
              randint(1995,2020),', "', choice(f),'")',sep='')

        print('car("', choice(d),'", "', choice(g), '", "', choice(ii), '", ', randint(100000,67732232), ', ',
              randint(1995,2020),', "', choice(f),'")',sep='')

def f5():
    
    for i in range (5):
            
        print('bank_client("',choice(b),'", "',choice(bb),'", "',choice(by),', ', randint(100000,67732232),', ', randint (-1, 10),', "', choice(f),'").',sep='')
        print('bank_client("',choice(d),'", "',choice(bb),'", "',choice(by),', ', randint(100000,67732232),', ', randint (-1, 10),', "', choice(f),'").',sep='')

f5()
