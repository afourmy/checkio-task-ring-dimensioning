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
        }
    ]
}
