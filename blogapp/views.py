from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog

from .forms import BlogPost
# Create your views here.


def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def summary(self):
    return self.body[:100]

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})