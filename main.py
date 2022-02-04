# 백준 No.15650 N과 M(2)

def dfs(index, number_list, numbers):
  
  if len(numbers) == m:
    for number in numbers:
      print(number, end = " ")
    print("")
    return
  
  for i in range(index, len(number_list)):
    numbers.append(number_list[i])
    dfs(i + 1, number_list, numbers)
    numbers.pop()

n, m = map(int, input().split())
dfs(0, list(range(1,n+1)), [])
