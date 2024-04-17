def isitprime(number)
  return false if number<=1
  (2..Math.sqrt(number)).each do |i|
    return false if number%i==0
  end
  true
end
def prime(limit)
  primes=[]
  (2...limit).each do |num|
    primes << num if isitprime(num)
  end
    primes
end

puts "Enter the limit :"
n=gets.chomp.to_i

puts "Prime numbers up to #(n) :#{prime(n).join(' ')}"
