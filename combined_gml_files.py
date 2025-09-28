import networkx as nx
import csv
import glob
import os

output_csv = r"G:\StackOverflow\Data\final_file_with_d-core\2022\Combined_Network_2022.csv"

files = glob.glob(r"G:\StackOverflow\Data\final_file_with_d-core\2022\**\finalgml_2022_*.gml", recursive=True)

with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    
    writer.writerow([
        "Label", "Year", "Month",
        "In Strength", "Out Strength", 
        "Betweenness Centrality", "Clustering Coefficient","Eigenvector Centrality",
        "Category", "Rank",
        "Reputation", "Active Duration (Days)",
        "Gold Badges", "Silver Badges", "Bronze Badges","Burt's Constraint","k-core","l-core"
    ])

    for file in files:
        G = nx.read_gml(file)
        filename = os.path.basename(file)
        parts = filename.split("_")
        year = parts[1]
        month = parts[2].split(".")[0]

        for node, attrs in G.nodes(data=True):
            writer.writerow([
                attrs.get("label", node),             
                year,
                month,
                attrs.get("in_strength", ""),
                attrs.get("out_strength", ""),
                attrs.get("betweenness", ""),
                attrs.get("clustering_coefficient", ""),
                attrs.get("Eigenvector_Centrality"),
                attrs.get("category", ""),
                attrs.get("rank", ""),                
                attrs.get("reputation", ""),
                attrs.get("active_duration_days", ""),
                attrs.get("gold_badges", ""),
                attrs.get("silver_badges", ""),
                attrs.get("bronze_badges", ""),
                attrs.get("burts_constraint",""),
                attrs.get("k_core",""),
                attrs.get("l_core","")
            ])

print(f"CSV file saved successfully: {output_csv}")
