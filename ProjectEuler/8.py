"""The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843
8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557
6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749
3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776
6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397
5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474
8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586
1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408
0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606
0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?"""

import itertools

temp_list = []
product_list = []
my_list = (itertools.islice('7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450', 0, None))


def my_func():
    max_numb = 0
    for i in my_list:
        temp_list.append(int(i))
    while len(temp_list) >= 13:
        temp_numb = temp_list[0] * temp_list[1] * temp_list[2] * temp_list[3] * temp_list[4] * temp_list[5] * temp_list[6] * temp_list[7] * temp_list[8] * temp_list[9] * temp_list[10] * temp_list[11] * temp_list[12]
        if temp_numb > max_numb:
            max_numb = temp_numb
        temp_list.pop(0)
    print(max_numb)


my_func()

