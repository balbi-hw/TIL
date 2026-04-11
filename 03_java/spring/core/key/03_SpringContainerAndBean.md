# ***스프링 컨테이너와 스프링 빈***

아래 내용들의 실제 코드는 [bean-find](/src/test/java/hello/core/beanfind) 에 모두 있다! (XML 제외)

## 스프링 컨테이너 생성
```java
ApplicationContext applicationContext = 
        new AnnotationConfigApplicationContext(AppConfig.class);
```
타입명이 엄청 길다!  
여기서 `ApplicationContext` 스프링 컨테이너라고 하고 이는 인터페이스이다.  
스프링 컨테이너는 XML 또는 에노테이션 기반의 자바 설정 클래스로 만들 수 있다. 하지만 XML 로 만드는 방식은 알아보지 않겠다! 나중에 필요하면 찾아보자.  
자바 설정 클래스를 기반으로 `ApplicatipmContext`를 만들어보자.
- `new AnnotationConfigApplicationContext(AppConfig.class)` 이 클래스는 `AnnotationContext` 인터페이스의 구현체이다.
  
> 참고!  
> 더 정확히는 스프링 컨테이너를 부를 때 `BeanFactory`, `ApplciationContext`로 구분해서 이야기 한다. 하지만 `BeanFactory`를 직접 사용하는 경우가 거의 없어 보통 `ApplicationContext`를 스프링 컨테이너라고 이야기한다.
  
컨테이너를 공부하며 일종의 `Map`이라는 느낌을 받았다. 컨테이너는 Map이고 Bean은 Key, 빈에 들어가는 객체는 Value 인 느낌.
```java
new AnnotationConfigApplicationContext(AppConfig.class)
```
이 생성자를 통해 만들어지는 객체는 `AppConfig` 스프링 컨테이너 안에 Map으로 생성된다. 그리고 AppConfig 안의 Bean 으로 등록된 메서드들의 이름이 Key로 저장되고 그 메서드의 결과가 Value 가 된다.  
그래서 메서드의 이름이 같으면 Map 의 Key 값이 같아지는 것과 같으므로 에러가 발생한다 !
  
이후 스프링 컨테이너는 이 AppConfig Map 정보를 활용해 DI를 진행한다.
  
## 컨테이너의 빈 조회
- 모든 빈 출력
  - `ac.getBeanDefinitionNames()`: 스프링에 등록된 모든 빈 이름을 조회한다.
  - 'ac.getBean()': 빈 이름으로 빈 객체를 조회한다.
- 애플리케이션 빈 출력
  - 스프링 내부에서 사용되는 빈을 제외하고 커스텀 빈만 출력하자!
    - `ac.getRole(ROLE_APPLICAION)`: 커스텀 빈
    - `ac.getRole(ROLE_INFRASTRUCTURE)`: 스프링 내부 빈

### 빈 조회 - 기본
가장 기본적인 빈 조회 방법이다.
- `ac.getBean(빈이름, 타입)`
- `ac.getBean(타입)`
- 조회 대상 빈이 없으면 `NoSuchBeanDefinitionException` 에러가 발생한다.

### 빈 조회 - 같은 타입이 둘 이상일 때
- 타입으로 조회 시 같은 타입이 둘 이상이면 오류가 발생한다. 이럴 때는 이름 인자를 넣어주자.
- `ac.getBeansOfType()` 을 사용하면 해당 타입의 모든 빈을 조회할 수 있다.

### 빈 조회 - 상속관계
- 부모 타입을 조회하면 자식 타입도 모두 함께 조회한다. -> `Object`를 조회하면 모든 스프링 빈이 튀어나온다. ( 코드 확인 [상속](/src/test/java/hello/core/beanfind/ApplicationBeanContextExtendsFindTest.java))

### BeanFactory 와 ApplicationContext
자바답게 이 컨테이너 또한 객체지향 원칙을 준수하는데 컨테이너의 최상위 인터페이스는 `BeanFactory`이다. 모든 빈을 관리하고 조회하며 `getBean()`을 포함해 지금까지 사용한 대부분의 기능은 이 `BeanFactory`에서 제공한다.  
그 밑에 `ApplicationContext` 인터페이스가 존재하는데 팩토리의 기능을 모두 상속받아 제공한다. 구분해둔 이유는 다음과 같다.
- 메시지소스를 활용한 국제화: 한국에선 한국, 영어권에선 영어 제공
- 환경변수: 로컬, 개발, 운영등을 구분해서 처리
- 애플리케이션 이벤트: 이벤트를 발행하고 구독하는 모델을 편리하게 지원
- 편리한 리소스 조회: 파일, 클래스패스, 외부 등에서 리소스 조회
  
`BeanFactory`를 직접 사용할 일은 거의 없고 부가기능이 포함된 `ApplcationContext`를 주로 사용한다. 이 둘을 스프링 컨테이너라고 칭한다. ( 보통 ApplicationContext )

## 다양한 설정 형식 지원 - Java, XML 등
스프링 컨테이너는 다양한 형식의 설정 정보를 받아들일 수 있도록 유연하게 설계되어있다.
- 자바, XML, Groovy 등등
  
우선 자바만 사용한다고 생각해도 된다! XML 관련 코드는 따로 작성해두지 않았다. 필요할 때 찾아보자!
  
그럼 어떻게 이런 다양한 형식을 지원할까? 바로 `BeanDefinition`이라는 추상화가 끼어있기 때문이다. 역시 추상화!  
쉽게 이야기하면 역할과 구현을 개념적으로 나눈 것이다. 다양한 설정 정보를 읽고 그 정보를 `BeanDefinition`으로 변환한다. 그리고 스프링 컨테이너는 오직 이 `BeanDefinition` 만 알고 있다.  
다행히도 이를 직접 정의하거나 사용할 일은 없을 거라고 한다.