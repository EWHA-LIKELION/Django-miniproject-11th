# Django-miniproject-11th

miniproject

기존 CRUD 구현된 BLOG에서 댓글기능 추가

Django 댓글구현
https://0ver-grow.tistory.com/956
댓글 목록 html참고
https://glory-summer.tistory.com/189

댓글 리스트 불러오기, 댓글목록
특정 객체를 찹조하는 (foreign)하는 모델(comment)의 집합 (_set.all)불러오기, blog를 참조하는 모든 댓글 목록 불러오기,for in 

*{% for comment in blog_detail.comment_set.all}
 cf) {% for comment in blog.comment_set.all %} (o)

<views.py>
def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)

    comment_form = Commentform()

    return render(request,'detail.html',{'blog':blog_detail, 'comment_form':comment_form})

-return render에서 blog:blog_detail
