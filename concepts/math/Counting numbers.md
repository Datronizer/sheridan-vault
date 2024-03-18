We often count numbers, but we never really stopped to consider why we do certain things. Like, have you ever stopped to question how/why the ones column resets to 0 whenever it hits 9? It's a very fundamental thing that we have internalized. Now it's time to externalize it and apply that to other number systems.
# Counting decimals
Decimal numbers start off easy, you start from 0, 1, 2,..., to 9. But when you hit 9, the ones [[Placevalues|placevalue]] cannot go any higher, so 9 resets to 0, and 1 is added to the tens column.

As you hit 19, this occurs again. 9 loops back to 0, and 1 gets added to the tens place and 1+1=2. So this becomes 20.

Keep doing this until you hit 99, and this happens again to replace the 1st 9 with a 0, add 1 to the tens column so 9 + 1 => 9 becomes 0 and 1 carries over to the hundreds column => 100.

We see that as we count, this often occurs whenever we hit a "limit" of how much a column can take and it "overflows" back to 0, and we carry the "overflow" (which is usually +1) to the column to the left. This is really easy to see in binary numbers.
# Counting binaries
Start with 0 -> 1. Now add 1 to 1. The limit is 1 so 1 + 1 = 0, carry 1 over to the left => 1 + 1 = 10.
Do this again. 10 + 1 = 11 => 11 + 1 = 12. 2 is an overflow of 0, 1 so 2 becomes 0, carry one over. 12 becomes 20. 2 becomes 0 again, carry 1 over. 20 = 100. 

> [!important] Keep in mind these are **binary** not **decimals**. The numbers are only representative and they DO NOT mean the same thing they mean in decimal values.
# Counting hexadecimals
Same things with hexadecimals btw, but I'm too lazy to write them all out. Refer to [this link](https://www.tutorialspoint.com/computer_logical_organization/hexadecimal_arithmetic.htm).
# Conclusion
We see that as we hit the limit of a column, the max permutations within that limit is always the same as the power of the [[Placevalues|placevalue]] of the limit you're trying to reach.