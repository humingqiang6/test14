% База фактов о семье

% Предикаты: parent(Родитель, Ребенок), male(Имя), female(Имя)
% Отношения: mother, father, sibling, grandparent и т.д. можно определить через правила.

% Мужчины
male(alex).
male(bob).
male(charlie).
male(david).

% Женщины
female(eve).
female(fiona).
female(grace).
female(helen).

% Родительские отношения
parent(alex, bob).    % alex - родитель bob
parent(alex, fiona).  % alex - родитель fiona
parent(eve, bob).     % eve - родитель bob
parent(eve, fiona).   % eve - родитель fiona
parent(bob, charlie). % bob - родитель charlie
parent(bob, grace).   % bob - родитель grace
parent(fiona, david). % fiona - родитель david
parent(fiona, helen). % fiona - родитель helen
