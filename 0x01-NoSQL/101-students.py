#!/usr/bin/env python3
"""This module defines a function `top_students`"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""

    project_stage = {
            "$project": {
                "_id": "$_id",
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            }

    sort_stage = {
            "$sort": {"averageScore": -1}
            }

    aggr_students = mongo_collection.aggregate([
        project_stage, sort_stage
        ])

    return aggr_students
