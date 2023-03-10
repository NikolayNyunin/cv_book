import numpy as np
import cv2 as cv

drawing = False  # True, если кнопка мыши нажата
mode = False  # если True, будут рисоваться прямоугольники (на 'm' смена)
ix, iy = -1, -1


# функция, реагирующая на мышь
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:  # если пользователь нажал на левую кнопку мыши
        drawing = True
        ix, iy = x, y  # меняем значения координат на текущие
    elif event == cv.EVENT_MOUSEMOVE:  # если пользователь передвинул мышь
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:  # если пользователь отжал левую кнопку мыши
        drawing = False
        if mode:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)  # устанавливаем обработчик мыши для указанного окна
while 1:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k != 255:
        print(k)
    if k == ord('m'):  # при нажатии 'm' сменяем фигуры которые мы будем рисовать (круги/прямоугольники)
        mode = not mode
    elif k == 27 or k == 113:  # 27 соответствует кнопке 'esc', 113 соответствует кнопке 'q' (при нажатии выходим)
        break
cv.destroyAllWindows()
