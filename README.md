# python_assessment

**NOTE**: Please DO NOT edit any of the files that I wrote. To prevent conflicts, you should write your code/answers in new files.

After forking this repo, you should set my repo as a remote repo of yours:
```
git add remote upstream https://github.com/vuoanh/python_assessment.git
```

So that you can update later tasks to your repo by pulling from my repo :
```
git pull upstream master
```

### Task 1:

Inside the directory named task1, write a python script that reads in the file sorted_models.txt, and plot a scatter plot between total score (x-axis) and interface_delta_X (y-axis). Make the plot as pretty and consistent as you can.


### Task 2:

Copy your python regular script file to a new directory named task2. Add an other parameter in the prompt so that the user can set their maximum total_score and maximum interface_delta_X. Now you will add more axis information to the graph (name of the axis). You should use some themes that matplotlib have. Feel feel to adjust font size of axises to make them more reable.

### Task3:
Copy your python script in part 2 to a new dir called task3. Now divide the data points into 2 groups based on whether the sum of (total_point + interface_delta_X) higher than average or not. Color those two group differently and include a legend for that. Also, in the lower right conner of the graph, include a annotation text of total_score and interface_delta_X of the point that have lowest sum of (total_point + interface_delta_X).


### Assessment:

In a new directory assessment, write a python script that:
- Read in the file rmsd_score_ligand.sc, prompt for maximum rmsd(ligand_rms_no_super_X) and interface_delta_X, and output file name from the user (like what you did in task 3).
- Divide the data points into 2 groups by comparing their total_score to the average total_score of all the data points that satisfy the user' setup.
- Plot the rmsd (x-axis) vs the Interface_delta_X (y-axis), set the maximum x and y stick value to maximum rmsd score and maximum Interface_delta_X, respectively.
- Set labels and font size for axis so that the plot looks pretty
- Color 2 groups of data differently,and include a legend for that.

