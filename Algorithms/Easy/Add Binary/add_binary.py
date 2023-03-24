class _Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def inner(index: int, a: str, b: str, pre_res: str):
            if index >= len(a):
                return (pre_res, False)
            res, rem = inner(index + 1, a, b, pre_res)

            if rem:
                if a[index] == "0":
                    if b[index] == "0":
                        return (f"1{res}", False)

                    return (f"0{res}", True)

                if b[index] == "0":
                    return (f"0{res}", True)

                return (f"1{res}", True)

            if a[index] == "0":
                if b[index] == "0":
                    return (f"0{res}", False)

                return (f"1{res}", False)

            if b[index] == "0":
                return (f"1{res}", False)

            return (f"0{res}", True)

        if len(a) == len(b):
            res, rem = inner(0, a, b, "")
            if rem:
                res = f"1{res}"
            return res
        s = abs(len(a) - len(b))

        if len(a) > len(b):
            res, rem = inner(0, a[s:], b, "")
            if rem:
                return self.addBinary(a[:s], "1") + res
            return a[:s] + res
        res, rem = inner(0, a, b[s:], "")

        if rem:
            return self.addBinary(b[:s], "1") + res

        return b[:s] + res


a = "1111110010101010101011"
b = "11010101011"

print(_Solution().addBinary(a, b))
print(Solution().addBinary(a, b))
