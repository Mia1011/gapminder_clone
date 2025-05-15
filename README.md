# 200 Countries, 200 Years, 4 Minutes

## Description
This project is a recreation of the renowned data visualization &mdash; [Hans Rosling's *200 Countries, 200 Years, 4 Minutes*](https://youtu.be/jbkSRLYSojo?si=J721nOUK5bfS5ugY). I used `pandas` and `sqlite3` to build the database, conducted a proof of concept using `matplotlib`, and finally recreated the visualization with `plotly.express`. 


## How to run
- Install [Miniconda](https://youtu.be/jbkSRLYSojo?si=J721nOUK5bfS5ugY). 

- Download the project files and ensure the four CSV files are placed in the `data/` folder within your working directory.

- Set up the environment:
```shell
conda env create -f environment.yml -n <your_env_name>
```

- Activate the environment: 
```shell
conda activate <your_env_name>
```

- Build the database `gapminder.db` in the `data/` folder:
```shell
python create_gapminder_db.py
```

- Finally, generate the visualization `gapminder_clone.html`:
```shell
python plot_with_px.py
```
