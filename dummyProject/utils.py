def get_cropped_img(img, x_min, y_min, x_end, y_end):
    cropped_img = img[y_min:y_end,x_min:x_end]
    return cropped_img

def multiply_by_three(x):
    return x * 3

def add5(x):
    return x + 5

def sub10(x):
    return x - 10


#here is a comment