replace_a_b_c([], []).

replace_a_b_c([a|T1], [b|T2]) :- replace_a_b_c(T1, T2).

replace_a_b_c([b|T1], [c|T2]) :- replace_a_b_c(T1, T2).

replace_a_b_c([c|T1], [a|T2]) :- replace_a_b_c(T1, T2).

replace_a_b_c([X|InTail],[X|OutTail]) :- X\=a, X\=b, X\= c,
              replace_a_b_c(InTail,OutTail).