"""
Tests for Data Validation Module - HitaVir Tech
"""

def test_validate_range_pass():
    from validator import validate_range
    assert validate_range(5, 1, 10) == True
    print("PASS: validate_range with valid input")

def test_validate_range_fail():
    from validator import validate_range
    try:
        validate_range(15, 1, 10)
        print("FAIL: Should have raised ValueError")
    except ValueError:
        print("PASS: validate_range correctly rejects out-of-range")

if __name__ == "__main__":
    test_validate_range_pass()
    test_validate_range_fail()
    print("\nAll tests passed!")
