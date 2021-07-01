predicates

max_of_two(integer max, integer num1, integer num2)
max_of_three(integer max, integer num1, integer num2, integer num3)

clauses

%without
%max_of_two(A, B, C) :- C >= B, A = C.
%max_of_two(A, B, C) :- B > C, A = B.

%with
max_of_two(A, B, C) :- C >= B, A = C, !.
max_of_two(A, B, C) :- B >= C, A = B.


%without
%max_of_three(A, B, C, D) :- C > D, C >= B, A = C.
%max_of_three(A, B, C, D) :- B >= D, B > C, A = B.
%max_of_three(A, B, C, D) :- D >= B, D >= C, A = D.

%without
max_of_three(A, B, C, D) :- C >= D, C >= B, A = C, !.
max_of_three(A, B, C, D) :- B >= D, B > C, A = B, !.
max_of_three(A, B, C, D) :- D >= B, D >= C, A = D.

goal

max_of_three(A, 1, 7, 7). 


