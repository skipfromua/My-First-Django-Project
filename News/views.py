from django.shortcuts import render
from django.views import View
from .models import News, Commentary
from .forms import MessageForm
from django.contrib import auth
from django.core.paginator import Paginator


class MainView(View):

    def get(self, request):
        form = MessageForm()
        context = {
            'form': form,
            'username': auth.get_user(request).username
        }
        return render(request, 'News/index.html', context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'News/index.html')


class NewsView(View):
    model = News

    def get(self, request, page_number=1):
        news = News.objects.all()
        current_page = Paginator(news, 5)
        form = MessageForm()
        context = {
            'news': current_page.get_page(page_number),
            'form': form,
            'username': auth.get_user(request).username
        }
        return render(request, 'News/news.html', context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'News/news.html')


def commentary_view(request, pk):
    post = News.objects.get(id=pk)
    form = MessageForm()
    commentary = Commentary.objects.filter(news=pk)
    if request.POST:
        comment = Commentary(news=post, commentary_text=request.POST['commentary_text'], user=auth.get_user(request))
        comment.save()
    context = {
        'form': form,
        'post': post,
        'username': auth.get_user(request).username,
        'commentary': commentary
    }
    return render(request, 'News/post.html', context)
