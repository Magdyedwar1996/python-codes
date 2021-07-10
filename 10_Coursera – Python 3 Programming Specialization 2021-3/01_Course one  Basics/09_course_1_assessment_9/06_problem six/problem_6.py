winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
print(winners)
z_winners = winners.reverse()
"""for i in range(len(winners)):
    for j in range(i+1 , len(winners)):
        if ascii(winners[i][0]) > ascii(winners[j][0]):
            temp = winners[i]
            winners[i] = winners[j]
            winners[j]= temp"""

print(winners)