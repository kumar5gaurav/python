nums = []
print("Enter the value of n:")
n=input()
print("Enter n Numbers in ascending order:")
for i in range(n):
    nums.insert(i, int(input()))
print("Enter a Number to Search:")
search = int(input())
first = 0
last = n
middle = (first+last)/2
middle = int(middle)
while first <= last:
    if nums[middle]<search:
        first = middle+1
    elif nums[middle]==search:
        print("Entered Number Found in the array at Position:")
        print(middle+1)
        break
    else:
        last = middle-1
    middle = (first+last)/2
    middle = int(middle)
if first>last:
    print("Entered Number is not Found in the array")