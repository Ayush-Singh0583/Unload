import statistics
import sys
import time

from sorter import sort_dump

DUMP = """infrrd form due soon, fix the numbers on my resume, portfolio timeline,
dp revision, bda viva prep, plan a trip with my friend, sleep properly,
the college wifi is down tonight"""

LEVEL = sys.argv[1] if len(sys.argv) > 1 else "medium"
RUNS = 5
times = []

print(f"Thinking level: {LEVEL}")
for i in range(1, RUNS + 1):
    start = time.perf_counter()
    result = sort_dump(DUMP, thinking_level=LEVEL)
    seconds = time.perf_counter() - start
    times.append(seconds)
    wifi_ok = any(
        "wifi" in item.text.lower() and item.bucket == "cant_fix_now"
        for item in result.items
    )
    print(f"Run {i}: {seconds:.1f} s, {len(result.items)} items, wifi correct: {wifi_ok}")

print(f"\nMedian: {statistics.median(times):.1f} s")
print(f"Fastest: {min(times):.1f} s   Slowest: {max(times):.1f} s")