subject1=int(input('Enter score between (0-100)'))
subject2=int(input('Enter score between (0-100)'))
subject3=int(input('Enter score between (0-100)'))

average=(subject1+subject2+subject3)/3
print(average)

if average>80:
    print('Grade A')
if average>70:
    print('Grade B')
if average <69:
    print('Grade F')