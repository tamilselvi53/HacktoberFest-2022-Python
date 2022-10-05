## Hacktober Fest 2022 - Hacktoberfest2022
### Topological Sort in Python

#### Problem Statement
A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge _uv_ from vertex _u_ to vertex _v_, _u_ comes before _v_ in the ordering.

Given a Directed and Acyclic Graph having **N** vertices and **M** edges, print topological sorting of the vertices.

#### Input Format
Make a function that accepts two space separated integers denoting **N** and **M** as arguments. 

Next, it will take the graph of **M** edges in the form of adjacency list. The format of adjacency list is in such a way, each input denotes that there is an outward edge from given to other nodes in the graph at that level.

#### Output Format
Print the array containing **N** integers denoting the topological sort, if there are multiple ordering print the lexicographically smallest one.

Also, if there is cycle exist in the graph, return **-1** as output.

#### Sample Input
```
Total Nodes = 5
Total Edges = 6
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [4],
    4: [5],
    5: []
}
```

#### Sample Output
```
[1, 2, 3, 4, 5]
```

#### Explanation 

![Acco. to question](https://www.interviewcake.com/images/svgs/messy_graph.svg?bust=210)

- Since node ```1``` points to nodes ```2``` and ```3```, node ```1``` appears before them in the ordering.

- Nodes ```2``` and ```3``` both point to node ```4```, they appear before it in the ordering.

![Final Answer](https://www.interviewcake.com/images/svgs/topologically_sorted_graph.svg?bust=210)

- So ```[1, 2, 3, 4, 5]``` would be a topological ordering of the graph.

> #### Note
   > Can a graph have more than one valid topological ordering? Yep! In the example above, [1, 3, 2, 4, 5] works too.

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
