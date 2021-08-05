from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm

# Create your views here.

def page_list(request):
    object_list = Page.objects.all()
    return render(request, 'diary/page_list.html', {'object_list': object_list})

def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object': object})

def info(request):
    return render(request, 'diary/info.html')

def page_create(request):
    if request.method == 'POST': 
        form = PageForm(request.POST) # make binding form the inserted value
        if form.is_valid(): #only when the data is validated
            new_page = form.save()  #data save and return saved data
        # new_page = Page( #post these data
        #     title=request.POST['title'],  
        #     content=request.POST['content'],
        #     feeling=request.POST['feeling'],
        #     score=request.POST['score'],
        #     dt_created=request.POST['dt_created']
        # )
        # new_page.save() # save on database
            return redirect('page-detail', page_id=new_page.id) #redirect to new page
    else:
        form = PageForm() #new empty form
    return render(request, 'diary/page_form.html', {'form': form})


def page_update(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=object.id)
    else:
        form = PageForm(instance=object)
    return render(request, 'diary/page_form.html', {'form': form})