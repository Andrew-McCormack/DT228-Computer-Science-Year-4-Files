wizard(harry).
wizard(ron).

mudblood(hagrid).
muggle(dudley).

death-eater(voldemort).
death-eater(lucius).

kills(X, Y) :- death-eater(X), wizard(Y).
stuns(X, Y) :- wizard(X), death-eater(Y).

room(kitchen).
room(office).
room(hall).
room('dining room').
room(cellar).

happy(X) :- wizard(X), death-eater(Y), stuns(X, Y).

loves(vincent, mia). 
loves(marsellus, mia). 
loves(pumpkin, honey_bunny). 
loves(honey_bunny, pumpkin).
jealous(X,Y) :- loves(X,Z), loves(Y,Z). 

sits_right_of(ron, natalie).
sits_right_of(hermione, ron).
sits_right_of(harry, hermione).
sits_right_of(colin, harry).
sits_right_of(seamus, colin).
sits_right_of(angelina, seamus).
sits_right_of(ginny, angelina).
sits_right_of(dean, ginny).
sits_right_of(dennis, dean).
sits_right_of(lee, dennis).
sits_right_of(george, lee).
sits_right_of(fred, george).
sits_right_of(alicia, fred).
sits_right_of(neville, alicia).
sits_right_of(lavender, neville).
sits_right_of(parvati, lavender).
sits_right_of(katie, parvati).
sits_right_of(natalie, katie).

sits_left_of(X, Y) :- sits_right_of(Y, X).

are_neighbours_of(X, Y, Z) :- sits_right_of(Z, Y), sits_left_of(X, Y).

next_to_each_other(X, Y) :- sits_right_of(Y, X) ; sits_left_of(Y, X).


male(paul).
male(albert).
male(vernon).
male(james).
male(dudley).
male(harry).

female(helen).
female(ruth).
female(petunia).
female(lili).

parent_of(paul, petunia).
parent_of(helen, petunia).
parent_of(paul, lili).
parent_of(helen, lili).
parent_of(albert, james).
parent_of(ruth, james).
parent_of(vernon, dudley).
parent_of(petunia, dudley).
parent_of(lili, harry).
parent_of(james, harry).

father_of(paul, petunia).
father_of(paul, lili).
father_of(albert, james).
father_of(vernon, dudley).
father_of(james, harry).

mother_of(helen, petunia).
mother_of(helen, lili).
mother_of(ruth,  james).
mother_of(petunia, dudley).
mother_of(harry, lili).