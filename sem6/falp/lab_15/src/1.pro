domains

addr = ad(symbol town, symbol street, integer building, integer appartment)
property = building(symbol name, integer cost, addr);	
	   place(symbol name, integer cost, addr, string date);
	   transport(symbol name, integer cost, string date);
	   car(symbol brand, symbol color, integer cost, integer year, symbol town)

predicates

person(symbol l_name, symbol ph_number, addr, property)
get_property(symbol name, symbol property, integer cost)
get_building_cost(symbol name, integer cost) 
get_place_cost(symbol name, integer cost) 
get_car_cost(symbol name, integer cost) 
get_transport_cost(symbol name, integer cost) 
get_sum(symbol name, integer sum)

clauses

person(klyuge, "+7912571026", ad("volgograd", "varshavshkoe sh.", 52, 83), 
	building(barn, 3213124, ad("volgograd", "varshavshkoe sh.", 11, 1))).
person(toporova, "+79165072034", ad("saint-petersburg", "varshavshkoe sh.", 11, 158), 
	building(shed, 123124, ad("saint-petersburg", "varshavshkoe sh.", 11, 17))).
person(klyuge, "+7912571026", ad("volgograd", "varshavshkoe sh.", 52, 83), 
	place(appartment, 12312312, ad("volgograd", "varshavshkoe sh.", 52, 83), "11.11.1999")).
person(zayceva, "+79138767153", ad("kasimov", "lermontovskiy pr.", 83, 578), 
	car("geely", "white", 6409914, 2015, "kasimov")).
person(nikitin, "+7913336524", ad("kiev", "pushkina", 86, 973), 
	car("geely", "black", 58439837, 2011, "ryazan")).
person(klyuge, "+7912571026", ad("volgograd", "varshavshkoe sh.", 52, 83), 
	transport("water_bike", 213124, "21.11.2007")).
person(toporova, "+79165072034", ad("saint-petersburg", "varshavshkoe sh.", 33, 45), 
	car("mitsubishi", "green", 12836628, 2018, "saint-petersburg")).

get_property(X, Y, Z) :- person(X, _, _, building (Y,Z,_)).
get_property(X, Y, Z) :- person(X, _, _, place (Y,Z,_,_)).
get_property(X, Y, Z) :- person(X, _, _, car(Y,_,Z,_,_)).
get_property(X, Y, Z) :- person(X, _, _, transport(Y,Z,_)).

get_building_cost(X, Y) :- person(X, _, _, building (_,Y,_)), !.
get_building_cost(_, 0).

get_place_cost(X, Y) :- person(X, _, _, place (_,Y,_,_)), !.
get_place_cost(_, 0).

get_car_cost(X, Y) :- person(X, _, _, car(_,_,Y,_,_)), !.
get_car_cost(_, 0).

get_transport_cost(X, Y) :- person(X, _, _, transport(_,Y,_)), !.
get_transport_cost(_, 0).

get_sum(X, Sum) :- get_building_cost(X, A), get_place_cost(X, B),
			get_car_cost(X, C), get_transport_cost(X, D),
			Sum = A + B + C + D.

goal

%property
get_property(Name, Property, _), Name = klyuge.

%Name=klyuge, Property=barn
%Name=klyuge, Property=appartment
%Name=klyuge, Property=water_bike
%3 Solutions

%property & cost
get_property(Name, Property, Cost), Name = klyuge.

%Name=klyuge, Property=barn, Cost=3213124
%Name=klyuge, Property=appartment, Cost=12312312
%Name=klyuge, Property=water_bike, Cost=213124
%3 Solutions

%sum of cost
get_sum(klyuge, Sum).

%Sum=15738560
%1 Solution