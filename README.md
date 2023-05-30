# Django-miniproject-11th

read.me 파일 열심히 작성해주세요!

## 1. 코드 Summary
### [CRUD 구현]
이전에 스터디에서 기획했던 게시판의 CRUD 기능을 구현했습니다. 지난 세션에서 진행했던 블로그 프로젝트 틀을 가지고 와 models.py의 Blog 클래스에 type이라는 새로운 변수를 추가했습니다. 게시글 제목 앞에 뮤지컬 제목을 붙여 게시글을 분류하기 위해 추가했습니다. 최종 목표는 type과 title을 각각 필터로 하여 검색하는 기능을 추가하는 것 인데, 아직 검색 기능은 구현하지 못했습니다.

### [해시태그 수정] 실패
지난 1:N과 M:N 세션에서 배웠던 코드를 가져와 댓글과 해시태그 기능을 구현했습니다. 게시물 수정에 해시태그 수정 기능을 추가하고 싶었으나, 수정 페이지에서 게시물의 해시태그가 로딩되지 않습니다. 아마도 해시태그 중복 제거 코드 어딘가와 충돌한 것이 아닐까...하는 추측과 함께 문제 해결 노력중입니다.

### [댓글 수정] 구현중...
댓글 수정을 위해 views.py 파일에 comment_detail과 update_comment 함수를 새로 만들고 comment_id를 사용해 수정하도록 함수를 정의했습니다. 그리고 urls에 'update_comment/<int:comment_id>'를 추가하고 update_comment.html 파일도 만들었습니다. 그러나 안됩니다... 뭐가 문제일까요... -> 230525 forms.py의 BlogForm에 hashtag를 추가하지 않았었다는걸 발견했습니다. 그러나 이게 연관이 있는지 왜 없는지는 모르겠습니다 -> BlogForm에 hashtag를 추가했더니 submit해도 저장이 안되는 문제가 생겼습니다. 다시 지워서 문제는 해결했지만 이유를 모르겠습니다...
230530 성공!!!!! 이전 실패의 이유는 다음과 같습니다
1) comment_detail에 게시물 id를 받아오지 않았었던것...
2) views.py의 update_comment의 redirect로 'detail' 페이지로 돌아갈 때 blog_id만 받으면 되는데 comment_id까지 받아온 것...
3) update_comment.html의 input 태그의 name을 'username'으로 views.py와 통일하지 않았음!!


### [유저인증과 확장]
세션에서 진행한 코드 참고하여 구현했습니다.
회원가입 진행 시에 비밀번호 조건을 만족하지 않으면 오류가 뜹니다.
 
### [html/css 기록]
지난 세션에서 진행한 것과 조금 다르게 html에서 a 태그가 아닌 button을 사용했는데, 이이에 링크를 추가하는 과정에서 그 뒤에 페이지 인덱스를 붙이는 방법을 찾지 못해 오류를 해결하지 못한 상태입니다. html 오류가 뜨지만 실행은 정상적으로 되고있습니다.

230524 static css 적용이 안되는 문제 발생. Nav Bar를 가져오며 외부 css와 충돌한 것으로 예상되고, css 적용 우선순위를 통해 해결 시도했습니다. css 코드에 !important를 추가하고, 웹페이지에서 F12로 개발자 도구를 켜 '캐시 비우기 및 강력 새로고침'을 했더니 문제 해결되었습니다. !important는 필수가 아닌 것 같습니다. 외부 css에 써있지 않은 내용에 대해서는 !important 없어도 적용 되는 것 같습니다 아마도... 그런데 hr은 또 투명도가 이상하게 적용되는데 이거 문제 이유는 모르겠다만 html은 이제 그만 하고싶어요... -> base.html에 load static해서 해결했으나 중간중간 선 굵기가 다른 애들보다 조금 더 굵어지는 문제가 발생(랜덤하게 문제가 발생해서 아마 외부 css와 static css 사이의 충돌이 아닐까 예상하지만 잘 모르겠습니다...)

230524 new.html에 이미지 업로드 기능을 추가했더니 submit이 안되는 문제 발생. 이건 위에서 이야기했던 BlogForm에 hashtag를 추가해서 발생한 문제였습니다.

230524 이미지 업로드는 되는데 디테일 페이지에서 이미지가 보이지 않는 문제가 발생. 이건 form.as_p 사용을 하지 않아서 기존 세션 코드대로 따라가면 당연히 문제가 생기는 부분이었음. new.html에서 파일 input 받을 때 설정한 name을 detail.html에서 img src에 그대로 써줘야함! 레퍼런스로 참조한 코드의 new.html에의 사진 파일 input태그의 name은 'imgfile'이었고, 세션 코드를 참조한 detial.html의 img태그의 src는 'blog.photo.url'이었는데 -> new.html의 input태그 name을 photo로 바꾸었더니 해결됨


<br/>

## 2. Key Changes 

230516 - 1:N과 M:N 기능을 추가했습니다.
230525 - static & media 기능을 추가했습니다.
230525 - 유저 로그인, 로그아웃, 회원가입 기능을 추가했습니다.
230527 - blog의 views.py에서 수정 시에 메인 홈으로 리디렉트 되던 것을 디테일 페이지로 리디렉트되도록 수정했습니다.

<br/>

## 3. Reference
https://www.nextree.co.kr/p8428/
html의 form을 수정하기 위해 참조했습니다.

이외에는 지난 세션 자료 참고했습니다.

https://korinkorin.tistory.com/31
댓글 수정 기능 구현을 위해 참조했습니다.

https://think0wise.tistory.com/24
static css 문제 해결을 위해 우선순위 내용 참조했습니다.

https://fhaktj8-18.tistory.com/entry/django-imgfile
new.html에서 {{ form.as_p }}를 사용하지 않고 이미지 파일을 가져오는 input 코드를 참조했습니다.

https://ho-ding.tistory.com/19
css가 적용되지 않는 문제를 해결하기 위해 참조했습니다.

https://free-eunb.tistory.com/42
홈에 static 사진 넣기 위해 참조했습니다.

<br/>

## 4. Report
https://equatorial-chard-0cb.notion.site/add643d0b1d74ca48c0ddafe3d9dec5f
