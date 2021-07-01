domains 

list = integer*.

predicates

more_than(list, integer length, list new_list).
odd_elems(list, integer index, list new_list).
delete_elem(list, integer elem, list new_list).
get_set(list, list).
clauses

more_than([], _, []) :- !.
more_than([Head|Tail], Number, New_List) :- Head > Number, 
			more_than(Tail, Number, List_), New_List = [Head|List_].
more_than([Head|Tail], Number, New_List) :- Head <= Number, 
			more_than(Tail, Number, New_List).

odd_elems([], _, []) :- !.
odd_elems([Head|Tail], Index, New_List) :- Index mod 2 = 1, Next_Index = Index + 1, 
			odd_elems(Tail, Next_Index, List_), New_list = [Head|List_].
odd_elems([_|Tail], Index, New_List) :- Index mod 2 = 0, Next_Index = Index + 1, 
			odd_elems(Tail, Next_Index, New_List).
			
delete_elem([], _, []) :- !.
delete_elem([Head|Tail], Elem, New_List) :- Elem <> Head, 
			delete_elem(Tail, Elem, List_), New_List = [Head|List_].
delete_elem([Head|Tail], Elem, New_List) :- Elem = Head, 
			delete_elem(Tail, Elem, New_List).				 

get_set([], []) :- !.
get_set([Head|Tail], Set) :- delete_elem(Tail, Head, New_List),
			get_set(New_List, Set_),Set = [Head|Set_].
goal

%list with elems that are more than
more_than([5,312,1,2,3,2,1,1,6], 1, Result).

%Result=[5,312,2,3,2,6]
%1 Solution


%list with odd elems
odd_elems([1,2,3,4,5,6,7,8,9,10],0, Result).

%Result=[2,4,6,8,10]
%1 SolutionNew_ListNew_List


%delete all entries
delete_elem([1,2,3,4,1,1],1, Result).

%Result=[2,3,4]
%1 Solution


%get a set from list
get_set([1,1,1,1,2,3,3,3,3,2,2,2,2,1], Result).

























%Result=[1,2,3]
%1 Solution