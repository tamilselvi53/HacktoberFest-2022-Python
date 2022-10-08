# Hacktoberfest 2022

## Floyd Warshall Algorithm

### Problem Statement

Floyd Warshall algorithm is a dynamic programming algorithm that is used to find the shortest path between all the pairs of vertices in a weighted graph. It is also used to detect the negative weight cycle in a graph.

## Input Format

The `floyd_warshall` function takes the following arguments:

- `graph`: The adjacency matrix of the graph.

## Output Format

The `floyd_warshall` function returns the shortest distance between all the pairs of vertices in a weighted graph.

## Sample Input

```
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]
```

## Sample Output

```
[[0, 5, 8, 9],
 [INF, 0, 3, 4],
 [INF, INF, 0, 1],
 [INF, INF, INF, 0]]
```
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