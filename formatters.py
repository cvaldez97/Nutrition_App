def format_height(height):
    feet = int(height) // 12
    inches = int(height) % 12

    return f"Height: {feet} ft {inches} in ({int(height)} in)"