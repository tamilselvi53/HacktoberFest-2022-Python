## Hacktober Fest 2022 - Hacktoberfest2022
### Bellman Ford Algorithm in Python

#### Problem Statement
The Bellman-Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

#### Input Format
Create a function that takes adjacency list of a graph and a source vertex as arguments and returns a list of distances from the source to all other vertices in the given graph. If there is a negative weight cycle, then return -1.

#### Output Format
Return a list of distances from the source to all other vertices in the given graph.

#### Sample Input
```
graph = {
    0: [[1, 4], [7, 8]],
    1: [[2, 8], [7, 11]],
    2: [[3, 7], [8, 2], [5, 4]],
    3: [[4, 9], [5, 14]],
    4: [],
    5: [[4, 10]],
    6: [[5, 2], [8, 6], [7, 1]],
    7: [[8, 7]],
    8: []
}
source = 0
```
#### Sample Output
```
[0, 4, 12, 19, 21, 11, 9, 8, 14]
```
#### Explanation
- The shortest path from source 0 to vertex 1 has weight 4 (0 -> 1)
- The shortest path from source 0 to vertex 2 has weight 12 (0 -> 1 -> 2)
- The shortest path from source 0 to vertex 3 has weight 19 (0 -> 1 -> 2 -> 3)
- The shortest path from source 0 to vertex 4 has weight 21 (0 -> 1 -> 2 -> 5 -> 4)
- The shortest path from source 0 to vertex 5 has weight 11 (0 -> 1 -> 2 -> 5)
- The shortest path from source 0 to vertex 6 has weight 9 (0 -> 7 -> 6)
- The shortest path from source 0 to vertex 7 has weight 8 (0 -> 7)
- The shortest path from source 0 to vertex 8 has weight 14 (0 -> 1 -> 2 -> 8)

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

## Happy Coding! :smile: