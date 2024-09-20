# Function to convert RGB to CMYK


def rgb_to_cmyk(red, green, blue):
    
    if red == 0 and green == 0 and blue == 0:
        return (0.0, 0.0, 0.0, 1.0)
    
    
    red = red / 255.0
    green = green / 255.0
    blue = blue / 255.0
    

    white = max(red, green, blue)
    

    
    cyan = (white - red) / white
    magenta = (white - green) / white
    yellow = (white - blue) / white
    
    
    black = 1 - white
    
    return (cyan, magenta, yellow, black)


red = int(input("Enter Red value (0-255): "))
green = int(input("Enter Green value (0-255): "))
blue = int(input("Enter Blue value (0-255): "))


cyan, magenta, yellow, black = rgb_to_cmyk(red, green, blue)


print(f"CMYK values are: C = {cyan:.2f}, M = {magenta:.2f}, Y = {yellow:.2f}, K = {black:.2f}")
