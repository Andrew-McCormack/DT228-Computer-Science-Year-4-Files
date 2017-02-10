check_equal(X, Y) :- =(X, Y).

all_as([H|T]) :- check_equal(a, H), check_equal([], T).
all_as([H|T]) :- all_as(T).