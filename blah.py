from src import sce
import sys

word = sys.argv[1]

with open('proto_to_a.txt', 'r') as t:
    ruleset = t.read()
    print(sce.run([word], ruleset, output='list')[0])
