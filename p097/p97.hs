start :: (Integral a) => a
start = 28433

multN2 :: (Integral a) => Int -> a -> a
multN2 0 x = x
multN2 n x = multN2 (n-1) ((x*2) `mod` 10000000000)

a97 = let x = multN2 783045 1 in let y = (x*x) `mod` 10000000000 in (((y*y*y*y*y) `mod` 10000000000)*2^7*start) `mod` 10000000000 + 1