class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:

        cleaned = []

        prev = position[0]
        for i in range(1, len(position)):
            if prev + distance >= (position[i]):
                prev = position[i]
            else:
                cleaned.append((prev, speed[i - 1]))
                prev = position[i]
            
            # print(prev)
        cleaned.append((prev, speed[-1]))
        # print(cleaned)


        stack = []

        for i, j in cleaned:

            # print(stack)
            while (stack) and (stack[-1][1] > j):
                stack.pop()


            stack.append((i, j))

        # print(stack)
        
        return len(stack)