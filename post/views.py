from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from el_pagination.decorators import page_template
from el_pagination.views import AjaxListView
from loginsys.models import MyUser
from post.forms import PostForm
from post.models import Post



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



# def post_list(request, template='post/post_list.html'):

    # post_form = post_form or PostForm()
    # posts = Post.objects.all().order_by('-created_date')
    #
    # paginator = Paginator(posts, 10)  # Show 25 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #      posts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #      posts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     posts = paginator.page(paginator.num_pages)
    #
    #
    # return render(request,
    #     'post/post_list.html',
    #     {'post_form': post_form, 'next_url': '/post_list',
    #     'posts': posts,})

    #
    # context = {
    #     'posts': Post.objects.all(),
    # }
    # return render_to_response(
    #     template, context, context_instance=RequestContext(request))
# class post_list(AjaxListView):
#     context_object_name = "posts"
#     template_name = "post/post_list.html"
#
#     def get_queryset(self):
#         return Post.objects.all()
# @page_template('post/post_list_page.html')  # just add this decorator
# def post_list(request,
#         template='post/post_list.html', extra_context=None):
#     context = {
#         'post_list': Post.objects.all(),
#     }
#     if extra_context is not None:
#         context.update(extra_context)
#     return render(request,
#         template, context, context_instance=RequestContext(request))
class post_list(AjaxListView):

    context_object_name = "posts"
    template_name = "post/post_list.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(post_list, self).get_context_data(**kwargs)
        context['post_form'] = PostForm()
        return context