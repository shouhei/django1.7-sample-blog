from django.shortcuts import render
from blogs.models import Post
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blogs/index.html')
    context = RequestContext(request, {
            'latest_post_list': latest_post_list,
    })
    return HttpResponse(template.render(context))
# Create your views here.

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blogs/detail.html', {'post': post})
