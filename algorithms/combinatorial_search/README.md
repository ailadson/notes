# Combinatorial Search

* Combinatorial search algorithms offers a set of techniques to find (1) all
possible solutions or (2) the best solution out of all possible solutions.

* For combinatorial problems, the search spaces are typically (1) so large that we must
employ a very systematic method of search to ensure that we don't miss any
possible solutions or repeat our work, or (2) too large to systematically search
for the best solution, so we must employ a heuristic to get a 'good-enough' solution

* Combinatorial search is a great option for NP-hard problems

* Wikipedia's definition of a combinatorial search problem is very good and
clear. It states that they "consists of finding an optimal object from a finite set of
objects. In many such problems, exhaustive search is not feasible."

* A few example problems:
  * All subsets or permutations
  * Bin packing
  * Traveling Salesman
  * Sudoku
  * 8-Queens


## Techniques

### Backtracking

* If your combinatorial search space is relatively small (~20 items, no more than 50)
and you need to find the optimal solution, backtracking is the approach you want
to take. It finds every possible solution in the search space

* Backtracking isn't really an algorithm so much as it is a way of structuring your
algorithm. The steps are:
  1. Determine how your solution space looks.
    * Remember, these problems are all about searching solution spaces for the
    optimal one. This may take some work, but typically its best to model the solution
    space a sequence
  2. Write a function that, given a partial solution, can construct a list of
  next possible steps to lead you to a complete solution. For example, if you
  were creating a sudoku solver, the partial solution would be an incomplete
  sudoku board. This function should return all eligible numbers that can go in t
  he next candidate square.
  3. Iterate over the candidate next steps that were created in the previous
  function. In each iteration, you will make the candidate move and then recurse into the
  backtracking algorithm with this new move (base case coming in the next step!).
  Finally, after the stack returns with the recursive call, unmake the move and move on
  to the next candidate solution
  4. Backtracking in recurive, so what's the base-case? Well, if we have a complete
  solution, then we should do something with it. This can be seeing if it's the
  optimal one, printing it out, collecting it, etc. Depends on your app.

 **~~~~~ Examples ~~~~~**

  - [8 Queens](./code/8_queens.py)
  - [All Paths in a Graph](./code/all_paths_in_graph.py)
  - [Sudoku Solver](./code/sudoku.py)
    - [Sudoku Tests](./code/test_sudoku.py)
    - [Sudoku Board](./code/sudoku_board.py)
  - [Permutations](./code/perms.py)
  - [Subsets](./code/subsets.py)


### Random Search

* Sounds like what is says. Keep creating random solutions until and hold on to
the optimal one. Repeat until your solution is good enough or you run out of time

* Great option when the solution space has many possible 'correct' or 'optimal'
solutions. Otherwise, pretty bad.

* Make sure that you are generating truly random solutions, aka, every possible
has an equal probability of being chosen

* No code examples yet

### Local Search

* Create a random solution first, then keep making incremental changes in all
possible 'directions' from the current solution. Maintain the optimal one. Repeat
until no more incremental solutions yield a better optimum.

* Great for finding local optimums, but shitty at finding global ones

### Simulated Annealing

* THIS IS SOOOO COOL. The algorithm is based on how metals cool down.

* Think about the energy of a really hot piece of metal. As it cools, its total
energy can be thought of as the sum of the energy it's particles. If we look at
the particles as the metal cools, we will notice that even though the energy
dissipates, there are sudden random spikes. The chance of a spike is greater when
the energy of the system is hotter. These random spikes start to subside as the
system grows cooler. So wtf does this have to do with combinatorial spaces?

* The algorithm is as follows:
  - Set your temperature to 100. The system starts off really hot
  - While your temperature is above some threshold OR your solution isn't good enough:
      - N times (in a for loop)
        - make an incremental change and find a new solution
        - if it's better than your current best, hold on to it OR
        - randomly decide to keep a worst solution. This should be a function of
        your temperature. See you wikipedia for the literature on making this randomness
      - decrease the temperature by some percentage (say 10%)

* This prevents you from getting stuck in a local optimum, increasing the chance
of finding the global optimum or at least a better local optimum.

* I haven't coded this up, but its so fucking cool I'll be sure to do so very soon

### n-choose-k problems

* A lot of combinatorial problems can be reduced to n-choose-k problems. That is,
problems like "if I have n items, how many ways can I choose n of them"

* To solve these, learn to compute [binomial coefficients](./binomial_coefficient.py)
