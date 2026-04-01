# ***LinkedList***

## 노드와 연결
배열 리스트는 내부에 배열을 사용해서 데이터를 보관하고 다음과 같은 단점을 가진다.
- 사용하지 않는 공간의 낭비
- 중간에 데이터 추가 시 공간 확보를 위해 기존 데이터들을 밀어내는 비용
  
이 문제 해결을 위해 노드를 만들고 연결을 하는 LinkedList 방식이 생겨났다.
  
```java
public class Node {
    Object item;
    Node next;
}
```
`item` 에 본인의 데이터를 집어 넣고 `next` 는 다음 노드의 참조값을 넣는다.  

![LinkedList](/properties/LinkedList.png)
  
코드는 다음과 같다.
  
```java
public class Node {
    Object item;
    Node next;

    public Node(Object item) {
        this.item = item;
    }
}

public class NodeMain1 {
    public static void main(String[] args) {
        Node first = new Node("A");
        first.next = new Node("B");
        first.next.next = new Node("C");
    }
}
```

## 노드와 연결2
출력값을 깔끔하게 하기 위해 `toString()` 을 오버라이딩 해보자.

```java
public class Node {
    Object item;
    Node next;

    public Node(Object item) {
        this.item = item;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node x = this;
        sb.append("[");
        while (x != null) {
            sb.append(x.item);
            if (x.next != null) {
                sb.append("->");
            }
            x = x.next;
        }
        sb.append("]");
        return sb.toString();
    }
}
//출력 : [A->B->C]
```
이전에 배웠던 StringBuilder 를 활용해서 출력값을 바꿨다.
  
## 노드와 연결3
다음과 같은 기능을 만들어보자.
- 모든 노드 탐색하기
- 마지막 노드 조회하기
- 특정 index의 노드 조회하기
- 노드에 데이터 추가하기

```java
public class NodeMain3 {

    public static void main(String[] args) {

        Node first = new Node("A");
        first.next = new Node("B");
        first.next.next = new Node("C");
    }

    //모든 노드 탐색
    private static void printAll(Node node) {
        Node x = node;
        while (x != null) {
            System.out.println(x.item);
            x = x.next;
        }
    }

    //마지막 노드 조회
    private static Node getLastNode(Node node) {
        Node x = node;
        while (x.next != null) {
            x = x.next;
        }
        return x;
    }

    //특정 index 조회
    private static Node getNode(int index, Node node) {
        Node x = node;
        for (int i = 0; i < index; i++) {
            x = x.next;
        }
        return x;
    }

    //데이터 추가
    private static void add(Node node, Object param) {
        Node lastNode = getLastNode(node);
        lastNode.next = new Node(param);
    }
}
```

## 직접 구현하는 연결 리스트

```java
public class MyLinkedListV1 {
    
    private Node first;
    private int size = 0;

    public void add(Object e) {
        Node newNode = new Node(e);
        if (first == null) {
            first = newNode;
        } else {
            Node lastNode = getLastNode();
            lastNode.next = newNode;
        }
        size ++;
    }
    
    private Node getLastNode() {
        Node x = first;
        while (x.next != null) {
            x = x.next;
        }
        return x;
    }

    private Object set(int index, Object element) {
        Node x = getNode(index);
        Object oldNode = x.item;
        x.item = element;
        return oldNode;
    }

    public Object get(int index) {
        Node x = getNode(index);
        return x.item;
    }

    public Node getNode(int index) {
        Node x = first;
        for (int i = 0; i < index; i++) {
            x = x.next;
        }
        return x;
    }

    public int indexOf(Object o) {
        int index = 0;
        for (Node x = first; x != null; x.next) {
            if (o.equals(x.item)) {
                return index;
            }
            index ++;
        }
        return -1;
    }

    public int size() {
        return size;
    }
}
```

## 직접 구현하는 연결 리스트2 - 추가와 삭제
특정 위치의 데이터를 추가하고 삭제하는 기능을 추가하자 !

```java
public void add(int index, Object o) {
    Node newNode = new Node(o);
    if (index == 0) {
        newNode.next = first;
        first = newNode;
    } else {
        Node oldValue = getNode(index - 1);
        newNode.next = oldValue.next;
        oldValue.next = newNode;
    }
    size++;
}

public Object remove(int index) {
    Node removeNode = getNode(index);
    Object removedItem = removeNode.item;
    if (index == 0) {
        Node oldValue = first;
        first = first.next;
        return oldValue;
    } else {
        Node prev = getNode(index - 1);
        prev.next = removeNode.next;
    }
    removeNode.item = null;
    removeNode.next = null;
    size--;
    return removedItem;
}
```

## BigO 성능 정리표
![BigO](/properties/BigOArrayvsLinked.png)
  
**참고 - 이중 연결 리스트**  
이중 연결 리스트는 노드를 앞 뒤로 연결하는 리스트로 성능을 더 개선할 수 있다.
```java
public class Node {
    Object item;
    Node next;
    Node prev;
}

// 마지막 노드를 참조하는 연결 리스트
public class LinkedList {
    private Node first;
    private Node last;
    private int size = 0;
}
```

## 직접 구현하는 연결 리스트4 - 제네릭 도입
지금까지 만든 연결리스트는 타입 안전성이 부족하다.  
예를 들어 연결 리스트 중간 노드의 item 에 의도치 않은 값이 들어가면 메서드에서 값을 반환하지 못하거나
변수에 값을 담을 때 컴파일 에러가 발생할 것이다.  
이를 제네릭을 이용해 안정시킬 수 있다.
