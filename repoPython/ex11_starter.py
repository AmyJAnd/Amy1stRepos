#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# basic way
# str_length =len(Belgium)
# print(str_length)
# print(str_length* "-")

# this one better as more translatable to other languages. Not all can multiply string characters
for e in Belgium:
    print("-", end="")

# why does this print 81 hyphens and not 11? Q for Martina oh because e is one element in list?

print(Belgium.replace(",",":"))

# or

new_belgium = Belgium.replace(",",":")
print(new_belgium)

#this one better. Less fragile
trial_list = Belgium.split(",")
print(trial_list)
print(int(trial_list[1]) + int(trial_list[3]))

# belgium_pop = Belgium[8:16]
# print(belgium_pop)
# capital_pop = Belgium[26:32]
# print(capital_pop)
# print(int(belgium_pop)+ int(capital_pop))

