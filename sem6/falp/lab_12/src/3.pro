domains

name = n(string) 
age = ag(integer) 
color = cl(string)
cost = c(integer)
country = cn(string)
shop_addr = ad(string,integer,integer)

predicates

car(name, age, color, cost, country, shop_addr)

clauses
car(n("geely"), ag(13), cl("green"), c(3046029), cn("japan"), ad("lermontovskiy pr.", 73, 1114)).
car(n("mitsubishi"), ag(14), cl("blue"), c(4062304), cn("japan"), ad("venevskaya", 72, 1120)).
car(n("mercedes"), ag(18), cl("white"), c(4121674), cn("ukraine"), ad("pushkina", 44, 680)).
car(n("mercedes"), ag(5), cl("blue"), c(578377), cn("russia"), ad("venevskaya", 4, 128)).
car(n("lamborgini"), ag(13), cl("blue"), c(3385131), cn("ukraine"), ad("lermontovskiy pr.", 2, 1259)).
car(n("lamborgini"), ag(6), cl("white"), c(3029382), cn("usa"), ad("lermontovskiy pr.", 41, 1285)).
car(n("ford"), ag(14), cl("red"), c(2470919), cn("france"), ad("pushkina", 99, 718)).
car(n("mitsubishi"), ag(13), cl("white"), c(152916), cn("france"), ad("antonova", 9, 1092)).
car(n("lamborgini"), ag(19), cl("red"), c(2839293), cn("france"), ad("varshavshkoe sh.", 18, 1270)).
car(n("geely"), ag(5), cl("green"), c(2984892), cn("usa"), ad("venevskaya", 35, 749)).
car(n("mercedes"), ag(2), cl("blue"), c(3883851), cn("usa"), ad("solomonova", 28, 440)).
car(n("mitsubishi"), ag(21), cl("blue"), c(3543981), cn("usa"), ad("solomonova", 40, 1277)).
car(n("geely"), ag(5), cl("green"), c(4314298), cn("china"), ad("antonova", 1, 616)).
car(n("mitsubishi"), ag(11), cl("white"), c(1938545), cn("russia"), ad("lermontovskiy pr.", 34, 782)).
car(n("lada"), ag(20), cl("red"), c(4607108), cn("usa"), ad("pushkina", 26, 348)).
car(n("geely"), ag(7), cl("red"), c(4257577), cn("japan"), ad("antonova", 16, 1083)).
car(n("lada"), ag(3), cl("blue"), c(1565904), cn("japan"), ad("solomonova", 76, 112)).
car(n("ford"), ag(3), cl("blue"), c(473209), cn("ukraine"), ad("lermontovskiy pr.", 35, 475)).
car(n("mitsubishi"), ag(21), cl("green"), c(780149), cn("usa"), ad("venevskaya", 48, 407)).
car(n("geely"), ag(14), cl("red"), c(1263246), cn("japan"), ad("pushkina", 27, 671)).
car(n("ford"), ag(3), cl("red"), c(2112563), cn("russia"), ad("gadjieva", 54, 1306)).
car(n("ford"), ag(23), cl("blue"), c(3342477), cn("russia"), ad("venevskaya", 38, 879)).
car(n("ford"), ag(2), cl("blue"), c(299402), cn("france"), ad("lermontovskiy pr.", 82, 882)).
car(n("lada"), ag(4), cl("white"), c(3238237), cn("ukraine"), ad("pushkina", 78, 314)).
car(n("mercedes"), ag(11), cl("blue"), c(4008621), cn("ukraine"), ad("gadjieva", 73, 633)).

goal 

%white cars
car(Name, _, cl("white"), _, Country, _), nl.
