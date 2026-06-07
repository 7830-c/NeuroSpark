from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .pred_models import *
from django.conf import settings
import os


@login_required(login_url='/auth/login')
def imageUplaoder(request,disease_name):
    if request.method == 'POST' and request.FILES.get('mri_image'):
        image_file = request.FILES['mri_image']

        img_path = os.path.join(settings.BASE_DIR, 'static','images', image_file.name)  # Specify the path where you want to save the image
        with open(img_path, 'wb') as f:
            for chunk in image_file.chunks():
                f.write(chunk)

        model = load_model(model_paths[disease_name])
        
        img = getImage(img_path)
        predictions = model.predict(np.expand_dims(img, axis=0))
        index=np.argmax(predictions[0])

        class_dict={
            'Alzehimer':['Mild Demented', 'Moderate Demented', 'Non Demented', 'Very Mild Demented'],
            'Tumor':['Glioma', 'Meningioma', 'No Tumor', 'Pituitary'],
            'Stroke':['Normal', 'Stroke'],
            'Scelerosis':['Control-Axial', 'Control-Sagittal', 'MS-Axial', 'MS-Sagittal'],
            'Hemmorahage':['Hemmorahage','Normal'],
            'All':['Control-Axial (Multiple Scelerosis)','Control-Sagittal (Multiple Scelerosis)','Hemmorahage','MS-Axial (Multiple Scelerosis)','MS-Sagittal (Multiple Scelerosis)','Mild Demented (Alzheimer)','Moderate Demented (Alzheimer)','Normal','Stroke','Very Mild Demented (Alzheimer)','Glioma (Brain Tumor)','Meningioma (Brain Tumor)','Pituitary (Brain Tumor)']
        }
        plot_path = showPredictionStatistics(img_path,predictions,class_dict[disease_name])
       
        os.remove(img_path)
 
        return render(request,'report.html',{'prediction':(class_dict[disease_name])[index],"img_plot":plot_path});
        
    else:
        return render(request,'upload_file.html',{})



