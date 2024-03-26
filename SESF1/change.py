import numpy as np
import sum
def change(image1,image2,image,i,j,m,n):
    image_comp = image1
    image_change = image2
    k = 0
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i, j - 1, m, n) == sum.SF(
            image_change, i, j - 1, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i - 1, j, m, n) == sum.SF(
            image_change, i - 1, j, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i, j + 1, m, n) == sum.SF(
            image_change, i, j + 1, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i + 1, j, m, n) == sum.SF(
            image_change, i + 1, j, m, n):
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i+1,j+1,m,n)==sum.SF(image_change,i+1,j+1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i+1,j-1,m,n)==sum.SF(image_change,i+1,j-1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i-1,j+1,m,n)==sum.SF(image_change,i-1,j+1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i-1,j-1,m,n)==sum.SF(image_change,i-1,j-1,m,n) :
        k += 1
    if k >= 4:
        image[i * m:i * m + m, j * n:j * n + n] = image_change[i * m:i * m + m, j * n:j * n + n]


    image_comp = image2
    image_change = image1
    k = 0

    # else:
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i, j - 1, m, n) == sum.SF(
            image_change, i, j - 1, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i - 1, j, m, n) == sum.SF(
            image_change, i - 1, j, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i, j + 1, m, n) == sum.SF(
            image_change, i, j + 1, m, n):
        k += 1
    if sum.SF(image, i, j, m, n) == sum.SF(image_comp, i, j, m, n) and sum.SF(image, i + 1, j, m, n) == sum.SF(
            image_change, i + 1, j, m, n):
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i+1,j+1,m,n)==sum.SF(image_change,i+1,j+1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i+1,j-1,m,n)==sum.SF(image_change,i+1,j-1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i-1,j+1,m,n)==sum.SF(image_change,i-1,j+1,m,n) :
        k += 1
    if sum.SF(image,i,j,m,n)==sum.SF(image_comp,i,j,m,n) and sum.SF(image,i-1,j-1,m,n)==sum.SF(image_change,i-1,j-1,m,n) :
        k += 1
    if k >= 4:
        image[i * m:i * m + m, j * n:j * n + n] = image_change[i * m:i * m + m, j * n:j * n + n]
