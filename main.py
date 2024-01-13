import cv2

img = cv2.imread('people.png')

print(type(img))
print(img.shape)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
