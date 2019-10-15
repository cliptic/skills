# skills
CV addition with technical skills.
That is how we do it. Woop woop.

Just add a simple CSV file, just like this one:
[<<_LOOK_AT_INPUT_CSV_FILE_>>](https://github.com/cliptic/skills/blob/master/CV_03.csv).
This code will plot a pretty little graph of your input hours on the skills you have.
[<<_LOOK_AT_GRAPH_>>](https://github.com/cliptic/skills/blob/master/Figure_6.pdf)

The code consists of 2 Python files: 
[<<_FILE_NO_1_>>](https://github.com/cliptic/skills/blob/master/CV_data.py)
-- Imports CSV
-- Transforms the DataFrame to a sequential Time / Skill relationship format
[<<_FILE_NO_2_>>](https://github.com/cliptic/skills/blob/master/Seaborn.py)
-- Transposes the DataFrame to a time series format
-- Aggregates accumulated hour values
-- Sorts skills by end Value
-- Uses Seaborn to make some pretty plots
