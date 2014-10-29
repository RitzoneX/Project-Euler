
numbers = ['one', 'two', 'three', 'four', 'five',
           'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty',
           'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = len('hundred') * 900
ands = len('and') * 891

sum1to9 = sum([len(n) for n in numbers[:9]])
sum1to99 = sum([len(n) for n in numbers]) + sum1to9 * 8
sum1to999 = sum1to99 * 10 + hundreds + ands + sum1to9 * 100
print sum1to999 + len('one thousand')