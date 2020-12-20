from django.shortcuts import render,redirect,get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from dal import autocomplete
from movies.models import Movie
from django.contrib import messages
# Create your views here.


def index(request):
    reviews=Review.objects.order_by('-id')
    context={
        'reviews':reviews
    }
    return render(request,'reviews/index.html',context)



@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=ReviewForm(request.POST,request.FILES)

            if form.is_valid():

                review=form.save(commit=False)
                review.user=request.user
                review.save()
                messages.success(request,"성공적으로 작성이 완료되었습니다.")
                return redirect('reviews:index')

        else:
            form=ReviewForm()
        context={
            'form':form
        }
        return render(request,'reviews/form.html',context)
    else:
        messages.warning(request,"로그인을 해주세요")
        return redirect('reviews:index')



def review_detail(request,review_id):
    review=get_object_or_404(Review,id=review_id)
    form = CommentForm()
    context={
        'review':review,
        'form':form
    }
    return render(request,'reviews/detail.html',context)


@login_required
def review_update(request,review_id):
    review=get_object_or_404(Review,pk=review_id)
    if request.user == review.user:
        if request.method=='POST':
            form = ReviewForm(request.POST,instance=review)
            if form.is_valid():
                form.save()
                messages.success(request,"성공적으로 수정되었습니다.")
                return redirect('reviews:review_detail',review_id)
        else:
            messages.warning(request,"다시 입력하세요")
            form = ReviewForm(instance=review)

        context={
            'form':form
        }
        return render(request,'reviews/form.html',context)
    else:
        messages.warning(request,"작성자가 아닙니다.")
        return redirect('reviews:review_detail',review_id)

@require_POST
def review_delete(request,review_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            review = get_object_or_404(Review,pk=review_id)
            if request.user == review.user:
                review.delete()
                messages.success(request,"성공적으로 삭제되었습니다.")
                return redirect('reviews:index')
            else:
                messages.warnig(request,"다른 사용자의 글을 삭제 할 수 없습니다.")
                return redirect('reviews:review_detail',review_id)
    else:
        return redirect('reviews:review_detail',review_id)


def like(request,review_id):
    review = get_object_or_404(Review,id=review_id)
    if request.user.is_authenticated:
        if request.user == review.user:
            messages.info(request,"자기글에 좋아요를 누를수 없습니다.")
            return redirect('reviews:review_detail',review_id)
        else:
            if review.like_users.filter(id=request.user.id).exists():
                review.like_users.remove(request.user)
            else:
                review.like_users.add(request.user)
            return redirect('reviews:review_detail',review_id)
    else:
        return redirect('reviews:review_detail',review_id)


@login_required
def comments_create(request,review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user=request.user
            comment.save()
    return redirect('reviews:review_detail',review_id)

@login_required
def comments_delete(request,review_id,comment_id):
    comment=get_object_or_404(Comment,id=comment_id)
    if request.user == comment.user:
        if request.method=='POST':

            comment.delete()
            return redirect('reviews:review_detail', review_id)
    else:
        return redirect('reviews:review_detail', review_id)



class MovieAutocomp(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Movie.objects.all()
        if self.q:
            print(qs.values())
            qs = qs.filter(title__istartswith = self.q)
            print(qs)
        return qs