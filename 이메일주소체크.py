import re

def check_email(email):
    # 이메일 패턴 정의
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # 정규표현식을 사용하여 이메일 주소 체크
    if re.match(pattern, email):
        return True
    else:
        return False

# 새로운 샘플 이메일 주소
email_samples = [
    "user@example.com",
    "example.user@domain.co.kr",
    "user123@test-mail.com",
    "test.email@example.com",
    "invalid_email.com",
    "another.example@test",
    "user@domain",
    "user@.com",
    "@example.com",
    "user123@.co.kr"
]

# 각 이메일 주소를 체크하고 결과 출력
for email in email_samples:
    if check_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is an invalid email address.")
