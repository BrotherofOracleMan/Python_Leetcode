class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        prime_number_list = [True] * (n +1)
        primes = 0
        if n <= 2:
            return 0
        prime_number_list[0] = False
        prime_number_list[1] = False
        
        for factor in range(2,int(ceil(sqrt(n)))):
            if prime_number_list[factor] == True:
                for i in range(2*factor, n+1,factor):
                    prime_number_list[i] = False
        
        for i in range(n):
            if prime_number_list[i] == True:
                primes +=1
            
        return primes
        """        

        sieve = [True]*(n+1)
        if n == 0 or n == 1:
            return 0
        sieve[0] = False
        sieve[1] = False
        for factor in range(2, int(ceil(n**.5))):
            if sieve[factor]:
                for multiple in range(2*factor, n+1, factor):
                    sieve[multiple] = False
        print(sieve)
        count = 0
        for i in range(n):
            if sieve[i]:
                count += 1
        print(count)
        return count
        """
        
