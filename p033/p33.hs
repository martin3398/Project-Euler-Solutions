import Data.List
import Data.Ratio

a33 :: Int
a33 = denominator $ foldr (\(x,y) e -> (x % y)*e) 1 cancelFrac

cancelFrac :: [(Int, Int)]
cancelFrac = [(x, y) | x <- [1..100], y <- [1..100], x `mod` 10 /= 0 || y `mod` 10 /= 0, (x % y) < 1, isCancalFrac (x, y)]

isCancalFrac :: (Int, Int) -> Bool
isCancalFrac (x, y) = if inters == [] then False else if cutY == 0 then False else (x % y) == (cutX % cutY)
                      where numsX = show x
                            numsY = show y
                            inters = numsX `intersect` numsY
                            cutXL = numsX \\ numsY
                            cutYL = numsY \\ numsX
                            cutX = if cutXL == [] then 0 else read cutXL :: Int
                            cutY = if cutYL == [] then 0 else read cutYL :: Int
