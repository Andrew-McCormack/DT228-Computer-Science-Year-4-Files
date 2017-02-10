member(X, [X| _]).

member(X, [H|T]) :- member(X, T).