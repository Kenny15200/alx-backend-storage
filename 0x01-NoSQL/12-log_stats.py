#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client["logs"]
    col = db["nginx"]

    logs_count = col.count_documents({})

    print(f"{logs_count} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_count = col.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    get_status_count = col.count_documents({'method': 'GET',
                                            'path': '/status'})

    print(f"{get_status_count} status check")
