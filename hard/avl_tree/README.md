## Hacktober Fest 2022 - Hacktoberfest2022
### AVL Tree in Python

#### Problem Statement
AVL tree is a self-balancing binary search tree in which each node maintains extra information called a balance factor whose value is either -1, 0 or +1.

Write a program for AVL tree having functions for the following operations:

- Insert an element (no duplicates are allowed),
- Delete an existing element,
- Traverse the AVL (in-order, pre-order, and post-order)

#### Input Format
Make a function to accept integer **NQ** as argument denoting the number of queries.

Following will take the tree in the form of adjacency list of **NQ** queries and are in the form **i x** _(Insert **x** into the AVL Tree)_  or **d x** _(Delete **x** from the AVL tree)_.

#### Output Format
For each query, print value of an unbalanced node (if any) at which rotation is being applied in the form of an array.

Later, print the ```PreOrder Traversal```, ```InOrder Traversal```, and ```PostOrder Traversal``` of an AVL tree that results after the execution of all **NQ** queries.

#### Sample Input
```
Total Queries = 8
graph = {
    1: [i, 1],
    2: [i, 2],
    3: [i, 3],
    4: [i, 4],
    5: [i, 5],
    6: [i, 6],
    7: [d, 4],
    8: [d, 5]
}
```

#### Sample Output
```
{1, 3, 2, 6}
PreOrder = [2, 1, 6, 3]
InOrder = [1, 2, 3, 6]
PostOrder = [1, 3, 6, 2]
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
