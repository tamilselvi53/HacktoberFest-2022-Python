## Hacktober Fest 2022 - Hacktoberfest2022
### Doubly Linked List in Python

#### Problem Statement
Maximum flow problems involve finding a feasible flow through a single-source, single-sink flow network that is maximum.

Find max flow in given weighted directed acyclic graph and return the total bottle-neck capacity.

#### Input Format
Make a function that accepts two integers denoting **E** and **V** as arguments.

Next, it will take the graph of **E** edge s in the form of adjacency list. The format of adjacency list is in such a way, each input denotes that there is an outward edge from given to other nodes in the graph at that level.

Make a function to accept Source **S** and Sink **D** as arguments.

#### Output Format
Print the maximum number of badges that can be made.

#### Sample Input
```
Total Vertices = 7
Total Edges = 12
graph = {
    A: [B, 7],
    A: [C, 10],
    B: [C, 1],
    B: [D, 3],
    B: [E, 5],
    C: [D, 2],
    C: [F, 7],
    D: [E, 3],
    D: [F, 2],
    E: [F, 2],
    E: [G, 10],
    F: [G, 4]
}
Source = A
Sink = G
```

#### Sample Output
```
12
```

#### Explanation
- First flow is ```A -> B -> E -> G = 5```.
- Second flow is ```A -> C -> F -> G = 4```.
- Third flow is ```A -> B -> D -> E -> G = 2```.
- Last flow is ```A -> C -> D -> E -> G = 1```.
- Therefore, maximum flow will be ``` 5 + 4 + 2 + 1 = 12```.

## How to Contribute
Please read the [CONTRIBUTING.md](../../CONTRIBUTING.md)

## Rules
- Put your solution in a solution.py file inside the folder of the problem.
- The function should take the input as specified in the problem statement.
- The function should return the output as specified in the problem statement.
- Follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Do not make any changes to the README.md file.
- If there is not any pull request for a problem, you can create a pull request for that problem.
- If there is already a pull request for a problem, you can create a pull request for that problem only if the pull request is not merged.
- Alternative solutions are not allowed.
- Pull requests will be merged on a first come first serve basis.
- Pull requests that do not follow the rules will not be merged.
- Please do not spam pull requests.
- Please read the [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md)

## Acknowledgments
- [Python](https://www.python.org/)
- [Hacktoberfest](https://hacktoberfest.digitalocean.com/)
- [GitHub](https://github.com)
- [Git](https://git-scm.com/)

## Maintainer
- [Anamaya](https://www.linkedin.com/in/anamaya1729/)
- [Kartik](https://github.com/kartik007007)
- [Shantanu](https://github.com/neutralWire)
- [Shailesh](https://github.com/ShaileshKumar007)

## License
**This project is licensed under the GNU GENERAL PUBLIC License - see the [LICENSE](../../LICENSE) file for details**

## Happy Coding! :smile: :tada:
