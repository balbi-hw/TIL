# join
words = ['Python', 'is', 'awesome']

sentence1 = ' '.join(words)
sentence2 = '-'.join(words)

print(sentence1)  # Python is awesome
print(sentence2)  # Python-is-awesome

#---------------------------------------------------------#

# split

# split 을 사용만해봤지 인수로 sep, maxsplit 을 넣을 수 있다는 점은 처음 알았다.

# 1. 공백을 기준으로 분리 (기본 동작)
# - 여러 개의 공백도 하나로 처리하며, 앞뒤 공백은 무시함
text = '  Hello    Python  '
print(text.split())
# 결과: ['Hello', 'Python’]


# 2. 특정 문자를 기준으로 분리
# - 지정한 문자를 기준으로 '엄격하게' 분리함 (빈 문자열 발생 가능)
data = '10,20,,30'
print(text.split(sep=','))
# 결과: ['10', '20', '', '30']


# 3. 분할 횟수 제한 (maxsplit)
# - 앞에서부터 1번만 자르고 나머지는 그대로 둠
path = 'User/admin/documents'
print(path.split('/', maxsplit=1))
# 결과: ['User', 'admin/documents']

#---------------------------------------------------------#

# strip

# 마지막 항목은 처음 알았다.
# 잘 사용하면 f-string이나 여러곳에 편하게 사용할 수 있을 듯

# 사용자 입력 등에서 불필요한 공백이 포함된 경우
text = '   Hello    World   '

# 1. 아무것도 지정하지 않으면 '공백(띄어쓰기, 탭, 엔터)'을 제거
clean_text = text.strip()

print(clean_text)
# 결과: 'Hello    World'
# (주의: 문자열 중간의 공백은 제거되지 않음)


# 2. 제거할 문자를 지정하는 경우
text = '!!!Hello World!!!'
print(text.strip('!'))
# 결과: 'Hello World'


# [심화] 문자열 집합으로 제거 (순서 상관 없음)
# 'w', '.', 'c', 'o', 'm' 중 하나라도 양쪽 끝에 있으면 계속 제거
url = 'www.example.com'
print(url.strip('w.com'))
# 결과: 'example'
# (왼쪽의 'www.'과 오른쪽의 '.com'이 모두 제거됨)