## Hacktober Fest 2022 - Hacktoberfest2022
### Circular Linked List in Python

#### Problem Statement
Circular Linked List is a type of linked list that is circular in nature. In a circular linked list, every node has successor. In this data structure, every node points to the next node and the last node of the linked list points to the first node.

You are given the head of a linked list containing integers, You need to find out whether the given linked list is circular or not.

#### Input Format
First line will take the input **T** as argument denoting the total number of links in the linked list.

Then, It will take the graph of **T** nodes with the data of the linked list and its next pointer in the form of adjacency list along with the head as argument.

#### Output Format
For each input graph print True or False depending on whether the linked list is circular or not.

> #### Note
> 1. A linked list is said to be circular if it has no node having its next pointer equal to NULL and all the nodes form a circle i.e. the next pointer of last node points to the first node.
> 2. An empty linked will also be considered as circular.
> 3. All the integers in the linked list are unique.
> 4. In the input, the next pointer of a node with i’th integer is linked to the node with data (i+1)’th integer (If (i+1)’th node exists). If there is no such (i+1)’th integer then the next pointer of such node is set to NULL.


#### Sample Input
```
Total Linkes = 4
graph = {
    1: [5, 7],
    2: [2, 5],
    3: [10, 2],
    4: [7, 8],
    5: [8, 10]
}
Head = 2
```

#### Sample Output
```
TRUE
```

#### Explanation

![Image Link](https://media.geeksforgeeks.org/wp-content/uploads/CircularLinkeList.png)

- According to the given input, linked list will look like this.
- Link Data and the next pointer is stored accordingly.
- Last link ```10``` is pointing towards ```2``` which is the head node, hence the given list is circular and the output generated is ```True```.

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
