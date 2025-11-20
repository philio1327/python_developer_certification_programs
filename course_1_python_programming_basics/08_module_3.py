def calculate_diameter_circle(radius: float) -> float:
    """
    Returns the diameter given the radius as input.

    Args:
        radius: The radius of the circle (float)

    Returns:
        The diameter of the circle (float)

    Raises:
        ValueError, TypeError
    """

    if not isinstance(radius, float) and not isinstance(radius, int):
        return "Please input a number"

    if radius < 0:
        return -1

    return 2 * radius


# Test values
print(f"Radius: 7, Diameter: {calculate_diameter_circle(7)}")
print(f"Radius: 2.5, Diameter: {calculate_diameter_circle(2.5)}")
print(f"Radius: 0, Diameter: {calculate_diameter_circle(0)}")
print(f"Radius: -3, Diameter: {calculate_diameter_circle(-3)}")
print(f"Radius: 'Hello', Diameter: {calculate_diameter_circle('Hello')}")
print(f"Radius: 1000_000, Diameter: {calculate_diameter_circle(1000_000)}")
