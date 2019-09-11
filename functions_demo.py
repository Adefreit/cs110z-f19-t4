def area_square(width, height):
    return width * height

def area_triangle(base, height):
    return 0.5 * base * height

def bytes_to_bits(number_of_bytes):
    return number_of_bytes * 8

if __name__ == '__main__':
    print("The area of a 5x5 square is", area_square(5, 5))
    print("The area of a 2x3 triangle is", area_triangle(2, 3))
    print("There are", bytes_to_bits(1024), "bits in a kilobyte (I'll teach you that later)")