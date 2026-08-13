class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five = 0
        ten = 0
        for note in bills:
            if note == 5:
                five += 1

            if note == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1

            if note == 20:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False


        return True