from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm
from django.core.paginator import Paginator

# Create your views here.

def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 8)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    return render(request, 'diary/page_list.html', {'page': page})

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


def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST': # if post method
        object.delete() # delete the page
        return redirect('page-list') # return diary list
    else: # if get method
                # return page_confirm_delete.html
                # put object for confirm title of delete
        return render(request, 'diary/page_confirm_delete.html', {'object': object})

def index(request):
    return render(request, 'diary/index.html')
