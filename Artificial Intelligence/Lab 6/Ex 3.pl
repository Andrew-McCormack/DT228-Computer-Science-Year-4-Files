del(X, [X|T], T).

del(X, [H1|T1], [H2|T2]) :- del(X, T1, T2).