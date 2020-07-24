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
      if bunnies == 0: complexity O(1)
        return 0    complexity of O(1)

      return 2 + bunnyEars(bunnies-1)  complexity of O(n)

    O(1) + O(1) + O(n)
      -->

      I beleive the complexity of C is O(n). As bunnies grows by one it will cause one additional recursion on the return meaning this should grow linerarly. That means it should be O(n)

## Exercise II

I think a very good way of handling this problem would be to attack it with the equivilent of a binary search tree. You can consider the "list" already ordered as the height will increase by one for each floor you move up. We'll be looking for the first floor where an egg breaks.

The quickest way to eastablish the first floor where an egg breaks is to eliminate the most possible choices at a time (just like a binary search tree). You start by going to the middle floor of the tower and dropping an egg there. If it breaks, you can eliminate all of the floors above and set this one as the break point. If it does not break, you can eliminate all of the floors below and set this as the afe point.

After you have the info on the first drop you then pick the middle of the remaining and repeat this process until the break point and the safe point are next to each other.
