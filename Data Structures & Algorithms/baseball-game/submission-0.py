class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = []

        for c in operations:
            if c == "C":
                op.pop()

            elif c == "D":
                s1 = op[-1]
                op.append(2 * s1)

            elif c == "+":
                s1 = op[-1]
                s2 = op[-2]
                op.append(s1 + s2)

            else:
                op.append(int(c))

        return sum(op)
        return sum