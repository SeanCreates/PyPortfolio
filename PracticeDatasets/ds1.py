import pandas

mydataset = {
    'cars' : ['BMMW', 'RollsRoyce', 'Tesla', 'Ford'],
    'passings' : [3, 7, 5, 6,]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)


