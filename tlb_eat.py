# Program to calculate Effective Access Time (EAT)

tlb_time = 10
memory_time = 80

def calculate_eat(hit_ratio):
    return (hit_ratio * (tlb_time + memory_time)
            + (1 - hit_ratio) * (tlb_time + 2 * memory_time))

print("Effective Access Time Calculation")
print("---------------------------------")
print("TLB Lookup Time:", tlb_time, "ns")
print("Main Memory Access Time:", memory_time, "ns")

hit_ratios = [0.90, 0.75]
results = []

for h in hit_ratios:
    eat = calculate_eat(h)
    results.append(eat)

    print("\nTLB Hit Ratio:", h)
    print(f"Effective Access Time: {eat:.2f} ns")

print("\nComparison")
print("EAT at 0.90 hit ratio:", results[0], "ns")
print("EAT at 0.75 hit ratio:", results[1], "ns")
print(f"Difference: {results[1] - results[0]:.2f} ns")
