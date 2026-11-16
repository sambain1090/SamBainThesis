def piCamPositionEstimate():
    """
    Estimate the position of the Pi Camera based on its mounting configuration.
    This function calculates the camera's position in the world coordinate system
    using known parameters such as mounting height, tilt angle, and field of view.

    Returns:
        tuple: A tuple containing the estimated (x, y, z) coordinates of the camera.
    """
    # Define known parameters
    mounting_height = 1.5  # meters
    tilt_angle = 30  # degrees
    field_of_view = 90  # degrees

    # Convert tilt angle to radians for calculations
    tilt_angle_rad = math.radians(tilt_angle)

    # Calculate the position of the camera in world coordinates
    x_position = 0  # Assuming camera is centered on the x-axis
    y_position = mounting_height * math.tan(tilt_angle_rad)
    z_position = mounting_height

    return (x_position, y_position, z_position)

def maixSenseEstimate():
    """
    Estimate the position of the MaixSense camera based on its mounting configuration.
    This function calculates the camera's position in the world coordinate system
    using known parameters such as mounting height, tilt angle, and field of view.

    Returns:
        tuple: A tuple containing the estimated (x, y, z) coordinates of the camera.
    """
    # Define known parameters
    mounting_height = 1.2  # meters
    tilt_angle = 25  # degrees
    field_of_view = 80  # degrees

    # Convert tilt angle to radians for calculations
    tilt_angle_rad = math.radians(tilt_angle)

    # Calculate the position of the camera in world coordinates
    x_position = 0  # Assuming camera is centered on the x-axis
    y_position = mounting_height * math.tan(tilt_angle_rad)
    z_position = mounting_height

    return (x_position, y_position, z_position)