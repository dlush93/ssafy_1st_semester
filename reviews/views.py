from django.shortcuts import render,redirect,get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
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
                return redirect('reviews:index')

        else:
            form=ReviewForm()
        context={
            'form':form
        }
        return render(request,'reviews/form.html',context)
    else:
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
                return redirect('reviews:review_detail',review_id)
        else:
            form = ReviewForm(instance=review)

        context={
            'form':form
        }
        return render(request,'reviews/form.html',context)
    else:
        return redirect('reviews:review_detail',review_id)

@require_POST
def review_delete(request,review_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            review = get_object_or_404(Review,pk=review_id)
            if request.user == review.user:
                review.delete()
                return redirect('reviews:review_list')
            else:
                return redirect('reviews:review_detail',review_id)
    else:
        return redirect('reviews:review_detail',review_id)


def like(request,review_id):
    review = get_object_or_404(Review,id=review_id)
    if request.user.is_authenticated:
        if request.user == review.user:
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