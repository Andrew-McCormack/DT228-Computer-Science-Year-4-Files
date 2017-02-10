father(albert,james).
father(james,harry).
mother(ruth,james).
mother(lili,harry).

wizard(lili).
wizard(ruth).
wizard(albert).
wizard(X) :- 
	father(Y,X),
	wizard(Y),
	mother(Z,X),
	wizard(Z).
