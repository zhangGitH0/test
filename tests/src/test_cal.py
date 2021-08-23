from app.src.cal import calculator

cal1 = calculator()

def test_add():
	assert cal1.add(1, 1) == 2
	assert cal1.add(1, 2) == 3

def test_divide():
	assert cal.divide(2, 1) == 2
	assert cal.divide(9, 3) == 3
	assert cal.divide(0, 9) == 0
def test_subtract():
	assert cal1.subtract(3, 2) == 1
	assert cal1.subtract(5, 9) == -4

def test_divide()
	assert cal1.divide(0, 1) == 0
	assert cal1.divide(9, 3) == 3
	assert cal1.divide(7, 0) == 0

