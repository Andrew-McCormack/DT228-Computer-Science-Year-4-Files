%% Harry is a wizard.
wizard(harry).

%% Hagrid scares dudley.
scare(hagrid,dudley).

%% All wizards are magical.
magical(X) :- wizard(Y).

%% Uncle Vernon hates everything that is magical.
hate(uncle_vernon,X) :- magical(X).

%% Aunt Petunia hates everything that is magical.
hate(aunt_petunia,X) :- magical(X).

%% Aunt Petunia hates anything that scares dudley.
hate(aunt_petunia,X) :- scare(X,dudley).
