"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)],
            "answer": [2, 2, 1, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4)],
            "answer": [0, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("EA", 41)],
            "answer": [4, 0, 3, 0, 0]
        }
    ],
    "Extra": [
        {
            "input": ["ADBC", ("AD",1), ("DB", 9), ("BC", 0.345), ("CA", 13)],
            "answer": [0, 1, 1, 2, 0]
        },
        {
            "input": ["9876543210"],
            "answer": [0, 0, 0, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4)],
            "answer": [0, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("BC", 3)],
            "answer": [0, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("BC", 3), ("AD", 1)],
            "answer": [0, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("EA", 41)],
            "answer": [4, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("DA", 4)],
            "answer": [0, 0, 3, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AD", 4), ("DA", 6.1)],
            "answer": [0, 3, 0, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AE", 4), ("EA", 4)],
            "answer": [0, 0, 8, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AE", 4), ("EA", 41)],
            "answer": [4, 0, 4, 0, 0]
        },
        {
            "input": ["ABCDEFGH", ("AE", 170), ("EA", 10000), ("HF", 1)],
            "answer": [410, 0, 0, 0, 0]
        },
        {
            "input": ["+-=/5gh3@", ("3@", 0.0005), ("+=",0.27), ("/5", 100.03)],
            "answer": [2, 0, 0, 2, 1]
        },
        {
            "input": ["+-=/5gh3@", ("3@", 0.0005), ("+=",0.27), ("/5", 100.03), ("+@", 187.2)],
            "answer": [4, 0, 0, 2, 1]
        },
        {
            "input": ["+-=/5gh3@", ("3@", 0.0005), ("+=",0.27), ("/5", 100.03), ("+@", 187.2), ("-h", 1100000)],
            "answer": [44006, 0, 0, 1, 0]
        }
    ]
}
