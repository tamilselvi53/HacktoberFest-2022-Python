## Hacktober Fest 2022 - Hacktoberfest2022
### KnapSack Problem in Python

#### Problem Statement
A thief broke into the house of a man who is the collector and have **i** antique artifacts. Cost and weight of every artifact is written on it. Thief have a knapsack of Capacity **T** which can hold items not more than this.

You are required to give an array as output of the artifacts that the thief will select so that the Porift is maximum and the weight is less than or equal to **T**.

#### Input Format
First line will take the input **i** as argument denoting the total number of items present.

Then, it will take the items in the form of adjacency list along with there Value **v[i]** and weight **w[i]**.

Last, input total Capacity **T** as an argument.


#### Output Format
Array of the selected items along with the maximum profit.

#### Sample Input
```
Total Items = 4
graph = {
    1: [10, 10],
    2: [2, 5],
    3: [1, 10],
    4: [3, 10]
}
Total Capacity = 20
```

#### Sample Output
```
["1", "4"]
13
```

#### Explanation
- Optimal selection is 1st and 4th object.
- Total value=(10+3)=13.
- Total weight=(10+10)=20.
- (Total weight) <= (Capacity).

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
