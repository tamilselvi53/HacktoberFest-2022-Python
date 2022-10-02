## Hacktober Fest 2022 - Hacktoberfest2022
### Breadth First Search in Python

#### Problem Statement
Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.

Given **n**, i.e. total number of nodes in an undirected graph numbered from **1** to **n** and an integer **e**, i.e. total number of edges in the graph. _Calculate the Breadth First order of nodes considering node 1 as source node_.

#### Input Format
It will take the graph input in the form of adjacency list and the starting node as input.

#### Output Format
For each input graph print the breadth first order of traversal of nodes.

#### Sample Input
```
graph = {
    1: [2],
    2: [1, 4, 3],
    3: [2, 5],
    4: [2],
    5: [3]
}
start = 1
```

#### Sample Output
```
1 2 4 3 5
```

#### Explanation
![Sample Output](https://he-s3.s3.amazonaws.com/media/uploads/5faefdfa-75f5-438e-976d-0efae05cec7d.png)
- The graph is represented as an adjacency list.
- The starting node is 1.
- The output is the breadth first order of traversal of nodes.
- The output is 1 2 4 3 5.
- The output is the order in which the nodes are visited.

                     
Constructed graph will look like above hence breadth first order will be ```1 2 3 4 5``` or ```1 2 4 3 5```.

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
