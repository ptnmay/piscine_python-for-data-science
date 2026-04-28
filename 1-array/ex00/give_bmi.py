# =========================
# take list of height and weigth to calculate bmi
# =========================


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values from height and weight lists.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("BMI: List only")
    if len(height) != len(weight):  # -> calcualte bmi and for zip
        raise ValueError("BMI: height and weight should have same length.")

    bmi = []

    for h, w in zip(
        height, weight
    ):  # zip -> loop 2 list in the same time. match value in same index.
        if not isinstance(h, (int, float)) or not isinstance(
            w, (int, float)
        ):  # check value of list -> int or float
            raise TypeError("BMI: Number only.")
        if h <= 0 or w <= 0:
            raise ValueError(
                "BMI: height and weight must be greater than 0."
            )  # h must be > 0 but w = 0 is not makesence
        res = w / (h**2)  # -> h power of 2
        bmi.append(res)
    return bmi


# ========================
# check if bmi > limit = true, else false
# ========================


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Compare BMI values with a limit.
    """
    res = []
    if not isinstance(bmi, list):
        raise TypeError("Limit: List only")
    if not isinstance(limit, int):
        raise TypeError("Limit: Number only.")
    for i in bmi:
        if not isinstance(i, (int, float)):
            raise TypeError("Limit: number only")
        res.append(i > limit)  # return List boolean
    return res


# ==================
# My test
# ==================
# from give_bmi import give_bmi, apply_limit

# tests = [
#     # height weight limit. list in tupe in list
#     ([1.8], [75.8], 20), # 1 value
#     ([1.8, 1.5], [75, 49.5], 20), #2 value int float
#     ([1.8, 1], [75, 49.5], 90), # 2 value change limit
#     ([1.4, "k"], [75, 49.5], 20), # error: not number
#     ([1.5, 0], [75, 49.5], 20), # error: h or w = 0
#     (33, [75, 49.5], 20), # error not list
#     ([1], [75, 49.5], 20), # error: h and w not same length
#     ([1.8, 1], [75, 49.5], "s"), # error: limit not number
# ]

# i = 1
# for case in tests:
#     try:
#         bmi = give_bmi(case[0], case[1])
#         print(f"Test {i} |", bmi, apply_limit(bmi, case[2]))
#     except Exception as e:
#         print(f"Test {i} |", "Error", e)
#     i += 1
