import math
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def calculate_recovery_rqd(core_run_length, recovered_length, intact_pieces_length):
    """
    Calculate core recovery and RQD values based on drill core data.
    
    Args:
        core_run_length (float): Total length of the core run (m)
        recovered_length (float): Total length of core recovered (m)
        intact_pieces_length (float): Summed length of intact pieces >= 0.10m (m)
    
    Returns:
        tuple: (core_recovery_pct, rqd_pct, rqd_classification, recovery_classification)
               or error string if validation fails
    """
    # Validate inputs
    if recovered_length > core_run_length:
        return "Error: Recovered length cannot exceed core run length."
    
    if intact_pieces_length > recovered_length:
        return "Error: Sum of intact pieces cannot exceed recovered length."
    
    # Calculate core recovery percentage
    core_recovery_pct = (recovered_length / core_run_length) * 100
    
    # Calculate RQD percentage
    rqd_pct = (intact_pieces_length / core_run_length) * 100
    
    # Classify RQD according to Deere classification
    if rqd_pct <= 25:
        rqd_class = "Very Poor"
    elif rqd_pct <= 50:
        rqd_class = "Poor"
    elif rqd_pct <= 75:
        rqd_class = "Fair"
    elif rqd_pct <= 90:
        rqd_class = "Good"
    else:
        rqd_class = "Excellent"
    
    # Classify core recovery
    if core_recovery_pct < 75:
        recovery_class = "Poor"
    elif core_recovery_pct < 90:
        recovery_class = "Fair"
    elif core_recovery_pct < 95:
        recovery_class = "Good"
    else:
        recovery_class = "Excellent"
    
    return core_recovery_pct, rqd_pct, rqd_class, recovery_class


def create_rqd_gauge(rqd_value):
    """
    Creates a horizontal gauge image representing the RQD value.
    
    Args:
        rqd_value (float): RQD percentage (0-100)
    
    Returns:
        str: Path to the generated image file
    """
    # Create a new image with white background
    width, height = 500, 50
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Define colors for each quality band
    colors = [
        ((0, 25), (255, 0, 0)),      # Very Poor: Red
        ((25, 50), (255, 165, 0)),   # Poor: Orange
        ((50, 75), (255, 255, 0)),   # Fair: Yellow
        ((75, 90), (0, 255, 0)),     # Good: Green
        ((90, 100), (0, 0, 255))     # Excellent: Blue
    ]
    
    # Draw the colored bands
    for (start_pct, end_pct), color in colors:
        start_x = int((start_pct / 100) * width)
        end_x = int((end_pct / 100) * width)
        draw.rectangle([start_x, 0, end_x, height], fill=color)
    
    # Draw the indicator line at the RQD value position
    indicator_x = int((rqd_value / 100) * width)
    draw.line([(indicator_x, 0), (indicator_x, height)], fill='black', width=3)
    
    # Add text labels for each band
    font_size = 12
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Place labels at the center of each band
    for (start_pct, end_pct), color in colors:
        mid_pct = (start_pct + end_pct) / 2
        mid_x = int((mid_pct / 100) * width)
        label = f"{start_pct}-{end_pct}%"
        bbox = draw.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        draw.text((mid_x - text_width//2, height//2 - font_size//2), label, fill='black', font=font)
    
    # Save the image to a temporary file
    temp_path = "/tmp/rqd_gauge.png"
    img.save(temp_path)
    return temp_path
