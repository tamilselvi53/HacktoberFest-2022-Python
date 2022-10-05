## Hacktober Fest 2022 - Hacktoberfest2022
### Kruskal's Algorithm in Python

#### Problem Statement
Kruskal's Algorithm is used to find the minimum spanning tree for a connected weighted graph. The main target of the algorithm is to find the subset of edges by using which we can traverse every vertex of the graph.

You will be given a weighted undirected graph **G** with **E** edges and **V** vertices along with the cost **C** of each edgs. Your task is to print the total minimum cost according minimum spanning tree.

#### Input Format
Make a function to accept total vertices **V** and total edges **E** as arguments.

Then, it will take the undirected weighted graph containing **E** edges in the form of adjacency list along with the weight of that respective edge.

#### Output Format
For each input graph, print the total cost after applying Kruskal's Algorithm.

#### Sample Input
```
Total Vertices = 5
Total Edges = 7
graph = {
    A: [B, 1],
    A: [C, 7],
    B: [C, 3],
    C: [D, 4],
    D: [E, 2],
    D: [A, 10],
    E: [A, 5]
}
```

#### Sample Output
```
10
```

#### Explanation 

![Input](https://static.javatpoint.com/ds/images/kruskals-algorithm1.png)

- Input graph will look like this.
- Sort the edges in ascending order respected to there costs.

| Edges | Weights |
| ----- | ------- |
|AB|1|
|ED|2|
|BC|3|
|CD|4|
|AE|5|
|AC|7|
|AD|10|
- Start Selecting the edges with the minimum weight. Drop if making a loop.
![Final](https://static.javatpoint.com/ds/images/kruskals-algorithm5.png)

- Starting from edge AB, following is the graph as output.
- The cost of the MST is = AB + DE + BC + CD = 1 + 2 + 3 + 4 = 10.

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
