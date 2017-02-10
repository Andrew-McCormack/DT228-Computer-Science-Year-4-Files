wizard('Harry').
scares('Hagrid', 'Dudley').
magical(X) :- wizard(X).
hates(X, 'Uncle Vernon') :- magical(X).
hates(X, 'Aunt Petunia') :- magical(X).
hates(X, 'Aunt Petunia') :- scares(X, 'Dudley').