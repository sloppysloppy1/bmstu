domains 

list = integer*.

predicates

len(list, integer length).
sum(list, integer sum).
odd_sum(list, integer sum, integer index).

clauses

len([], 0) :- !.
len([_|Tail], Length) :- len(Tail, Tail_Length), Length = Tail_Length + 1.

sum([], 0) :- !.
sum([Head|Tail], Sum) :- sum(Tail, Sum_), Sum = Sum_ + Head.

odd_sum([], 0, _) :- !.
odd_sum([Head|Tail], Sum, Index) :- Index mod 2 = 1, Next_Index = Index + 1, 
			odd_sum(Tail, Sum_, Next_Index), Sum = Sum_ + Head.
odd_sum([_|Tail], Sum, Index) :- Index mod 2 = 0, Next_Index = Index + 1, 
			odd_sum(Tail, Sum, Next_Index).
				 

goal

len([1,21,3,4,5], Length).
%[1,21,3,4,5]
%sum of numbers
%sum([1,21,3,4,5], Sum).
%Sum=34
%1 Solution

%sum of odd
%odd_sum([1,21,3,4,5], Sum, 0).
%Sum=25
%1 Solution