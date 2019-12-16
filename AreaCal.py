shape = input("Choose the Shape: ")
area = int

if shape == 'square':
    height = input("Please enter height ")
    h = int(height)
    width = input("Please enter width ")
    w = int(width)
    print("Area of Triangle is height x width")
    area = h * w
    print(area)

if shape == 'triangle':
    print("Area is 2r x pi")
else :
    print("Area is non-sense")