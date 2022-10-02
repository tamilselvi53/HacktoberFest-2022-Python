## Hacktober Fest 2022 - Hacktoberfest2022
### Dijkstra Algorithm in Python

#### Problem Statement
The Dijkstra algorithm is an algorithm that is used for finding the shortest distance, or path, from starting node to target node in a weighted graph.

Here You need to implement Dijkstra's Algorithm(Single Source Shortest Path Algorithm).

You will be given an adjacency list of an undirected graph with the destination/Source node and print the shortest path between the source node and all the other given nodes.

#### Input Format
Create a function that takes _adjacency list_ of a graph and a source vertex as arguments and returns a list of distances from the source to all other vertices in the given graph.

#### Output Format
Return the list of minimum distances between the source node and all the other nodes.

#### Sample Input
```
graph = {
    A: [[B, 4], [H, 8]],
    B: [[C, 8], [H, 11]],
    C: [[D, 7], [I, 2], [F, 4], [B, 8]],
    D: [[E, 9], [F, 14], [C, 7]],
    E: [[D, 9], [F, 10]],
    F: [[E, 10], [D, 14], [C, 4], [G, 2]],
    G: [[F, 2], [I, 6], [H, 1]],
    H: [[I, 7], [A, 8], [B, 11], [G, 1]]
    I: [[C, 2], [G, 6], [H, 7]]
}

source = A
```

#### Sample Output
```
[0, 4, 12, 19, 21, 11, 9, 8, 14]
```

#### Explanation
- The shortest path from source A to vertex B has weight 4 (A -> B)
- The shortest path from source A to vertex C has weight 12 (A -> B -> C)
- The shortest path from source A to vertex D has weight 19 (A -> B -> C -> D)
- The shortest path from source A to vertex E has weight 21 (A -> B -> C -> F -> E)
- The shortest path from source A to vertex F has weight 11 (A -> B -> C -> F)
- The shortest path from source A to vertex G has weight 9 (A -> H -> G)
- The shortest path from source A to vertex H has weight 8 (A -> H)
- The shortest path from source A to vertex I has weight 14 (A -> B -> C -> I)

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
