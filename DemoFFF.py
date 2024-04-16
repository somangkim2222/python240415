data = "   spam and ham  "
result = data.strip()
print(data)
print(result)
result = result.replace("spam", "spam egg")
print(result)
print(result.split())
result2 = ":)".join(result)
print(result2)


#정규표현식
import re
result = re.search("[0-9]*th", "35th")
print(result.group())

result = re.search("\d[4]","올해는 2024년")
print(result.group())

result = re.search("\d[5]","우리 동네는 52100")
print(result.group())