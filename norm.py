from __future__ import print_function
import cv2 as cv
import argparse


def normalizada(imagem):
    """coloque o nome da imagem exemplo 'imagem.jpeg' no argumento"""
    parser = argparse.ArgumentParser(description='Code for Histogram Equalization tutorial.')
    parser.add_argument('--input', help='Path to input image.', default= imagem)
    args = parser.parse_args()
    src = cv.imread(cv.samples.findFile(args.input))

    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)

    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(src)

    cv.imshow('Source image', src)
    cv.imshow('Equalized Image', dst)
    cv.waitKey()

    parser = argparse.ArgumentParser(description='não precisa de descrição')
    parser.add_argument('--input', help='Path to input image.', default='lena_gray.jpeg')
    args = parser.parse_args()
    src = cv.imread(cv.samples.findFile(args.input))

    if src is None:
        print('Could not open or find the image:', args.input)
        exit(0)

normalizada('image1.png')
normalizada('lena_gray.jpeg')