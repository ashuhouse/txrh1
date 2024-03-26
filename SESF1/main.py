import numpy as np
import cv2
import matplotlib.pyplot as plt

import change
import sum


# 展示图片，name表示窗口名字，image表示图片
def cv2_show(name, image):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)

    # 展示窗口等待时间，0表示任意键关闭窗口，
    # 其他数值表示毫秒后关闭窗口，如 cv2.waitKey(1000)表示1000毫秒后关闭窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#
#
m = int(input("请输入m\n"))
n = int(input("请输入n\n"))
TH = float(input("请输入TH\n"))
image1 = cv2.imread("1.png",0)
image2 = cv2.imread("2.png",0)
image11 = cv2.imread("1.png")
image22 = cv2.imread("2.png")
b1,g1,r1= cv2.split(image11)
b2,g2,r2= cv2.split(image22)


image = np.zeros_like(image1)
b = np.zeros_like(b1)
g = np.zeros_like(g1)
r = np.zeros_like(r1)

M = int(image.shape[0]/m)
N = int(image.shape[1]/n)
print(M)
print(N)

for i in range(M):
    for j in range(N):
        image1_sf = sum.SF(image1, i, j, m, n)
        image2_sf = sum.SF(image2, i, j, m, n)
        b1_sf = sum.SF(b1, i, j, m, n)
        g1_sf = sum.SF(g1, i, j, m, n)
        r1_sf = sum.SF(r1, i, j, m, n)
        b2_sf = sum.SF(b2, i, j, m, n)
        g2_sf = sum.SF(g2, i, j, m, n)
        r2_sf = sum.SF(r2, i, j, m, n)

        if b1_sf > b2_sf + TH:
            b[i * m:i * m+m, j * n:j * n + n] = b1[i * m:i * m+m, j * n:j * n + n]

        elif b1_sf < b2_sf - TH:
            b[i * m:i * m+m, j * n:j * n + n] = b2[i * m:i * m+m, j * n:j * n + n]

        else:
            b[i * m:i * m+m, j * n:j * n + n] = b1[i * m:i * m+m, j * n:j * n + n]/2+b2[i * m:i * m+m, j * n:j * n + n]/2
        if g1_sf > g2_sf + TH:
            g[i * m:i * m + m, j * n:j * n + n] = g1[i * m:i * m + m, j * n:j * n + n]

        elif g1_sf < g2_sf - TH:
            g[i * m:i * m + m, j * n:j * n + n] = g2[i * m:i * m + m, j * n:j * n + n]

        else:
            g[i * m:i * m + m, j * n:j * n + n] = g1[i * m:i * m + m, j * n:j * n + n] / 2 + g2[i * m:i * m + m,j * n:j * n + n] / 2
        if r1_sf > r2_sf + TH:
            r[i * m:i * m + m, j * n:j * n + n] = r1[i * m:i * m + m, j * n:j * n + n]

        elif r1_sf < r2_sf - TH:
            r[i * m:i * m + m, j * n:j * n + n] = r2[i * m:i * m + m, j * n:j * n + n]

        else:
            r[i * m:i * m + m, j * n:j * n + n] = r1[i * m:i * m + m, j * n:j * n + n] / 2 + r2[i * m:i * m + m,j * n:j * n + n] / 2

imagebefore=cv2.merge([b,g,r])



cv2.imwrite('before.png', imagebefore)
# f = np.copy(image)

for i in range(1,M-1):
    for j in range(1,N-1):
        change.change(b1, b2, b, i, j, m, n)
        change.change(g1, g2, g, i, j, m, n)
        change.change(r1, r2, r, i, j, m, n)






imageall=cv2.merge([b,g,r])
cv2_show("all",imageall)
cv2.imwrite('after1.png', imageall)
all=np.hstack((image11,image22,imageall))
cv2_show("all",all)

