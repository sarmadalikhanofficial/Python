**README.md**

**Introduction**

This Python code analyzes a dataset of traffic accidents in Barcelona, Spain, and implements Dijkstra's algorithm to find the shortest path between two locations based on the number of accident victims involved. The code utilizes the pandas and NetworkX libraries for data manipulation and graph creation, respectively.

**Data Source**

The code expects a CSV file named `accidents_2017.csv` containing accident data. You can download this dataset from the following Kaggle link: [https://www.kaggle.com/code/xvivancos/discovering-barcelona-part-ii/input?select=accidents_2017.csv](https://www.kaggle.com/code/xvivancos/discovering-barcelona-part-ii/input?select=accidents_2017.csv)

**Code Functionality**

1. **Data Loading and Exploration:**
   - Loads the CSV data using pandas.
   - Displays the first few rows of the dataset.
   - Provides summary statistics of the data.
   - Analyzes the distribution of accidents by weekday and part of the day.
   - Calculates the total number of mild injuries, serious injuries, and total victims.

2. **Graph Creation and Shortest Path Finding:**
   - Constructs an undirected graph using NetworkX, where nodes represent streets and edges represent connections between streets.
   - Sets edge weights based on the number of accident victims involved in each accident.
   - Prompts the user to enter a source and target street name (replace with actual names from your dataset).
   - Implements Dijkstra's algorithm to find the shortest path between the source and target in terms of total accident victims.
   - Prints the shortest path and its total victim count.

3. **Shortest Path Visualization:**
   - Creates a subgraph containing only the nodes and edges of the shortest path.
   - Employs NetworkX visualization functions to display the graph with highlighted shortest path.

4. **Data Visualization:**
   - Generates bar charts to visualize the distribution of accidents by weekday and part of the day.

**Instructions**

1. Ensure you have pandas and NetworkX libraries installed (`pip install pandas networkx`).
2. Replace `'accidents_2017.csv'` with the actual path to your CSV file if it's located elsewhere.
3. Run the script using `python main.py`.
4. When prompted, enter the source and target street names for finding the shortest path.

**Note:**

* This code assumes the presence of the required columns (`Street`, `Neighborhood Name`, and `Victims`) in the CSV data.
* You might need to adjust the code for different data structures or file formats.
