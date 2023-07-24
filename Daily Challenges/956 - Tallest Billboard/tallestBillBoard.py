class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        maxSum = sum(rods)
        tallestBill = [-1] * (maxSum + 1)
        tallestBill[0] = 0

        for rod in rods:
            tallestBill_copy = tallestBill[:]

            for i in range(maxSum - rod + 1):
                if tallestBill_copy[i] < 0:
                    continue

                tallestBill[i + rod] = max(tallestBill[i + rod], tallestBill_copy[i])
                tallestBill[abs(i - rod)] = max(tallestBill[abs(i - rod)], tallestBill_copy[i] + min(i, rod))

        return tallestBill[0]
