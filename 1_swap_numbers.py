### by temporary variables using
# a=10
# b=20
# a=input('enter a number : ')
# b=input('enter b number : ')
#
# print('value of a before swapping : ',a)
# print('value of b before swapping : ',b)
#
# temp=a
# a=b
# b=temp
# print('value of a after swapping : ',a)
# print('value of b after swapping : ',b)

###-----approch 2 ---
a=10
b=20
a,b=b,a
print(a)
print(b)
