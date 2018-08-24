temp_num ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000, '亿':100000000}

def Solution(Str):
   total = 0
   r = 1
   num = ''
   for i in range(len(Str)-1, -1, -1):
      if '0' <= Str[i] <= '9':
         num = Str[i]+num
         continue
      val = temp_num.get(Str[i])
      if val >= 10 and i == 0:
         if val > r:
            r = val
            total = total + val
         else:
            r = r * val
      elif val >= 10:
         if val > r:
            r = val
         else:
            r = r * val
      else:
         total = total + r * val
   if num:
      return total+int(num)
   return total

if __name__ == "__main__":
    print(Solution('十三'))

