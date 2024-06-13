from django.shortcuts import render
from .models import Article

def articles(request):
    # grabs all articles from the model table
    articles = Article.objects.all().order_by('date')
    
    return render(request, 'articles/articles.html', {
        'articles': articles
    })