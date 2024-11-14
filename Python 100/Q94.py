# Write a program to solve a classic ancient Chinese puzzle: We count 35
# heads and 94 legs among the chickens and rabbits in a farm. How many
# rabbits and how many chickens do we have?

def counting_legs(heads, legs):
    chicken_legs = 2
    rabbit_legs = 4
    for rabbit_heads in range(0, heads):
        total_legs = (chicken_legs * (heads - rabbit_heads)) + (rabbit_legs * rabbit_heads)
        if total_legs == legs:
            return f"{rabbit_heads} rabbits & {heads - rabbit_heads} chickens!"

print(counting_legs(35,94))