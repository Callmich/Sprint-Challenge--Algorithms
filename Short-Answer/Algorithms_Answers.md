#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
<!-- a = 0  complexity of O(1)
    while (a < n * n * n): complexity of O(3n)
      a = a + n * n     complexity of O(1)
      
      O(1) + (O(n) * O(1)) --> 

    I believe the first question has a complexity of O(n). When the lines are multiplied the value of O(3n) can be reduced to just O(n)

b)
<!-- sum = 0   complexity of O(1)
    for i in range(n): complexity of O(n)
      j = 1 Complexity O(1)
      while j < n: Complexity of O(log n)??
        j *= 2 complexity of O(1)
        sum += 1 complexity of O(1)
        
    O(1) + O(n) *(O(1) + (O(logn) * O(1) + O(1)))
        --> 
    I believe the complexity of this is going to be O(n log n). The while loop increases the amount of functions completed but not on a 1:1 basis so it is not going to be another O(n). So the O(n) is multiplied by the O(log n) which gives us O(n log n).

c)
<!-- def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) -->

## Exercise II


