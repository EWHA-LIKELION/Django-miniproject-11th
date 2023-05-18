# Django-miniproject-11th

read.me 파일 열심히 작성해주세요!

## 1. 코드 Summary
이전에 스터디에서 기획했던 게시판의 CRUD 기능을 구현했습니다. 지난 세션에서 진행했던 블로그 프로젝트 틀을 가지고 와 models.py의 Blog 클래스에 type이라는 새로운 변수를 추가했습니다. 게시글 제목 앞에 뮤지컬 제목을 붙여 게시글을 분류하기 위해 추가했습니다. 최종 목표는 type과 title을 각각 필터로 하여 검색하는 기능을 추가하는 것 인데, 아직 검색 기능은 구현하지 못했습니다.

지난 세션에서 진행한 것과 조금 다르게 html에서 a 태그가 아닌 button을 사용했는데, 이이에 링크를 추가하는 과정에서 그 뒤에 페이지 인덱스를 붙이는 방법을 찾지 못해 오류를 해결하지 못한 상태입니다. html 오류가 뜨지만 실행은 정상적으로 됩니다.

지난 1:N과 M:N 세션에서 배웠던 코드를 가져와 댓글과 해시태그 기능을 구현했습니다. 게시물 수정에 해시태그 수정 기능을 추가하고 싶었으나, 수정 페이지에서 게시물의 해시태그가 로딩되지 않습니다. 아마도 해시태그 중복 제거 코드 어딘가와 충돌한 것이 아닐까...하는 추측과 함께 문제 해결 노력중입니다.

댓글 수정을 위해 views.py 파일에 comment_detail과 update_comment 함수를 새로 만들고 comment_id를 사용해 수정하도록 함수를 정의했습니다. 그리고 urls에 'update_comment/<int:comment_id>'를 추가하고 update_comment.html 파일도 만들었습니다. 그러나 안됩니다... 뭐가 문제일까요...

<br/>

## 2. Key Changes 

230516 - 1:N과 M:N 기능을 추가했습니다.

<br/>

## 3. Reference
https://www.nextree.co.kr/p8428/
html의 form을 수정하기 위해 참조하였습니다.

이외에는 지난 세션 자료 참고했습니다.

<br/>

## 4. Report
https://equatorial-chard-0cb.notion.site/add643d0b1d74ca48c0ddafe3d9dec5f
