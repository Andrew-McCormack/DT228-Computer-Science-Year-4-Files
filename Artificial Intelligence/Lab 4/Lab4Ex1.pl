male(paul).
male(albert).
male(vernon).
male(james).
male(dudley).
male(harry).
male(john).
male(fred).

female(helen).
female(ruth).
female(petunia).
female(lili).
female(jane).
female(mary).

parent_of(paul, petunia).
parent_of(helen, petunia).
parent_of(paul, lili).
parent_of(helen, lili).
parent_of(albert,  james).
parent_of(ruth, james).
parent_of(vernon, dudley).
parent_of(petunia, dudley).
parent_of(lili, harry).
parent_of(james, harry).
parent_of(john, albert).
parent_of(jane, albert).
parent_of(fred, ruth).
parent_of(mary, ruth).

different(X, X) :- !, fail.
different(X, Y) :- true.

father_of(X, Y) :- parent_of(X, Y), male(X).

mother_of(X, Y) :- parent_of(X, Y), female(X).

grandfather_of(X, Y) :- parent_of(Z, Y), parent_of(X, Z), male(X).

grandmother_of(X, Y) :- parent_of(Z, Y), parent_of(X, Z), female(X).

sister_of(X, Y) :- parent_of(Z, X), parent_of(Z, Y), female(X), different(X, Y).

aunt_of(X, Y) :- sister_of(Z, X), parent_of(Z, Y).

grandparent_of(X, Y) :- parent_of(X, Z), parent_of(Z, Y).

greatgrandparent_of(X, Y) :- parent_of(X, Z), parent_of(Z, A), parent_of(A, Y).

ancestor_of(X, Y) :- parent_of(X, Y).

ancestor_of(X, Y) :- parent_of(X, Z), ancestor_of(Z, Y). 