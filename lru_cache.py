# Program to simulate LRU Cache Replacement

cache_size = 3
access_sequence = [4, 2, 1, 4, 3, 2, 5, 4]

cache = []  # Least recently used block is at the beginning
hits = 0
misses = 0

print("LRU Cache Replacement Simulation")
print("-" * 65)
print(f"{'Block':<10}{'Status':<10}{'Cache Contents':<25}{'Removed'}")
print("-" * 65)

for block in access_sequence:
    removed = "-"

    if block in cache:
        status = "HIT"
        hits += 1
        cache.remove(block)
        cache.append(block)
    else:
        status = "MISS"
        misses += 1

        if len(cache) == cache_size:
            removed = cache.pop(0)

        cache.append(block)

    print(f"{block:<10}{status:<10}{str(cache):<25}{removed}")

total_accesses = len(access_sequence)
hit_ratio = hits / total_accesses

print("-" * 65)
print("Total Hits:", hits)
print("Total Misses:", misses)
print(f"Hit Ratio: {hit_ratio:.3f}")
print(f"Hit Percentage: {hit_ratio * 100:.2f}%")
