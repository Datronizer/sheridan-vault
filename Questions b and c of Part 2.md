Suppose that graph G has the following adjacency lists:
a → (b,10)→(c,5)→(d,4)→NULL
b → (a,15)→(c,10)→(d,12)→NULL
c → (a,2)→(b,5)→(d,8)→NULL
d → (a,5)→(b,7)→(c,9)→(f,11)→NULL
e → (f,3)→(g,10)→(h,8)→NULL
f → (d,11)→(d,3)→(e,5)→(g,9)→NULL
g → (e,5)→(g,8)→(h,12)→NULL
h → (e,2)→(g,5)→NULL

For the following questions, I will use capital letters (A-H) to denote the question's (a-h). This is for readability as the letter `a` can be mistaken for the article "a" in English.

# b. Give the sequence of vertices visited using depth-first search starting at vertex 1.
1) Start from A
2) Go to B and mark B (C and D are on hold). 
	1) *NOTE: Similarly for all future nodes, upon entering, the node will be marked*
3) From B:
	1) A is marked so we skip
	2) Go to C (D is on hold)
4) From C:
	1) A is marked so we skip
	2) B is marked so we skip
	3) Go to D
5) From D:
	1) A is marked so we skip
	2) B is marked so we skip
	3) C is marked so we skip
	4) Go to F
6) From F:
	1) D is marked so we skip
	2) D is marked so we skip, again
	3) Go to E (G is on hold)
7) From E:
	1) F is marked so we skip
	2) Go to G (H is on hold)
8) From G:
	1) E is marked so we skip
	2) G is marked so we skip
	3) Go to H
9) From H:
	1) E is marked so we skip
	2) G is marked so we skip
	3) We've reached the end. Backtrack to G.
10) From G:
	1) We've visited all nodes. Backtrack to E.
11) From E:
	1) Release H from hold
	2) H is marked so we skip
	3) We've visited all nodes. Backtrack to F.
12) From F:
	1) Release G from hold
	2) G is marked so we skip
	3) We've visited all nodes. Backtrack to D.
13) From D:
	1) We've visited all nodes. Backtrack to C.
14) From C:
	1) We've visited all nodes. Backtrack to B.
15) From B:
	1) Release D from hold
	2) D is marked so we skip
	3) We've visited all nodes. Backtrack to A.
16) From A:
	1) We've visited all nodes. Terminate.

**Final traversal sequence: A → B → C → D → F → E → G → H**


# c. Give the sequence of vertices visited using breadth-first search starting at vertex 1

We will visit every node of each key, in the order that they appear in the linked list. Then we go to the next key, and do it again, skipping any node we visited previously.
1. Start from A, mark A
	1. Visit B, mark B
	2. Visit C, mark C,
	3. Visit D, mark D
2. Go to B. From B:
	1. Do nothing: A, C, D are already visited.
3. Go to C. From C:
	1. Do nothing: A, B, D are already visited.
4. Go to D. From D:
	1. Skip A, B, C.
	2. Visit F and mark F.
5. Go to F. From F:
	1. Skip D.
	2. Visit E and mark E
	3. Visit G and mark G
6. Go to E. From E:
	1. Skip F, G
	2. Visit H and mark H
7. Go to G. From G:
	1. Do nothing: E, G, H are already visited.
8. Go to H. From H:
	1. Do nothing: E, G are already visited. 
	2. Terminate.

**Final traversal sequence: A → B → C → D → F → E → G → H**