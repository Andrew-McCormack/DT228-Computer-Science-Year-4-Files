%% The list is empty. So, all_as succeeds.

all_as([]).

%% The first element of the list is an a. So, we check whether the
%% rest of the list is also a list containing only a's.

all_as([a|Tail]) :- all_as(Tail).