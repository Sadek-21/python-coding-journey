message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for charachter in message:
    count.setdefault(charachter, 0 )
    count[charachter] = count[charachter] + 1

print(count)
