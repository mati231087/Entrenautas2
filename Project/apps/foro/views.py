from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post, Comment
from .forms import CommentForm

class PostView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        form = CommentForm()
        return render(request, 'foro/post.html', {'post': post, 'comments': comments, 'form': form})

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', post_id=post_id)
        else:
            comments = Comment.objects.filter(post=post)
            return render(request, 'foro/post.html', {'post': post, 'comments': comments, 'form': form})
        
def home(request):
    return render(request, "foro/index.html")

class CommentView(View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, 'foro/comment.html', {'comment': comment})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        # Lógica para procesar el formulario de edición de comentarios
        return redirect('comment', comment_id=comment_id)

