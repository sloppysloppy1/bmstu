domains

name = fn(string, string)
age = ag(integer)
addr = ad(string, integer, integer)
ph_number = ph(string)
university = uni(string)

predicates

student(name, age, ph_number, addr, university)

clauses

student(fn("sveta","olova"), ag(25), ph("+79113489439"), ad("lermontovskiy pr.", 1, 547), uni("mitht")).
student(fn("oleg","toporov"), ag(18), ph("+79152627919"), ad("pushkina", 21, 460), uni("mitht")).
student(fn("zhenya","zayceva"), ag(18), ph("+79156679781"), ad("lermontovskiy pr.", 50, 509), uni("msu")).
student(fn("anton","toporov"), ag(19), ph("+79127622503"), ad("varshavshkoe sh.", 12, 579), uni("msu")).
student(fn("masha","klyuge"), ag(23), ph("+79142605589"), ad("gadjieva", 76, 577), uni("bmstu")).
student(fn("nikita","konev"), ag(22), ph("+79118703495"), ad("varshavshkoe sh.", 47, 512), uni("mitht")).
student(fn("olga","toporova"), ag(24), ph("+7912872742"), ad("gadjieva", 93, 431), uni("bmstu")).
student(fn("vasya","nikitin"), ag(20), ph("+79165712450"), ad("gadjieva", 73, 470), uni("mspu")).
student(fn("lena","toporova"), ag(19), ph("+79163421536"), ad("pushkina", 11, 277), uni("bmstu")).
student(fn("kirill","olov"), ag(23), ph("+79162514175"), ad("solomonova", 1, 1184), uni("mipt")).

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