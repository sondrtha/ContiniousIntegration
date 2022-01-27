import utils

# def test_get_cropped_img():   # this unit test requires opencv to be installed, if opencv is install you can uncomment this line
#     import cv2
#     import os
#     dirname = os.path.dirname(__file__)
#     file_path = dirname + "//kingsdomino.jpg"
#     img = cv2.imread(file_path)
#     cropped_img = utils.get_cropped_img(img, 0,0,600,500)
#     h,w = cropped_img.shape[:2]
#     assert(w == 600)
#     assert(h == 500)


def test_multiply_by_three():
    assert(utils.multiply_by_three(5) == 15)
    assert(utils.multiply_by_three(10) == 30)

def test_add5():
    assert(utils.add5(10) == 15)


def test_add_should_fail():
    assert(utils.add5(5) == 15)

# def test_add_should_also_fail():            #if this functions is uncommented, this unit test will also be ran.
#     assert(utils.add5(5) == 15)

# a random comment, change and save this line (or make any other change) while running the main file
# so that the CI will run unit tests.   fdsas