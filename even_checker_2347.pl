% Prolog predicate to check if a number is even
% Usage: even(N) where N is an integer.
% Example queries:
% ?- even(4). -> true.
% ?- even(5). -> false.

even(N) :-
    N mod 2 =:= 0.