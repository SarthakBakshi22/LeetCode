class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # remAmount = amount
        # count=0
        # coins.sort()
        # if sum(coins)==amount:
        #     return len(coins)
        # while(len(coins)>0):
        #     remAmount=remAmount-max(coins)
        #     if remAmount>0:
        #         count+=1
        #     elif remAmount==0:
        #         return count+1
        #     else:
        #         remAmount=remAmount+max(coins)
        #         coins.remove(max(coins))
        # if remAmount > 0:
        #     return -1
        # else:
        #     return count
        coinComb = [amount + 1] * (amount + 1)
        coinComb[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                coinComb[i] = min(coinComb[i], coinComb[i - coin] + 1)
        for i in range(amount + 1):
            if coinComb[i] == amount + 1:
                coinComb[i] = -1
        return coinComb[amount]
