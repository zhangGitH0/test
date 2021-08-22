from app.src.cal import calculator

cal1 = calculator()

def test_add():
	assert cal1.add(1, 1) == 2
	assert cal1.add(1, 2) == 3

def test_subtract():
	assert cal1.subtract(3, 2) == 1
	assert cal1.subtract(5, 9) == -4
