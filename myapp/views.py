from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.

def Home(request):

    if request.method == 'POST':
        # print("POST Method")
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            # print("Valid form")
            form.save()
    form=ImageForm()
    img=Image.objects.all()

    return render(request,"home.html",context={"form":form,"img":img})