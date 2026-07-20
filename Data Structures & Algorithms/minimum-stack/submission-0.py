class MinStack:

    def __init__(self):
        self.array = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.array.append(val)

        if not self.min_vals:
            self.min_vals.append(val)

        #Keep adding the minimum value between the current value and the current smallest
        else:
            self.min_vals.append(min(val, self.min_vals[-1]))

    def pop(self) -> None:
        self.array.pop()
        self.min_vals.pop()
        
    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]

