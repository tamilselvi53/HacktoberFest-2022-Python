## Hacktober Fest 2022 - Hacktoberfest2022
### Binary Search Tree in Python

#### Problem Statement
A Binary Search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree.

Monk is standing at the door of his classroom. There are currently **N** students in the class, **i<sup>th</sup>** student got **A<sub>i</sub>** candies.

There are still **M** more students to come. At every instant, a student enters the class and wishes to be seated with a student who has exactly the same number of candies. For each student, Monk shouts _YES_ if such a student is found, _NO_ otherwise.

#### Input Format
Make a function to accept 2 integers **N** and **M** as arguments.

Next accept an array of ***N + M*** integers, representing the candies of the students.

#### Output Format
For each new student, Monk's answer to the **M** students.
Print _"YES"_ (without the quotes) or _"NO"_ (without the quotes) pertaining to the Monk's answer.


#### Sample Input
```
Students in Class = 2
Students Yet to Come = 3
[5, 3, 6, 5, 3]
```

#### Sample Output
```
[NO, YES, YES]
```

#### Explanation 
- There are already 2 students present in the class with ```5``` and ```3``` candies respectively.
- On the arrival of 3<sup>rd</sup> student, no earlier student have ```6``` candies so output is ```NO```.
- When 4<sup>th</sup> and 5<sup>th</sup> students came, earlier students with candies count ```5``` and ```3``` found so the output was ```YES``` and ```YES```.

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
