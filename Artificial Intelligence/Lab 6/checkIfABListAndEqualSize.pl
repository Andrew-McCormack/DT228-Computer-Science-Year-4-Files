a_b_and_equal_list([], []).

a_b_and_equal_list([a|T1], [b|T2]) :- equal_list(T1, T2).