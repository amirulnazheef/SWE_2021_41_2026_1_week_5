def isHappy(n):
  temp = n
  while temp >= 10:
    sum = 0
    while temp > 0:
      digit = temp % 10
      sum += (digit ** 2)
      temp //= 10
    temp = sum

  if temp == 1:
    return True
  else:
    return False

if __name__ == "__main__":
  sample0_output = isHappy(19)
  sample1_output = isHappy(2)

  with open("/app/bind_mount/output.txt", "w") as f:
    f.write(f"19: {sample0_output}\n")
    f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")