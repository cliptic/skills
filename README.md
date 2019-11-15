# skills
CV addition with technical skills.
That is how we do it. Woop woop.

Just add a simple CSV file, just like this one:
![alt text](https://github.com/cliptic/skills/blob/master/CSV.jpg)
[link](https://github.com/cliptic/skills/blob/master/CV_03.csv).
This code will plot a pretty little graph of your input hours on the skills you have.
![alt text](https://github.com/cliptic/skills/blob/master/Figure_7.png)

The code consists of 2 Python files: 
[<<_FILE_NO_1_>>](https://github.com/cliptic/skills/blob/master/CV_data.py)
-- Imports CSV
-- Transforms the DataFrame to a sequential Time / Skill relationship format
[<<_FILE_NO_2_>>](https://github.com/cliptic/skills/blob/master/Seaborn.py)
-- Transposes the DataFrame to a time series format
-- Aggregates accumulated hour values
-- Sorts skills by end Value
-- Uses Seaborn to make some pretty plots
