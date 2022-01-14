# 프로그래머스 No.81301 숫자 문자열과 영단어

def solution(s):
  answer = ""
  number_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

  temp = ""
  for char in s:
    if char.isdigit():
      answer += char
      temp = ""
    else:
      temp += char

    if temp in number_dict:
      answer += number_dict[temp]
      temp = ""
  return int(answer)


s = "one4seveneight"
print(solution(s))