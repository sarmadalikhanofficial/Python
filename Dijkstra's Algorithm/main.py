import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load the dataset from the local folder
data = pd.read_csv('accidents_2017.csv')

# Display the first few rows of the dataset
print(data.head())

# Summary statistics of the dataset
summary_stats = data.describe()
print(summary_stats)

# Count of accidents by weekday
accidents_by_weekday = data['Weekday'].value_counts()
print("Accidents by Weekday:")
print(accidents_by_weekday)

# Count of accidents by part of the day
accidents_by_part_of_day = data['Part of the day'].value_counts()
print("Accidents by Part of Day:")
print(accidents_by_part_of_day)

# Number of injuries
total_mild_injuries = data['Mild injuries'].sum()
total_serious_injuries = data['Serious injuries'].sum()
total_victims = data['Victims'].sum()

print(f"Total Mild Injuries: {total_mild_injuries}")
print(f"Total Serious Injuries: {total_serious_injuries}")
print(f"Total Victims: {total_victims}")

# Create a graph from the dataset using Dijkstra's algorithm
G = nx.Graph()

# Adding edges with weights (e.g., number of victims)
for index, row in data.iterrows():
    G.add_edge(row['Street'].strip(), row['Neighborhood Name'].strip(), weight=row['Victims'])

# Find shortest path using Dijkstra's algorithm
source = 'Número 27'  # Replace with actual street name from your dataset
target = 'Las Navas de Tolosa'  # Replace with actual street name from your dataset

# Check if source and target exist in the graph
if source in G.nodes() and target in G.nodes():
    shortest_path = nx.dijkstra_path(G, source=source, target=target)
    shortest_path_length = nx.dijkstra_path_length(G, source=source, target=target)
    
    print(f"Shortest path from {source} to {target}: {shortest_path}")
    print(f"Length of shortest path (Total Victims): {shortest_path_length}")

    # Create a subgraph for visualization of the shortest path
    H = G.edge_subgraph([(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)])

    plt.figure(figsize=(10, 6))
    
    # Draw the subgraph with highlighted path
    pos = nx.spring_layout(H)  # positions for all nodes in subgraph

    nx.draw(H, pos, node_size=700, with_labels=True, font_size=10, edge_color='b', width=2)
    
    # Highlight nodes in red for clarity
    nx.draw_networkx_nodes(H, pos, nodelist=shortest_path, node_color='r')

    plt.title(f'Shortest Path from {source} to {target}')
    plt.show()
else:
    print(f"Source '{source}' or Target '{target}' not found in graph.")

# Visualizations for accidents by weekday and part of day
plt.figure(figsize=(10, 5))
accidents_by_weekday.plot(kind='bar', color='skyblue')
plt.title('Accidents by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
accidents_by_part_of_day.plot(kind='bar', color='salmon')
plt.title('Accidents by Part of Day')
plt.xlabel('Part of Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()
