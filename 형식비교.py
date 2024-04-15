# 리스트와 튜플 생성
data_list = [1, 2, 3, 4, 5]
data_tuple = (1, 2, 3, 4, 5)

# 요소 출력
print("리스트 요소 출력:")
for element in data_list:
  print(element)

print("\n튜플 요소 출력:")
for element in data_tuple:
  print(element)

# 요소 변경
try:
  data_list[0] = 10
  print("리스트 첫 번째 요소 변경 성공:", data_list[0])

  data_tuple[0] = 10
  print("튜플 첫 번째 요소 변경 성공:", data_tuple[0])
except Exception as e:
  print("튜플 요소 변경 실패:", e)

# 요소 추가
try:
  data_list.append(6)
  print("리스트 요소 추가 성공:", data_list)

  data_tuple.append(6)
  print("튜플 요소 추가 실패:", data_tuple)
except Exception as e:
  print("튜플 요소 추가 실패:", e)

# 요소 삭제
try:
  del data_list[0]
  print("리스트 첫 번째 요소 삭제 성공:", data_list)

  del data_tuple[0]
  print("튜플 첫 번째 요소 삭제 실패:", data_tuple)
except Exception as e:
  print("튜플 요소 삭제 실패:", e)