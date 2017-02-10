conc([], L, L).

conc([H|T], L2, [H|L3]) :- conc(T, L2, L3).

conc2([], L, L).

conc2([H|T], L2, [H|L3]) :- conc(T, L2, L3).

sublist(S, L) :- conc(L1, L2, L), conc2(S, L3, L2).