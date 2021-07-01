predicates

max_of_two(integer max, integer num1, integer num2)
max_of_three(integer max, integer num1, integer num2, integer num3)

clauses

%without
max_of_two(A, B, C) :- C >= B, A = C.
max_of_two(A, B, C) :- B > C, A = B.

%with
max_of_two(A, B, C) :- C >= B, A = C, !.
max_of_two(A, B, C) :- B >= C, A = B.


%without
max_of_three(A, B, C, D) :- C > D, C >= B, A = C.
max_of_three(A, B, C, D) :- B >= D, B > C, A = B.
max_of_three(A, B, C, D) :- D >= B, D >= C, A = D.

%without
max_of_three(A, B, C, D) :- C >= D, C >= B, A = C, !.
max_of_three(A, B, C, D) :- B >= D, B > C, A = B, !.
max_of_three(A, B, C, D) :- D >= B, D >= C, A = D.

goal

%max of two
max_of_two(Max, 69, 228).

%Max=228
%1 Solution

%max of three
max_of_three(Max, 1, 7, 7). 

%Max=7
%1 Solution

