s = "abcbcd"
test = s[0]      # seed with first letter in string s
best = ''        # empty var for keeping track of longest sequence

for n in range(1, len(s)):    # have s[0] so compare to s[1]
    if len(test) > len(best):
        best = test
    if s[n] >= s[n - 1]:
        test = test + s[n]    # add s[1] to s[0] if greater or equal
    else:                     # if not, do one of these options
        test = s[n]

print('Longest substring in alphabetical order is:', best)
