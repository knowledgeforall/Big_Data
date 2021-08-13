

#create empty array
A = []
print("Array A: ", A)

#create a "populated" array
B = [12, 23, 56, 17, 23]
print("Array B: ", B)

#Add an element to an array
print("Before adding to A: ", A)
A.append(90)
print("After adding to A:  ", A)


#access the 2nd element in array B
print("The second element in Array B is: ", B[1])

print("\nChanging the second element in B:")
print(B)
B[1] = 72
print(B)


#computing the average over all values stored in B
print("Computing the average over all elements in B:")
total=0
for i in range( 0, len(B) ):
    total = total + B[i]
print("Sum = ", total)
print("Avg = ", total/len(B) )


#read some value from the user
x = int ( input("Enter a number to search for it in Array B: ") )


#sequential search of an array
found=False
for i in range(0, len(B) ):
    if B[i] == x:
        print(x, "found at index", i)
        found = True
        break

if not found:      
    print(x, "not found")
    
