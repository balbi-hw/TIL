package jpabook.jpashop.service;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@Transactional  // 데이터 변경은 트랜잭셔널 꼭 넣기
//@Transactional(readOnly = true)  // 쓰기보다 읽기가 많으니까 위에 이렇게 해두고 쓰기에만 따로 @Transactional 걸어줘도 됨
@RequiredArgsConstructor  // lombok 에서 required 가 걸려있는 필드의 생성자를 만들어줌 ( 밑의 생성자 생략 가능, 권장 )
public class MemberService {

    // 이전에 Spring 강의에서 말헀듯이 이렇게 Autowired 를 바로 걸어주는것 보다
    // 생성자 인젝션을 걸어주는게 더 좋다
//    @Autowired
    private final MemberRepository memberRepository;  // final 걸어주면 값 설정이 안되었을 때 컴파일 불가 ( 휴먼에러 방지 )
                                                      // required 를 걸어준다고 생각하자

    // 추후 테스트를 할 때 다른 DB로 갈아 끼워 넣기도 편하고 테스트 중간에
    // 다른 DB로 바뀔 염려도 없다 ( Setter Injection 의 단점 )
//    @Autowired  // 그리고 생성자가 하나만 있으면 어노테이션 생략 가능
//    public MemberService(MemberRepository memberRepository) {
//        this.memberRepository = memberRepository;
//    }

    // 회원 가입
    @Transactional  // 변경이니 어노테이션 // 위에 안쓸 때
    public Long join(Member member) {

        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {
        //EXCEPTION
        List<Member> findMembers = memberRepository.findByName(member.getName());
        if (!findMembers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        }
    }

    // 회원 전체 조회
    @Transactional(readOnly = true) // 변경 아니고 조회만 할 때는 readOnly true 해주면 최적화 해줌
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    @Transactional(readOnly = true)
    public Member findOne(Long memberId) {
        return memberRepository.findOne(memberId);
    }

    @Transactional
    public void update(Long id, String name) {
        Member member = memberRepository.findOne(id);
        member.setName(name);
    }
}
