"""
parsing
"""

import argparse

developers = {"java": ["prashant", "rahul", "hardik"],
              "python": ["sachin", "dhoni"]
              }
parser = argparse.ArgumentParser(description="handy tool to greet of developers")

parser.add_argument("developer1", type=str, choices=["python","java"])
parser.add_argument("developer2", type=str, choices=["python","java"])

args = parser.parse_args()

if args.developer1 == "java" or args.developer1 == "python":
    print(f"list of developers -\n {developers.get(args.developer1)}")
else:
    print("ERROR : please choose between python and java")

if args.developer2 == "java" or args.developer2 == "python":
    print(f"list of developers -\n {developers.get(args.developer2)}")
else:
    print("ERROR : please choose between python and java")
