primes :: [Integer]
primes = 2 : 3 : 5 : primes'
          where
           isPrime (p:ps) n = p*p > n || n `rem` p /= 0 && isPrime ps n
           primes' = 7 : filter (isPrime primes') (scanl (+) 11 $ cycle [2,4,2,4,6,2,6,4])

factorize :: Integer -> [Integer]
factorize = factor primes
             where factor ps@(p:pt) n | p*p > n      = [n]
                                      | rem n p == 0 = p : factor ps (quot n p)
                                      | otherwise    =     factor pt n

eulerphi :: Integer -> Integer
eulerphi n = let factors = removeMult $ factorize n in foldr (\x y -> y - y `div` x) n factors

removeMult :: (Integral a) => [a] -> [a]
removeMult [] = []
removeMult (x:xs) = x : (removeMult $ dropWhile (==x) xs)

a69Helper :: (Ord a, Fractional a) => Integer -> (Integer, a)
a69Helper x = max $ map (\x -> (x,(fromIntegral x)/(fromIntegral $ eulerphi x))) [2..x]
          where max (x:[]) = x
                max ((x1, x2):(y1, y2):xs) = max $ if x2 > y2 then (x1,x2):xs else (y1,y2):xs

a69 = let (x, _) = a69Helper 1000000 in x
