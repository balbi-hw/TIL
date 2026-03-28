# ***TIME***

## 날짜와 시간 라이브러리가 필요한 이유?
1. **날짜와 시간 차이 계산**  
특정 날짜에서 다른 날짜까지의 정확한 일수를 계산하는건 생각보다 복잡하다. ( 정말로.. 네이버 시간 계산기가 괜히 있는게 아니다. )
2. **윤년 계산**  
윤년은 보통 4년에 한 번 이라고 알고 있지만 100년 단위일 때는 윤년이 아니며 또 400년 단위일 때는 다시 윤년이다.  
ex) 2024년 1월 1일에서 2024년 3월 1일까지 > 2024년은 윤년이라 2월이 29일까지라는 점을 고려해야 한다.
3. **썸머타임(DST) 변환**  
우리나라에서는 시행하지 않지만 일광절약시간을 적용하는 나라는 시기에 따라 그 값을 고려해야한다.
4. **타임존 계산**  
`ZD` 에 따른 `ZT` 계산을 해야한다.

## 자바 날짜와 시간 라이브러리 표
![표](/properties/DateTimeTable.png)

- 원문: https://docs.oracle.com/javase/tutorial/datetime/iso/overview.html


### **LocalDate, LocalTime, LocalDateTime**
- *LocalDate*: 날짜만 표현할 때 사용. 년, 월, 일을 다룬다.
- *LocalTime*: 시간만을 표현할 때 사용. 시, 분, 초를 다룬다.
- *LocalDateTime*: 위의 둘을 합한 개념이다.
  
Local 은 세계 시간대를 고려하지 않아 ZD 적용이 안된다는 뜻이다.
  
**LocalDate**
> 주의! - 모든 날짜 클래스는 불변이기 때문에 변경이 발생하면 새 객체를 생성해 반환하므로 반환값을 반드시 받아야한다.  
[예시 코드](../javamidlecture/src/time/LocalDateMain.java)
- now(): 현재 시간을 기준으로 객체를 생성한다.
- of(): 특정 날짜를 기준으로 객체를 생성한다. 년, 월, 일을 인수로 받는다.
- plusDays(): 특정 일 수를 더한다. 다양한 plusXxx() 메서드가 있다.
  
**LocalTime**
[예시 코드](../javamidlecture/src/time/LocalTimeMain.java)
- plusSecond(): 특정 초를 더한다.
  
**LocalDateTime**
[예시 코드](../javamidlecture/src/time/LocalDateTimeMain.java)
- 날짜( LocalDate ) 와 시간 ( LocalTime ) 을 toXxxx() 메서드로 분리할 수 있다.
- LocalDateTime.of(localDate, localTime): 날짜와 시간을 사용해 LocalDateTime을 만든다.
- isBefore(): 다른 날짜시간과 비교한다. 현재 날짜보다 이전이라면 true를 반환한다.
- isAfter(): 다른 날짜시간과 비교한다. 현재 날짜보다 이후이라면 true를 반환한다.
- isEqual(): 다른 날짜시간과 비교한다. 날짜시간이 같다면 true를 반환한다.
  
isEqual() vs equals()  
- isEqual() 는 단순히 비교 대상이 시간적으로 같으면 true 를 반환한다. 객체가 다르고 타임존이 달라도 오직 시간만 비교한다.
- equals() 는 객체의 타입, 타임존 등등 내부 필드를 모두 비교해 모두 같아야 true 를 반환한다.


### **ZonedDateTime, OffsetDataTime**
- *ZonedDateTime*: 시간대를 고려한 날짜와 시간을 표현할 때 사용한다. ZD를 적용한다.
  - ex) 2013-11-21T08:20:30.213+9:00[Asia/Seoul]
  - +9:00 은 ZT를 표현하고 오프셋이라고 한다.
  - 뒤의 Asia/Seoul 은 타임존이라고 하며 이를 알면 오프셋과 썸머타임에 대한 정보를 알 수 있다.
  - 썸머타임 DST를 적용한다.
- *OffsetDateTime*: 시간대를 고려한 날짜와 시간을 표현할 때 사용한다. 타임존은 없고 오프셋만 포함한다.
  - ex) 2013-11-21T08:20:30.213+9:00
  - 썸머타임 DST를 적용하지 않는다.
  
`ZoneDateTime`은 타임존이 있어 DST 처리가 가능하지만 `OffsetDataTime`은 그렇지 않다.
  
**ZoneDateTime**
자바는 타임존을 ZoneId 클래스로 제공한다.
[예시 코드](../javamidlecture/src/time/ZoneIdMain.java)
- ZoneId.systemDefault(): 시스템이 사용하는 기본 ZoneId를 반환한다.
- ZoneId.of(): 타임존을 직접 제공해서 ZoneId 를 반환한다.
ZoneId 는 내부에 썸머타임, UTC와의 오프셋 정보를 포함하고 있다.
  
ZoneDateTime 은 LocalDateTime 에 시간대 정보인 ZoneId 가 합쳐진 것이다.
```java
import java.time.ZoneId;

public class ZonedDateTime {
  private final LocalDateTime dateTime;
  private final ZoneOffset offset;
  private final ZoneId zone;
}
```
[예시 코드](../javamidlecture/src/time/ZonedDateTimeMain.java)
- withZoneSameInstant(ZoneId): 타임존을 변경한다. 그에 맞추어 시간도 함께 변경된다.

**OffsetDateTime**
LocalDateTime에 UTC 오프셋 정보인 ZoneOffset이 합쳐진 것이다.
```java
public class OffsetDateTime {
    private final LocalDateTime dateTime;
    private final ZoneOffset offset;
}
```
[예시 코드](../javamidlecture/src/time/OffsetDateTimeMain.java)

**참고** 
ZonedDateTime이나 OffsetDateTime은 글로벌 서비스를 하지 않으면 잘 사용하지 않는다. 따라서 너무 깊이 파기 보다는
대략 이런 것이 있다 정도만 학습해도 좋다. 글로벌 서비스를 하게 되면 그때 학습해도 된다.

### **Year, Month, YearMonth, MonthDay**
년 월 년월 달일을 각각 다룰 때 사용한다. 자주 사용하지는 않는다.  
DayOfWeek 과 같이 월, 화, 수, 목, 금, 토, 일 을 나타내는 클래스도 있다.

### **Instant**
UTC를 기준으로 하는 시간의 한 지점을 나타낸다. Instant는 날짜와 시간을 나노초 정밀도로 표현하며 1970년 1월 1일 0시 0분 0초를 기준으로
경과한 시간으로 계산된다.  
**Instant 내부에는 초 데이터만 들어있다. (나노초 포함)**  
따라서 날짜와 시간을 계산에 사용할 때는 적합하지 않다.
  
```java
public class Instant {
    private final long second;
    private final int nanos;
}
```
**참고 - Epoch 시간**
Epoch time 또는 Unix timestamp 는 컴퓨터에서 시간을 나타내는 방법 중 하나이다.  
Instant는 이 Epoch time 을 다루는 클래스이다.

- 장점:
  - 시간대 독립성: Instant는 UTC를 기준으로 하므로, 시간대에 영향을 받지 않는다. 이는 전 세계 어디서나 동일한 시점을 가리키는데 유용하다.
  - 고정된 기준점: 모든 Instant는 1970년 1월 1일 UTC를 기준으로 하기 때문에, 시간 계산 및 비교가 명확하고 일관된다.
- 단점:
  - 불친절함: Instant 는 기계적 시간 처리에는 적합하지만, 사람이 읽고 이해하기에는 직관적이지 않다.
  - 시간대 정보 부재: Instant 에는 시간대 정보가 포함되어 있지 않아 특정 지역의 날짜와 시간으로 변환하려면 추가 작업이 요구된다.
- 사용 예:
  - 전 세계적인 시간 기준 필요
  - 시간대 변환 없이 시간 계산 필요
  - 데이터 저장 및 교환: 데이터 베이스에 날짜와 시간 정보를 저장하거나 다른 시스템과 날짜와 시간 정보를 교환할 때 Instant를 사용하면 모든
  시스템에서 동일한 기준점을 사용하므로 데이터의 일관성을 유지하기 쉽다.
    
[예시 코드](../javamidlecture/src/time/InstantMain.java)
- ofEpochSecond(): 에포크 시간을 기준으로 Instant를 생성한다. 0초를 선택하면 에포크 시간은 1970년 ... 를 생성한다.
- getEpochSecond(): 에포크 시간을 기준으로 흐른 초를 반환한다.


### **Period, Duration**
시간은 크개 두 개의 개념으로 나뉜다.
- 특정 시점의 시간 (시각)
- 시간의 간격 (시간)
Period, Duration 은 시간을 표현하는 데 사용된다.  
시간의 간격은 영어로 amount of time 으로 불린다.
  
![표](/properties/PeriodDuration.png)
  
**Period**  
두 날짜 사이의 간격을 년, 월, 일 단위로 나타낸다.  
```java
public class Period {
    private final int years;
    private final int months;
    private final int days;
}
```  
[예시 코드](../javamidlecture/src/time/PeriodMain.java)
- 2030년 1월 1일에 10일을 더하면 2030년 1월 11일이 된다. 라고 표현할 때 특정 날짜에 10일이라는 기간을 더할 수 있다.
- 2023년 1월 1일과 2023년 4월 2일간의 차이는 3개월 1일이다. 라고 표현할 때 날짜의 차이를 구하면 기간이 된다.
  - Period.between(startDate, endDate) 와 같이 특정 날짜의 차이를 구하면 Period가 반환된다.

**Duration**  
두 시간 사이의 간격을 시, 분, 초 단위로 나타낸다.  
```java
public class Duration {
    private final long seconds;
    private final int nanos;
}
```
내부에서 초를 기반으로 시, 분, 초를 계산해서 사용한다.
[예시 코드](../javamidlecture/src/time/DurationMain.java)
- 1:00 에 30분을 더하면 1:30 이 된다. 라고 할 때 이 시간의 간격을 더할 수 있다.
- Duration.between(start, end) 와 같이 특정 시간의 차이를 구하면 Duration 이 반환된다.


## 크로노 유닛과 크로노 필드, 그리고 그 이외의 내용들
- 김영한의 실전 자바 중급 1편 - 날짜와 시간 pdf 파일을 살펴보자.