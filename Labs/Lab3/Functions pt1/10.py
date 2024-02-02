def list_to_set(lst):
    st = []
    for i in lst:
        if i in st:
            continue
        else:
            st.append(i)
    return st

print(list_to_set([1,2,4,0,0,7,5])) 
print(list_to_set([1,0,2,4,0,5,7]))
print(list_to_set([1,7,2,0,4,5,0])) 
