from django.shortcuts import render, redirect
from crud.models import Article
from crud.forms import *
# Create your views here.

def article_func(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html', {'article':article})


def article_create(request):
    form = ArticleForm(request.POST or None, request.FILES)
    if request.method == "POST" and form.is_valid():
        instance = form.save (commit=False)
        instance.author = request.user
        instance.save()
        return redirect("article_func")
    form = ArticleForm()
    return render(request, "article_create.html", {"form": form})

def article_edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(request.POST or None, instance=article,)
    if form.is_valid():
        form.save()
        return redirect('article_detail', slug=request.POST.get("slug"))
    return render(request, 'article_edit.html', {"form":form, 'article':article})
    

def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method =='POST':
        article.delete()
        return redirect('article_func')
    return render(request, 'article_delete.html' ,{'article': article})

