#!/usr/bin/python3
"""
extend Python script to export
data in the CSV format.
"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    payload = {"userId": sys.argv[1]}
    req_rep1 = requests.get(url1, params=payload)
    req_rep2 = requests.get(url2)
    req_rep1 = req_rep1.json()
    req_rep2 = req_rep2.json()
    filename = f"{sys.argv[1]}.csv"
    with open(filename, 'w', newline='') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=",", quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        for data in req_rep1:
            data_writer.writerow([data["userId"], req_rep2["username"],
                                 data["completed"], data["title"]])
