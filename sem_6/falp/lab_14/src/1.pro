domains

addr = ad(symbol town, symbol street, integer building, integer appartment)

predicates

person(symbol l_name, symbol ph_number, addr)
car(symbol owner_lname, symbol brand, symbol color, integer cost, integer year, symbol town)
bank_client(symbol client_lname, symbol bank_name, symbol type, integer amount_of_money, integer behaviour, symbol town)

get_stuff(symbol car_color, symbol car_brand, symbol lname, symbol town, symbol ph_num, symbol bank)

clauses

person("klyuge", "+7912571026", ad("volgograd", "varshavshkoe sh.", 52, 83)).
person("toporova", "+79165072034", ad("saint-petersburg", "varshavshkoe sh.", 100, 1151)).
person("zayceva", "+79138767153", ad("kasimov", "lermontovskiy pr.", 83, 578)).
person("mishkina", "+79165329056", ad("moscow", "antonova", 53, 1294)).
person("klyuge", "+79127675454", ad("moscow", "venevskaya", 85, 947)).
person("nikitin", "+7913336524", ad("kiev", "pushkina", 86, 973)).
person("nikitin", "+79146106984", ad("ryazan", "varshavshkoe sh.", 72, 27)).
person("toporov", "+7913733594", ad("saint-petersburg", "varshavshkoe sh.", 47, 1321)).
person("zaycev", "+7912486657", ad("volgograd", "lermontovskiy pr.", 86, 668)).
person("mishkin", "+79154045900", ad("kiev", "pushkina", 25, 278)).

car("zayceva", "geely", "white", 6409914, 2015, "kasimov").
car("nikitin", "mitsubishi", "green", 42502483, 2011, "ryazan").
car("klyuge", "mercedes", "blue", 19367655, 2013, "moscow").
car("toporov", "geely", "black", 59107666, 2011, "saint-petersburg").
car("toporova", "mitsubishi", "green", 12836628, 2018, "saint-petersburg").
car("mishkin", "mercedes", "black", 33637427, 2015, "kiev").
car("mishkin", "mitsubishi", "green", 3009291, 2011, "kiev").
car("zayceva", "ford", "blue", 36681813, 2012, "kasimov").
car("nikitin", "geely", "black", 58439837, 2011, "ryazan").
car("zaycev", "geely", "blue", 61712885, 2011, "kiev").

bank_client("mishkina", "tinkoff", "payment", 2439027, 8, "moscow").
bank_client("konev", "sberbank", "payment", 63838628, 4, "kasimov").
bank_client("toporova", "tinkoff", "savings", 60815175, 9, "saint-petersburg").
bank_client("klyuge", "tinkoff", "savings", 1768099, 9, "moscow").
bank_client("zayceva", "tinkoff", "savings", 53406609, 0, "kasimov").
bank_client("nikitin", "alphabank", "savings", 14555497, 8, "kiev").
bank_client("klyuge", "tinkoff", "credit", 34218309, -1, "volgograd").
bank_client("toporova", "sberbank", "credit", 37214889, 10, "saint-petersburg").
bank_client("toporova", "sberbank", "savings", 51895925, 10, "saint-petersburg").
bank_client("nikitin", "sberbank", "payment", 3318136, 8, "toporova").
	
get_stuff(Car_color, Car_brand, Lname, Town, Ph_num, Bank) :- car(Lname, Car_brand, Car_color, _, _, Town),
		person(Lname, Ph_num, ad(Town, _, _, _)), 
		bank_client(Lname, Bank, _, _, _, Town).

goal

%last name, town, ph number, bank
get_stuff(Car_color, Car_brand, Lname, Town, Ph_num, Bank), Car_brand = "mitsubishi", Car_color = "green", nl.
%
%Car_color=green, Car_brand=mitsubishi, Lname=toporova, Town=saint-petersburg, Ph_num=+79165072034, Bank=tinkoff
%Car_color=green, Car_brand=mitsubishi, Lname=toporova, Town=saint-petersburg, Ph_num=+79165072034, Bank=sberbank
%Car_color=green, Car_brand=mitsubishi, Lname=toporova, Town=saint-petersburg, Ph_num=+79165072034, Bank=sberbank
%3 Solutions
