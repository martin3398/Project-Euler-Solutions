import Data.List

pows :: Integer -> [Integer]
pows n = [a^b| a <- [2..n], b <- [2..n]]

powssorted n = sort $ pows n

remDouble :: Integer -> [Integer] -> [Integer]
remDouble _ [] = []
remDouble (-1) (x:xs) = x:(remDouble x xs)
remDouble last (x:xs) = if x == last then remDouble x xs else x:(remDouble x xs)

a29 :: Int
a29 = length $ remDouble 0 $ powssorted 100