## Hacktober Fest 2022 - Hacktoberfest2022
### Dijkstra Algorithm in Python

#### Problem Statement
> The Dijkstra algorithm is an algorithm that is used for finding the shortest distance, or path, from starting node to target node in a weighted graph.

Here You need to implement Dijkstra's Algorithm(Single Source Shortest Path Algorithm).

You will be given an _adjacency matrix of an undirected graph_ and some q queries.

Each query contains **two integers**(0-indexed) denoting the source and destination vertices. 

For every query you need to ***print the shortest path*** between the given two vertices.

#### Input Format
First line contains integer **n** denoting the number of vertices in the graph.

Next **n** lines contains **n** integers denoting ***n***_x_***n*** adjacency matrix **a**,the value ***a[ i ] [ j ]*** denotes the distance between _ith_ and _jth_ vertex.

Next line contains integer **q** denoting number of queries.

Next **q** lines contains two integers denoting source and destination vertices

#### Output Format
Output the **q** lines _denoting_ the _shortest path between two vertices_ given in each respective query.

#### Sample Input
```
5
0 5 10 2 0
5 0 3 7 2
10 3 0 0 0
2 7 0 0 3
0 2 0 3 0
3
0 4
2 3
1 3
```
#### Sample Output
```
5
8
5
```
#### Constraints 
- [x] 1 <=  **n** <= 9

- [x] 1 <= **q** <= **n**

- [x] 1<= **a[i][j]** <= 100000.

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
