from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from .forms import SearchForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'


class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('編集権限がありません。')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class DeleteViews(LoginRequiredMixin, generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')


def search(request):
    article = None
    searchform = SearchForm(request.GET)

    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        articles = Article.objects.filter(content__icontains=query)
        
    return render(request, 'bbs/results.html', {'articles': articles, 'seachform': searchform})
