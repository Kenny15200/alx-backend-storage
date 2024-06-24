#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    col = db.nginx

    # getting the methods and count for each
    logs_count = col.count_documents({})

    print(f"{logs_count} logs\nMethods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_count = col.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    get_status_count = col.count_documents({'method': 'GET',
                                            'path': '/status'})

    print(f"{get_status_count} status check\nIPs:")

    # adding the top 10 of the most present IPs
    group_stage = {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
                }
            }

    sort_stage = {
            "$sort": {"count": -1}
            }

    limit_stage = {
            "$limit": 10
            }

    pipeline = [group_stage, sort_stage, limit_stage]

    result = col.aggregate(pipeline)

    for row in result:
        print(f"\t{row['_id']}: {row['count']}")
