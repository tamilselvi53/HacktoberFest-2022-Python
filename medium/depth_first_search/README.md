## Hacktober Fest 2022 - Hacktoberfest2022
### Depth First Search in Python

#### Problem Statement
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

Given **n**, i.e. total number of nodes in an undirected graph numbered from **1** _to_ **n** . _Calculate the Depth First order of nodes considering given node s as source node_.

#### Input Format
First line will take the input **n** as argument denoting the total number of nodes in the graph.
It will take the graph in the form of adjacency list along with the starting/source node as argument.

#### Output Format
For each input graph print the Depth first order of traversal of nodes.

#### Sample Input
```
Total Nodes = 5
graph = {
    1: [2],
    2: [1, 4, 3],
    3: [2, 5],
    4: [2],
    5: [3]
}
start = 2
```

#### Sample Output
```
2 1 3 5 4
```

#### Explanation
![Sample Output](https://he-s3.s3.amazonaws.com/media/uploads/5faefdfa-75f5-438e-976d-0efae05cec7d.png)
- The graph is represented as an adjacency list.
- The starting node is 2.
- The output is the depth first order of traversal of nodes.
- Traversing the neighboring node to the farthest before moving on to the next node.
               
Constructed graph will look like above hence depth first order will be ```2 1 3 5 4```.

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
