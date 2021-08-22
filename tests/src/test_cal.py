from app.src.cal import calculator

cal1 = calculator()

def test_add():
	assert cal1.add(1, 1) == 2
	assert cal1.add(1, 2) == 3

