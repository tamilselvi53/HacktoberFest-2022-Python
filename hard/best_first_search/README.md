## Hacktober Fest 2022 - Hacktoberfest2022
### Best First Search in Python

#### Problem Statement
Best-first search is a class of search algorithms, which explore a graph by expanding the most promising node chosen according to a specified rule.

Given a connected and weighted graph, a source node, and a destination node. The task is to find the path with the least cost from the source node **src** to the destination node **dest**. Where the cost is the sum of the weights of the edges included in the path.

#### Input Format
First line will take the input **n** as argument denoting the total number of edges in the graph.

Following will take the graph in the form of adjacency list of **n** edges and are in the form **[v1, v2, e]** where _v1 v2_ denotes that there is an edge between these two with edge value of _e_.

Moreover, make a function to accept source node **src** and destination node **dest**. 

#### Output Format
For each input graph print the path to be followed with minimum cost in an array.

#### Sample Input
```
Total Edges = 7
graph = {
    1: [0, 1, 5],
    2: [0, 2, 7],
    3: [1, 3, 6],
    4: [2, 4, 3],
    5: [4, 5, 2],
    6: [5, 3, 10],
    7: [1, 4, 2],
}
src = 0
dest = 5
```



#### Sample Output
```
[0, 1, 4, 5]
```

#### Explanation
![Sample Output](https://scaler.com/topics/images/example-to-explain-best-first-search.webp)
- The graph is represented as an adjacency list.
- The starting node is 0.
- The path printed as the output has the cost 9 associated with it i.e.i.e. the sum of weights of all edges present in the path.
- It can be shown that no other path exists that connects \text{src}src to \text{dest}dest with a smaller weight.

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
