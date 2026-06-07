from tensorflow.keras.models import load_model
from django.conf import settings

import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os
from NeuroSpark.settings import BASE_DIR

model_paths={
    'Tumor':os.path.join(settings.BASE_DIR,'static', 'models', 'tumor_xception.h5'),
    'Stroke':os.path.join(settings.BASE_DIR,'static','models','stroke_xception.h5'),
    'Scelerosis':os.path.join(settings.BASE_DIR,'static','models','MS_xception.h5'),
    'Alzehimer':os.path.join(settings.BASE_DIR,'static','models','Alzehimer_xception.h5'),
    'All':os.path.join(settings.BASE_DIR,'static','models','Combined_Model_xception.h5'),
    'Hemmorahage':os.path.join(settings.BASE_DIR,'static','models','Haemorrage_xception.h5')
}



resize_size=(240,240)

def getImage(img_path):
    image = cv2.imread(img_path)
    image = Image.fromarray(image, 'RGB')
    image = image.resize(resize_size)
    image = np.array(image)
    return image


def showPredictionStatistics(img_path, predictions, class_names, size=resize_size):
    plt.figure(figsize=(10, 10))  
    img = getImage(img_path)
    probs = list(predictions[0] * 100)
    labels = class_names
    
    plt.subplot(2, 1, 1)  
    plt.imshow(img)
    plt.axis('off')
    
    plt.subplot(2, 1, 2)  
   
    bars = plt.barh(labels, probs)
    plt.xlabel('Percentage', fontsize=16)  
    plt.xticks(fontsize=12)  
    plt.yticks(fontsize=12)  
    ax = plt.gca()
    ax.bar_label(bars, fmt='%.2f')

    # Save the plot as an image file
    plot_path = os.path.join(BASE_DIR, 'static', 'images', "plot.png")
    plt.tight_layout() 
    plt.savefig(plot_path)

    return plot_path