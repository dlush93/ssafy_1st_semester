from django.shortcuts import render, redirect
from .models import Review
# Create your views here.
def review_list(request):
    reviews=Review.objects.all()
    context={
        'reviews':reviews,
    }
    return render(request,'community/review_list.html',context)

def new_review(request):
    return render(request,'community/new_review.html')

def create_review(request):
    review=Review()
    review.title=request.GET.get('title')
    review.content=request.GET.get('content')
    review.rank=request.GET.get('rank')
    review.save()
    return redirect(f'/community/review_detail/{review.id}')   ### 각자 detail에 들어가는 redirect
    # return redirect('/community/')  ### 전체리스트로 돌아가는 redirect
    # return render(request,'community/create_review.html')

def review_detail(request,review_id):
    review=Review.objects.get(id=review_id)
    context={
        'review':review,
    }
    return render(request,'community/review_detail.html',context)
    
