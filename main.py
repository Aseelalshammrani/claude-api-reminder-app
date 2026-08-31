def greeting():
    print("Hi there")


def calculate_pi(precision=5):
    """
    Calculate pi to the specified number of decimal digits.
    Uses the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        precision: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Pi calculated to the specified precision
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        x_squared = x * x
        numerator = x
        
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * numerator / (2 * n + 1)
            numerator *= x_squared
        
        return result
    
    # Number of terms needed for desired precision
    # More terms = better accuracy
    num_terms = 100 if precision <= 5 else precision * 20
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi_over_4 = 4 * arctan(1/5, num_terms) - arctan(1/239, num_terms)
    pi_value = 4 * pi_over_4
    
    # Round to the specified precision
    return round(pi_value, precision)