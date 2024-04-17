defmodule Prime do
  def is_prime?(number) do
    return false if number <= 1
    for i <- 2..round(:math.sqrt(number)) do
      if rem(number, i) == 0 do
        return false
      end
    end
    true
  end

  def primes_up_to(limit) do
    Enum.filter(2...limit, &is_prime?/1)
  end
end

IO.puts("Enter the limit:")
n = String.to_integer(IO.gets(""))

primes = Prime.primes_up_to(n)
IO.puts("Prime numbers up to #{n}: #{Enum.join(primes, ' ')}")

