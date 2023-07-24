class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 1000000007
        n = len(locations)   
        routes = [[0] * (fuel + 1) for _ in range(n)]
        for f in range(fuel + 1):
            routes[finish][f] = 1
        
        for f in range(fuel + 1):
            for city in range(n):
                for nextCity in range(n):
                    if nextCity != city and f >= abs(locations[nextCity] - locations[city]):
                        routes[city][f] = (routes[city][f] + routes[nextCity][f - abs(locations[nextCity] - locations[city])]) % MOD
        
        return routes[start][fuel]
