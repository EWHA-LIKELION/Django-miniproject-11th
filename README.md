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

-요일을 기준으로 나눌지 온도를 기준으로 나눌지 모르겠음...
그리고 요일이나 온도를 기준으로 설정하면 글을 새로 쓰는 형태가 아니라 카테고리로 나누어서 고정시켜야 하는거 아닌가...?하는 생각
카테고리 만들어서 나누고 거기에 글을 추가하는 형식으로 의상 적고 댓글 남길 수 있게...? 아니면 댓글이 아니라 추천, 비추천 등 의견 표시 형태를 추가하는게 맞는건가 ㅠㅅ ㅠ

<feedback - 230404>
-체질 댓글쓰는거에 선택해서 
-기온별 추천옷차림도 추천
-사진도 같이 첨부
-사진을 올리면 카테고리 만들어서 옷 스타일 카테고리 구분해서 패션참고도 
-카테고리에 지역 다 넣어서 선택하게 하기 
-온도별로 선택해서 필터링 하는 거
