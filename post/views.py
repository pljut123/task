from django.contrib.auth.decorators import login_required
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.views.generic import ListView
from el_pagination.views import AjaxListView

from loginsys.models import MyUser
from post.forms import PostForm
from post.models import Post, Follows

try:
    from django.utils import simplejson as json
except ImportError:
    import json


@login_required
def addlike(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST.get('id', None)
        post = get_object_or_404(Post, id=id)

        if post.likes.filter(id=user.id).exists():

            post.likes.remove(user)

        else:

            post.likes.add(user)

    ctx = {'likes_count': post.total_likes}

    return HttpResponse(json.dumps(ctx), content_type='application/json')


def submit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            post_form = PostForm(data=request.POST)

            if post_form.is_valid():
                post = post_form.save(commit=False)

                post.author = request.user
                post.save()
                return redirect('/')
            else:
                return post_list(request, post_form)
    else:
        redirect('/auth/login.html')
    return redirect('/')


def follows(request):
    if request.method == "POST":
        user = request.user
        id = request.POST.get('id', None)
        author = Post.objects.get(id=id).author
        foll = Follows.objects.get_or_create(user=user)[0]
        foll.follows.add(author)
        message = 'Вы подписались на %s' %author.username

    ctx = {'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')



class post_list(AjaxListView):
    context_object_name = "posts"
    template_name = "post/post_list.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(post_list, self).get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context

class post_follow(ListView):
    context_object_name = "posts"
    template_name = "post/post_follow.html"

    def get_queryset(self):
        # self.foll = Follows.objects.get(id).follows
        # self.posts = Post.objects.filter(id=self.foll)
        return Post.objects.all().order_by('-created_date')

