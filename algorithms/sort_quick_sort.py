def quick_sort(input_list=[]):
    if len(input_list) < 2:
        return input_list
    
    base_val = input_list[0]
    left = list(filter(lambda x: x<base_val, input_list))
    center = [x for x in input_list if x==base_val]
    right = list(filter(lambda x: x>base_val, input_list))
    return quick_sort(left) + center + quick_sort(right)


input_list = [0, 2, 9, 5, 8, 3, 1]
sorted_list = quick_sort(input_list=input_list.copy())
print(f"        {input_list=}")
print(f"       {sorted_list=}")
print(f"{sorted(input_list)=}")
print(f"{(sorted_list==sorted(input_list))=}")
