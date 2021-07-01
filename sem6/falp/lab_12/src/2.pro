domains

name = fn(string, string)
age = ag(integer)
addr = ad(string, integer, integer)
ph_number = ph(string)
university = uni(string)

predicates

student(name, age, ph_number, addr, university)

clauses

student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("zhenya","koneva"), Age = ag(22), Ph_number = ph("+79121873110"), Addr = ad("solomonova", 77, 925), Uni = uni("msu").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("anton","konev"), Age = ag(25), Ph_number = ph("+79150356221"), Addr = ad("pushkina", 92, 5), Uni = uni("msu").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("olga","koneva"), Age = ag(24), Ph_number = ph("+79115405457"), Addr = ad("varshavshkoe sh.", 75, 941), Uni = uni("mspu").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("nikita","toporov"), Age = ag(21), Ph_number = ph("+79160795949"), Addr = ad("gadjieva", 41, 77), Uni = uni("mipt").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("lena","olova"), Age = ag(18), Ph_number = ph("+79131615329"), Addr = ad("gadjieva", 64, 434), Uni = uni("bmstu").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("kirill","toporov"), Age = ag(25), Ph_number = ph("+79121671399"), Addr = ad("solomonova", 11, 921), Uni = uni("mipt").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("sveta","mishkina"), Age = ag(24), Ph_number = ph("+79120877442"), Addr = ad("lermontovskiy pr.", 42, 424), Uni = uni("mipt").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("nikita","konev"), Age = ag(20), Ph_number = ph("+79126893010"), Addr = ad("venevskaya", 68, 697), Uni = uni("mipt").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("nastya","klyuge"), Age = ag(25), Ph_number = ph("+7911822975"), Addr = ad("varshavshkoe sh.", 92, 1122), Uni = uni("mitht").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("kirill","mishkin"), Age = ag(19), Ph_number = ph("+79135139940"), Addr = ad("pushkina", 39, 374), Uni = uni("mspu").
student(F_name, Age, Ph_number, Addr, Uni) :- F_name = fn("lena","klyuge"), Age = ag(19), Ph_number = ph("+79135308016"), Addr = ad("solomonova", 9, 350), Uni = uni("mipt").	


goal 

%students from the same uni
student(Name,_,Phone,_,uni("bmstu")), nl.
student(Name,_,Phone,_,uni("msu")), nl.
student(Name,_,Phone,_,uni("mitht")), nl.
student(Name,_,Phone,_,uni("mipt")), nl.

%students older than 18
student(Name,ag(Age),Phone,_,_), Age > 18, nl.

%students named lena
student(fn(Name,Lastname),_,Phone,_,_), Name = "lena", nl.

%students from varshavshkoe sh.
student(Name,_,Phone,ad(Street,_,_),_), Street = "varshavshkoe sh.", nl.