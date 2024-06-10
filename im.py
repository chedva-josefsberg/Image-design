from tkinter import filedialog
from tkinter.simpledialog import askstring
import cv2
import imageio

class MyImage:
    # כאן יכתבו כל הפונקציות שמטפלות בתמונה עצמה
    def __init__(self, path, nameWindow):
        self.nameWindow = nameWindow
        self.path = path
        self.image = imageio.imread(path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        self.image = cv2.resize(self.image, (800, 500))
        self.orig_image = self.image.copy()
        self.start_point = None
        self.end_point = None
        self.cropping = False
        self.show()

    def show(self):
        cv2.imshow(self.nameWindow, self.image)

    def add_text(self):
        text = askstring("Enter Text", "Enter the text you want to add:")
        if text:
            def add_text_event(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(self.image, text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
                    self.show()
        cv2.setMouseCallback(self.nameWindow, add_text_event)

    def filter(self):
        self.image = cv2.applyColorMap(self.image, cv2.COLORMAP_JET)
        self.show()

    def draw_rec(self):
        def draw_rect_event(event, x, y, flags, param):
            global ix, iy
            if event == cv2.EVENT_LBUTTONDOWN:
                # לחצנו על העכבר השמאלי
                # אנחנו רוצים להתחיל לצייר ריבוע
                ix = x
                iy = y

            elif event == cv2.EVENT_LBUTTONUP:
                # סיימנו לצייר
                cv2.rectangle(self.image, (ix, iy), (x, y), (100, 50, 200), 8)
                self.show()

        cv2.setMouseCallback(self.nameWindow, draw_rect_event)

    def cut(self):
        def cut_image(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                self.start_point = (x, y)
                self.cropping = True

            elif event == cv2.EVENT_MOUSEMOVE:
                if self.cropping:
                    self.image = self.orig_image.copy()
                    cv2.rectangle(self.image, self.start_point, (x, y), (0, 0, 255), 2)
                    self.show()

            elif event == cv2.EVENT_LBUTTONUP:
                self.end_point = (x, y)
                self.cropping = False
                cv2.rectangle(self.image, self.start_point, self.end_point, (0, 0, 255), 2)
                self.show()
                self.crop_and_save()

        cv2.setMouseCallback(self.nameWindow, cut_image)

    def crop_and_save(self):
        if self.start_point and self.end_point:
            x1, y1 = self.start_point
            x2, y2 = self.end_point
            cropped_image = self.orig_image[y1:y2, x1:x2]
            cv2.imshow('Cropped Image', cropped_image)
            cv2.imwrite('cropped_image.jpg', cropped_image)

    def rotate(self):
        angle = float(askstring("Enter Angle", "Enter the rotation angle:"))
        if angle:
            height, width = self.image.shape[:2]
            center = (width / 2, height / 2)
            rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            self.image = cv2.warpAffine(self.image, rotation_matrix, (width, height))
            self.show()

    def save_image(self, file_path):
            # תמיר את התמונה מתבנית BGR לתבנית RGB
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            # שמור את התמונה לקובץ באמצעות הספרייה imageio
            imageio.imwrite(file_path, image_rgb)
            print("Image saved successfully.")
    def run(self):
        while True:
            cv2.imshow(self.nameWindow, self.image)
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # Escape key
                break


        cv2.destroyAllWindows()
