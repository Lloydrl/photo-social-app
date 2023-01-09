from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user    #gives the current logged in user for the new post
            new_post.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'posts/create.html', {'form':form})

