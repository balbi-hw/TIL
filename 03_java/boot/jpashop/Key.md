## 목차
  - [API 개발 시작](#api-개발)



# API 개발

- API Request 의 Response 로 Entity 를 보내면 안된다.  
Entity 의 필드에 변동이 생기면 API 스펙이 달라지기 때문이다. Entity 는 변하기 쉬운 데이터인데 이게 변할 때마다 API 스펙에 변화가 생기면 API 를 사용하는 입장에서 사용하기 매우 까다로워진다.

- 엔티티에 프레젠테이션 계층을 위한 로직이 추가되면 안된다.  
위와 같은 맥락으로 API 는 매우 다양하게 만들어지는데 한 API 를 위해 Entity 에 변화가 생기면 다른 API 에서 문제가 생긴다.

- **따라서 API 요청 스펙에 맞추어 별도의 DTO 를 파라미터로 받아야한다.**

[참고](/src/main/java/jpabook/jpashop/api/MemberApiController.java)
