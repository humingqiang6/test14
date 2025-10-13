% База фактов о семье

% Предикат 'parent(Parent, Child)' означает, что Parent - родитель Child
parent(иван, мария).
parent(иван, алексей).
parent(ольга, мария).
parent(ольга, алексей).
parent(алексей, дмитрий).
parent(алексей, анастасия).
parent(мария, екатерина).

% Предикат 'male(Person)' указывает, что Person - мужчина
male(иван).
male(алексей).
male(дмитрий).

% Предикат 'female(Person)' указывает, что Person - женщина
female(ольга).
female(мария).
female(анастасия).
female(екатерина).

% Правило 'father(Father, Child)' - отец
father(Father, Child) :- parent(Father, Child), male(Father).

% Правило 'mother(Mother, Child)' - мать
mother(Mother, Child) :- parent(Mother, Child), female(Mother).

% Правило 'grandparent(Grandparent, Grandchild)' - бабушка/дедушка
grandparent(Grandparent, Grandchild) :- parent(Grandparent, Parent), parent(Parent, Grandchild).

% Правило 'sibling(Person1, Person2)' - брат или сестра
sibling(Person1, Person2) :- parent(Parent, Person1), parent(Parent, Person2), Person1 \= Person2.

% Правило 'uncle(Uncle, Person)' - дядя
uncle(Uncle, Person) :- parent(Parent, Person), sibling(Uncle, Parent), male(Uncle).