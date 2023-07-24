class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maxProb = collections.defaultdict(dict)
        for (st, en), prob in zip(edges, succProb):
            maxProb[st][en] = prob
            maxProb[en][st] = prob

        que = []
        heapq.heappush(que, (-1, start))
        while que:
            pr, node = heapq.heappop(que)
            if node == end:
                return -pr
            for sn, sp in maxProb[node].items():
                heapq.heappush(que, (pr*sp, sn))
                del maxProb[sn][node]
            del maxProb[node]

        return 0.0
