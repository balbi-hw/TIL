REMOTE 추가
git remote add [name] [URL]

이후
git fetch [name]
을 통해 브랜치 정보를 가져와 local 에도 tracking branch 를 만들 수 있음

위 두 가지를 한 번에 진행
git remote add [-f] [name] [URL]

태그 정보까지 가져옴
git remote add [--tags] [name] [URL]


remote 를 여러개 관리하면서 용도에 맞게 사용할 수 있을 것 같다.
원본 repo 에 backup 등의 commit 이 쌓이는 게 싫어서 방법을 찾아본건데
원본 repo 를 fork 하고 private 으로 설정하면 아무 걱정 없이 backup 을 할 수 있을 것 같다.
