"""
wimbledon
Estimate: 60 minutes
Actual:   49 minutes
"""

import csv

def read_data():
    """Read Wimbledon data from a CSV file and return a list of lists."""
    FILE_NAME = "wimbledon.csv"
    data = []
    with open(FILE_NAME,'r') as file_object:
        reader = csv.reader(file_object)
        next(reader)
        for row in reader:
            data.append(row)  # 添加每一行数据
    return data

def process_data(data):
    """Process Wimbledon data to extract champion counts and unique countries."""
    champion_to_wins = {}
    countries = set()
    for row in data:
        champion, country = row[2], row[1]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
        countries.add(country)
    return champion_to_wins, countries


def print_results(champion_to_wins, countries):
    """Display the processed Wimbledon champions and countries."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items(), key=lambda item: item[1], reverse=True):
        print(f"{champion} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def main():
    data = read_data()
    champion_to_wins, countries = process_data(data)
    print_results(champion_to_wins, countries)

main()