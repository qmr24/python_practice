marks=[75,82,64,91,58]
print(marks)
print(marks[0])
print(marks[2])
print(marks[-1])


marks.append(88)
marks.insert(1,95)
marks.remove(64)
marks.pop()


for mark in marks :
    print(mark)

total=0
for mark in marks:
    total = total+mark
print(total)

average = total /len(marks)
print(average)

maximum_mark=max(marks)
minimum_mark=min(marks)

print("maximum mark is ",maximum_mark)
print("minimum mark is ",minimum_mark)

