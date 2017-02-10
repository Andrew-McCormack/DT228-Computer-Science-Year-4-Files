%	Andrew McCormack
%	C13569113

connected(a,b,10).
connected(b,c,5).
connected(b,d,5).
connected(f,e,15).
connected(e,d,10).
connected(d,g,5).
connected(g,h,10).
connected(g,i,15).

% Q1 Part A, find out if path exists between 2 nodes
route(X, Y, [X,Y]) :- connected(X, Y, _).
route(X, Y, [X|Z]) :- connected(X, V, _), route(V, Y, Z). 


% Q2 Part B, find the distance between 2 nodes connected along a path
distance(X, Y, Z) :- connected(X, Y, Z).
distance(X, Y, Z) :- connected(X, V, Z1), 
					 distance(V, Y, Z2), 
					 Z is Z1 + Z2.

% Q2 
fn(X, 1) :- X < 0.
fn(X, 100) :- X >= 100.
fn(X, Y) :- X >= 0, X < 100,
			X2 is X + 1,
			fn(X2, Result),
			Y is X + Result.