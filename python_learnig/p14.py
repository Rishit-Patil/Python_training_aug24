#Program to find 2nd smallest digit in a number

sample_number = int(input("Enter a number: "))
string=[]
for i in str(sample_number):
    if i not in string:
        string.append(i)

assending_str = sorted(string)

print('The second smallest digit is: ',assending_str[1])
