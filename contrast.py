import cv2 as cv

# This code is performing image processing operations to convert an input image into a sketch-like
# image. Here is a breakdown of the code:
image1 = cv.imread(r"C:\Users\f_kaf\Downloads\images.jpg")
window_name = 'Original image'

# `cv.imshow(window_name, image1)` is a function from the OpenCV library that displays an image in a
# window with the specified window name. In this case, it is displaying the original image `image1` in
# a window with the name `window_name`.
cv.imshow(window_name, image1)

# The code `grey_img = cv.cvtColor(image1,cv.COLOR_BGR2GRAY)` is converting the original color image
# `image1` from the BGR color space to grayscale. This is done using the `cv.cvtColor()` function from
# the OpenCV library, with the `cv.COLOR_BGR2GRAY` flag indicating the conversion from BGR to
# grayscale.
grey_img = cv.cvtColor(image1,cv.COLOR_BGR2GRAY)
invert = cv.bitwise_not(grey_img)

# The code `blur = cv.GaussianBlur(invert, (21, 21), 0)` is applying a Gaussian blur to the inverted
# grayscale image `invert`. The `cv.GaussianBlur()` function from the OpenCV library is used for this
# purpose. The `(21, 21)` parameter specifies the size of the kernel used for blurring, and `0`
# indicates that the standard deviation of the Gaussian kernel is automatically calculated based on
# the kernel size.
blur = cv.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv.bitwise_not(blur)
sketch = cv.divide(grey_img, invertedblur, scale=256)

cv.imwrite('sketch.png', sketch)

image = cv.imread('sketch.png')

window_name = 'Sketch image'

cv.imshow(window_name, image)
#wait to user to press any key (necessary to avoid Python Kernel from crashing)
cv.waitKey(0)
