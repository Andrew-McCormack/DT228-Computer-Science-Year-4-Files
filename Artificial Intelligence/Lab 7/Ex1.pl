last_element([H|[]], H) :- !.
last_element([H|T], Last) :- last_element(T, Last).

second_last([H|[H2|[]]], H) :- !.
second_last([H|T], SecondLast) :- second_last(T, SecondLast).

element_in_list([H|T], 1, H) :- !.
element_in_list([H|T], N, Val) :- NewN is N - 1, 
									element_in_list(T, NewN, Val). 

num_elements_in_list([], 0).
num_elements_in_list([H|T], Count) :- num_elements_in_list(T, Count2), 
										Count is Count2 + 1.

%append([H1|[]], [H1|[]]).
%append([H|T], [H|T]) :- append(T, L).
%append([H1|T1], [H2|T2], L) :- append(T1, L1), append(T2, L2),
					%			L is L1 + L2.
%append([H1|T1], L) :- append(T1, L2), L is L2 + H1.
%append([H1|T1], [H2|T2], [_|T3]) :- append(T1, L1), 
%									append(T2, L2).

append([], X, X).
append([X|Y], Z, [X|W]) :- append(Y, Z, W).

%reverse([H|[]], [H|[]]).
%reverse([H|T], [List|H]) :- reverse(T, List).

reverse([], []).
reverse([H|T], List) :- reverse(T, CloneList), append(CloneList, [H], List).


reverse2(X, Xrev) :- reverse3(X, [], Rev).

reverse3([], Rev, Rev).     % Nothing left to reverse.
reverse3([H|T], Prev, Rev) :- reverse3(T, [H|Prev], Rev).

accRev([H|T], R, A) :- accRev(T, R, [H|A]).
accRev([], A, A).
rev(L, R) :- accRev(L, R, []).


length2(L, N) :- length3(L, 0, N).
length3([], N, N).
length3([H|T], L, N) :- L1 is L + 1,
						length3(T, L1, N).

lengthWithoutAcc([], 0).
lengthWithoutAcc([H|T], N) :-  lengthWithoutAcc(T, N2), 
								N is N2 + 1.

palindrome1(L) :- rev(L, R), palindrome2(L,R).
palindrome2([], []).
palindrome2([H|T1], [H|T2]) :- palindrome2(T1, T2). 

toptail([X, Y, Z|[]], [Y]).
toptail([H|Tail], T) :- toptail(Tail, T).

