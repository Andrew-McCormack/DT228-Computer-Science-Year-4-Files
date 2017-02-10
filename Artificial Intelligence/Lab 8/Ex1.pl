increment(X, Y) :- Y is X + 1.

signum(X, Y) :- Y is X - 1, X > 0; Y is 0.

max_two_numbers(X, Y, Z) :- X > Y, Z is X; 
							Y > X, Z is Y. 

max_three_numbers(X, Y, Z, W) :- X > Y, X > Z, W is X; 
								 Y > X, Y > Z, W is Y;
								 Z > X, Z > Y, W is Z.

absolute(X, Y) :- Y is abs(X).

fact(0, 1).

fact(X, Y) :- X > 0, NextVal is X - 1, 
			fact(NextVal, RecursiveVal), 
			Y is RecursiveVal * X.

%fib(1, 1) :- !.
%fib(0, 0) :- !.


%fib(X, Y) :- X > 1,
%			NextX is X - 1,
%			NextNextX is X - 2,
%			fib(NextX, Fib1),
%			fib(NextNextX, Fib2),
%			Y is Fib1 + Fib2.

:- dynamic(fib/2).  % Not ISO, but works in SWI, YAP and GNU unlike the ISO declaration.
fib(1, 1) :- !.
fib(0, 0) :- !.
fib(N, Value) :-
  A is N - 1, fib(A, A1),
  B is N - 2, fib(B, B1),
  Value is A1 + B1,
  asserta((fib(N, Value) :- !)).


ack(0, Y, Z) :- Z is Y + 1.

ack(X, 0, Z) :- X > 0, X2 is X - 1,
				ack(X2, 1, Z).

ack(X, Y, Z) :- X > 0, Y > 0,
				X2 is X - 1, Y2 is Y - 1,
				ack(X, Y2, Z2), ack(X2, Z2, Z).


min(X, Y, X) :- X =< Y.
min(X, Y, Y) :- Y =< X.

gcd(X, 0, X) :- X > 0.
gcd(X, Y, GCD) :- Z is mod(X, Y), gcd(Y, Z, GCD). 
