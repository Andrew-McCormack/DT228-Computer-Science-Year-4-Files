/*
	Lab 3 Prolog Test Practice Excercise
	Andrew McCormack
	C13569113
*/

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
mother_of(ruth, james).
mother_of(petunia, dudley).
mother_of(lili, harry).

grandfather_of(paul, dudley).
grandfather_of(paul, harry).
grandfather_of(albert, harry).

grandmother_of(helen, dudley).
grandmother_of(helen, harry).
grandmother_of(ruth, harry).

sister_of(petunia, lily).
sister_of(lily, petunia).

aunt_of(lili,dudley).
aunt_of(petunia, harry).

uncle_of(james, dudley).
uncle_of(vernon, harry).