%%member/2 Solution

member(X,[X|Tail]).
member(X,[Head|Tail]):-member(X,Tail).

%%conc/3 Solution

conc([],L,L).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).

%%del/3 Solution

del(X,[X|Tail],Tail).
del(X,[Y|Tail],[Y|Tail1]):-del(X,Tail,Tail1).

%%sublist/2 Solution

sublist(S,L):-conc(L1,L2,L),conc(S,L3,L2).
