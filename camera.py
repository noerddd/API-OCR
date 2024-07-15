import cv2

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    image_path = 'image.jpg'
    cv2.imwrite(image_path, frame)
    cam.release()
    return image_path
