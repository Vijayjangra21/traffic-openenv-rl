from grader import grade
from baseline import baseline

modes = ["easy", "medium", "hard"]

print("Baseline Performance:\n")

for mode in modes:
    score = grade(baseline, mode=mode)
    print(f"Mode: {mode}, Score: {score:.3f}")