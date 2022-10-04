## Hacktober Fest 2022 - Hacktoberfest2022
### Prim's Algorithm in Python

#### Problem Statement
Prim's algorithm starts with the single node and explores all the adjacent nodes with all the connecting edges at every step. The edges with the minimal weights causing no cycles in the graph got selected.

You are given a weighted undirected graph consisting of **N** nodes (numbered from 0 to N) along with the weight **W** of every edge. _Print the weight of it's Minimum Spanning Tree_.

#### Input Format
First line will take the input **N** as argument denoting the total number of nodes in the graph.

It will take the graph in the form of Array along with the weight of each edge.

Take Source node as argument.

#### Output Format
Print the weight of the Minimum Spanning Tree of the given graph.

#### Sample Input
```
Total Nodes = 5
Array = [A B : 4, B C : 2, C D : 1, D A : 3, A E : 5]
Source = A
```

#### Sample Output
```
11
```

#### Explanation
![Sample Output](https://favtutor.com/resources/images/uploads/mceu_12372525921626765362468.png)
- The graph is represented as above according to the input.
- The starting node is A.
- Start from node **A** and select those nodes with that of minimum weight and are not making any cycle.

![Result Image](https://favtutor.com/resources/images/uploads/mceu_65779473161626765621880.png)

- The resulting graph will loom like this.
- Total Cost = ```2 + 1 + 3 + 5 = 11```

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
