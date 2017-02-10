/*
	Name: Andrew McCormack
	Student Number: C13569113
*/

haspart(worldhq, chinahq).
haspart(worldhq, irelandhq).
haspart(chinahq, chinasales).
haspart(chinahq, chinafinance).
haspart(irelandhq, irelandsales).
haspart(irelandhq, irelandfinance).

head(bob, worldhq).
head(zhi, chinahq).
head(marry, irelandhq).
head(hui, chinasales).
head(ya, chinafinance).
head(neil, irelandsales).
head(karen, irelandfinance).

employee(john, worldhq).
employee(wen, chinahq).
employee(brian, irelandhq).
employee(hong, chinasales).
employee(ming, chinafinance).
employee(michael, irelandsales).
employee(alan, irelandfinance).

indepartment(X, Y) :- head(X, Y); employee(X, Y).

colleagues(X, Y) :- indepartment(X, Z), indepartment(Y, Z), X\=Y.

component(X, Y) :- haspart(Y, X). 
component(X, Y) :- haspart(Z, X), component(Z, Y).

memberof(X, Y) :- head(X, Y); employee(X, Y).
memberof(X, Y) :- component(Z, Y), memberof(X, Z).

bossof(X, Y) :- memberof(X, Z), memberof(Y, V), head(X, Z), employee(Y, V), component(V, Z); colleagues(X, Y).