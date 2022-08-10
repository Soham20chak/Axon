import imp
import cv2
import easygui
import numpy as np
import imageio 
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

def upload():
    ImagePath= easygui.fileopenbox()
    cartoonify(ImagePath)
def cartoonify(ImagePath):
    originalmage= cv2.imread(ImagePath)
    

