def create_prompt(inputs: list[str]) -> str:
    print(inputs)
    with open("prompt.txt", "r") as f:
        pt = f.read()
    for i in inputs:
        pt = pt.replace("|", i, 1)
    return pt
