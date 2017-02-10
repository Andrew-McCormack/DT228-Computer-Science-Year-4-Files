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

