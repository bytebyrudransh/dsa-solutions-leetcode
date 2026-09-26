class StockSpanner:

    def __init__(self):
        # Stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:

        # Today's span starts as 1 (today itself)
        span = 1

        # Merge spans of all previous prices
        # that are smaller than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Store current price and its computed span
        self.stack.append((price, span))

        # Return today's span
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)