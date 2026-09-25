class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []                   # monotonic stack storing indices
        result = [0] * len(temp)     # default 0 = no warmer day found

        for i in range(len(temp)):
            # temp[i] is warmer than days waiting in the stack
            while len(stack) and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                result[idx] = i - idx    # days waited = current index - waiting index
            stack.append(i)

        # remaining indices in stack have no warmer day → result stays 0
        return result