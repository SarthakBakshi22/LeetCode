class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        playLists = [[0] * (goal + 1) for _ in range(n+1)]
        playLists[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                playLists[i][j] = (playLists[i-1][j-1] * (n - i + 1) + playLists[i][j-1] * max(i-k, 0)) % MOD

        return playLists[n][goal]
