from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from board.models import *
from django.views.generic import *
from .forms import BoardForm


class Index(TemplateView):
    template_name = 'board_class/index.html'


class BoardList(ListView):
    template_name = 'board_class/list.html'
    context_object_name = 'boards'

    def get_queryset(self):
        boards = Board.objects.all()
        return boards


class BoardDetail(DetailView):
    model = Board
    template_name = 'board_class/detail.html'


class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'board_class/create.html'
    success_url = reverse_lazy('board_class:list')

    def form_valid(self, form):
        board_post = form.save(commit=False)
        user = User.objects.get(id=1)  # 임시
        board_post.user = user
        board_post.save()
        return super().form_valid(form)


class BoardUpdate(UpdateView):
    model = Board
    fields = ['title', 'content']
    template_name = 'board_class/update.html'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy('board_class:detail', kwargs={'pk': pk})


class BoardDelete(DeleteView):
    model = Board
    success_url = reverse_lazy('board_class:list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

