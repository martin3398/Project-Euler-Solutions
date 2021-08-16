import Data.List

factorize :: Integer -> [Integer]
factorize = factor primes
             where factor ps@(p:pt) n | p*p > n      = [n]
                                      | rem n p == 0 = p : factor ps (quot n p)
                                      | otherwise    =     factor pt n

primes :: [Integer]
primes = 2 : 3 : 5 : primes'
          where
           isPrime (p:ps) n = p*p > n || n `rem` p /= 0 && isPrime ps n
           primes' = 7 : filter (isPrime primes') (scanl (+) 11 $ cycle [2,4,2,4,6,2,6,4])

eulerphi :: Integer -> Integer
eulerphi n = let factors = removeMult $ factorize n in foldr (\x y -> y - y `div` x) n factors

removeMult :: (Integral a) => [a] -> [a]
removeMult [] = []
removeMult (x:xs) = x : (removeMult $ dropWhile (==x) xs)

isPerm :: (Ord a) => [a] -> [a] -> Bool
isPerm x y = sort x == sort y

a70Helper n = fst $ min $ map (\x -> (x, let phix = eulerphi x in if isPerm (show x) (show $ phix) then (fromIntegral x)/(fromIntegral phix) else 2)) [2..n]
          where min (x:[]) = x
                min ((x1, x2):(y1, y2):xs) = min $ if x2 < y2 then (x1,x2):xs else (y1,y2):xs

a70 = a70Helper 10000000
