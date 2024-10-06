def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero and non-numeric input errors.
    
    Args:
        numerator (str): The numerator as a string (to be converted to float).
        denominator (str): The denominator as a string (to be converted to float).
    
    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Attempt to convert the inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division, check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Return the result of the division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        # Handle the case where inputs are not numeric
        return "Error: Please enter numeric values only."
