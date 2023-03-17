def add_nums(*nums: int) -> int:
    ans = 0
    for i in nums:
        ans = _add(ans, i)
    return ans


def _add(a, b):
    return a + b


# def add_nums(*nums: int) -> int:
#     return sum(nums)
