## Hacktober Fest 2022 - Hacktoberfest2022
### Reverse Doubly-Linked list in Python

#### Problem Statement
A doubly-linked list is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains two fields, called links, that are references to the previous and to the next node in the sequence of nodes.

Given a Doubly Linked List, you are asked to reverse the list in place without using any extra space.

#### Input Format
First line will take the input **N** as argument denoting the total number of nodes in the Doubly linked list.

Then, it will take the linked list in the form of adjacency list along with the next and previous pointers.
If a node has no previous pointer then, it means it's the source/head node.
If a node has no next pointer then, it means it's the end node.

Consider first node as the HEAD.

#### Output Format
For each input graph, print the final result after reversing the list.

#### Sample Input
```
Total Links = 5
graph = {
    1: [, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4,]
}
```

#### Sample Output
```
[5, 4, 3, 2, 1]
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
