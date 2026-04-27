# =========================
# take list of height and weigth to calculate bmi
# =========================


def give_bmi(height: list[int | float],
			 weight: list[int | float]) -> list[int | float]:
	if not isinstance(height, list) or not isinstance(weight, list):
		raise TypeError("List only")
	if len(height) != len(weight): #-> calcualte bmi and for zip
		raise ValueError("height and weight should have same length.")

	bmi = []

	for h, w in zip(height, weight): # zip -> loop 2 list in the same time. match value in same index.
		if not isinstance(h, (int, float)) or not isinstance(w, (int, float)): # check value of list -> int or float
			raise TypeError("Number only.")
		if h <= 0 or w <= 0:
			raise ValueError("height and weight must be greater than 0.") # h must be > 0 but w = 0 is not makesence
		res = w / (h ** 2) # -> h power of 2
		bmi.append(res)
	return bmi
