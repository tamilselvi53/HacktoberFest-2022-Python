#Hacktoberfest 2022

## A* Pathfinding Algorithm

This is a simple implementation of the A* pathfinding algorithm in Python. You can implement this algorithm in your own projects to find the shortest path between two points. The algorithm is based on the pseudocode from Wikipedia. you can use various heuristics to find the shortest path. The default heuristic is the Manhattan distance. 

## Input Format

The input is a adjacency list of the graph. First argument is the graph and the second argument is the start node and the third argument is the end node.

## Output Format

The output is the shortest path between the start node and the end node.

## Sample Input

```
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('A', 1), ('C', 1), ('D', 3)],
    'C': [('A', 2), ('B', 1), ('D', 1)],
    'D': [('B', 3), ('C', 1)]
}
start = 'A'
end = 'D'
```

## Sample Output

```
['A', 'C', 'D']
```

## Explanation

- The graph is represented as an adjacency list.
- The starting node is A.
- The path printed as the output has the cost 9 associated with it i.e.i.e. the sum of weights of all edges present in the path.
- It can be shown that no other path exists that connects src to dest with a smaller weight.

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
