import re
from queue import Queue

from utils import read, p1, p2


def main():
    lines = read()

    v = {}
    for line in lines:
        name, rate, valves = re.findall(r'Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)[0]
        v[name] = {
            'rate': int(rate),
            'valves': valves.split(', '),
        }

    distances = {}
    valves_of_interest = set(x for x, y in v.items() if y['rate'] > 0)
    for valve in list(valves_of_interest) + ['AA']:
        q = Queue()
        visited = set()
        q.put((valve, 0))
        while not q.empty():
            valve2, dist = q.get()
            visited.add(valve2)
            if valve != valve2 and valve2 in valves_of_interest:
                distances[(valve, valve2)] = dist

            for valve_cand in v[valve2]['valves']:
                if valve_cand not in visited:
                    q.put((valve_cand, dist + 1))

    print(distances)

    dp_memo = {}
    def dp(valve, time, current_opens):
        key = (valve, time, ','.join(sorted(current_opens)))
        if key not in dp_memo:
            current_release = sum(v[x]['rate'] for x in current_opens)
            best = 0
            for valve2 in valves_of_interest:
                if valve2 not in current_opens and valve2 in valves_of_interest:
                    t = distances[(valve, valve2)] + 1
                    if time - t >= 0:
                        res = t * current_release + dp(valve2, time - t, [valve2] + current_opens)
                        if res > best:
                            best = res
            if best == 0:
                best = time * current_release
            dp_memo[key] = best
        return dp_memo[key]

    p1(dp('AA', 30, []))

