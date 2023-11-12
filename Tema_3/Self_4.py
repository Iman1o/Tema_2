st = input("enter sentences: ")
if "The" in st:
    print("contains 'The'")
if "end" in st:
    print("contains 'end'")
a = st.replace("ugly", "beauty")
count = 0
for char in st:
    if char in "aeiouAEIOU":
        count += 1
        a = st.replace("ugly", "beauty")
print("Vowel count:", count)
print("line length:",len(st))
print(st.lower())
print(a)






