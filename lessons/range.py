"""Demonstrates range in a for loop."""

names: list[str] = {"Alyssa", "Janet", "Vrinda"}

for index in range(0,len(names)):
    # 0: Alyssa
    print(f"{index}:{names[index]}")