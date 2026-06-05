"""
Data Validation Module - HitaVir Tech
Validates data quality before loading into warehouse
"""

def validate_not_null(dataframe, columns):
    """Check that specified columns have no null values"""
    for col in columns:
        null_count = dataframe[col].isnull().sum()
        if null_count > 0:
            raise ValueError(f"Column '{col}' has {null_count} null values")
    return True

def validate_unique(dataframe, columns):
    """Check that specified columns have unique values"""
    for col in columns:
        dupes = dataframe[col].duplicated().sum()
        if dupes > 0:
            raise ValueError(f"Column '{col}' has {dupes} duplicates")
    return True

def validate_range(value, min_val, max_val):
    """Check that a value is within expected range"""
    if not (min_val <= value <= max_val):
        raise ValueError(f"Value {value} outside range [{min_val}, {max_val}]")
    return True

if __name__ == "__main__":
    print("Data Validator ready!")
    print("Modules: validate_not_null, validate_unique, validate_range")
