import cv2
import numpy as np

# 適當的閾值，用於區分黑點
threshold_value = 100

# 創建一個視窗以顯示圖像
cv2.namedWindow("Black Dots Detection", cv2.WINDOW_NORMAL)

# 創建一個空白的陣列來存放黑點位置
black_dot_positions = []

while True:
    # 讀取圖片
    image = cv2.imread('test1.jpg')

    # 轉換圖片為灰度
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化處理以偵測黑點
    ret, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # 找到黑點的輪廓
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 清空黑點位置陣列
    black_dot_positions = []

    # 存放每個黑點的位置
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            black_dot_positions.append((cX, cY))

    # 在原圖上繪製黑點位置
    for position in black_dot_positions:
        cv2.circle(image, position, 5, (0, 0, 255), -1)  # 在圖片上繪製紅色圓圈

    # 顯示圖像
    cv2.imshow("Black Dots Detection", image)

    # 按下ESC鍵退出迴圈
    key = cv2.waitKey(1)
    if key == 27:
        break

# 釋放資源和關閉視窗
cv2.destroyAllWindows()
