def bubble_sort(input_list=[]):
    if len(input_list) < 2:
        return input_list
    
    list_len = len(input_list)
    for step in range(list_len - 1):
        empty_step = True
        for i in range(list_len - 1 - step):
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                empty_step = False
        if empty_step:
            break
    return input_list


input_list = [0, 2, 9, 5, 8, 3, 1]
sorted_list = bubble_sort(input_list=input_list.copy())
print(f"        {input_list=}")
print(f"       {sorted_list=}")
print(f"{sorted(input_list)=}")
print(f"{(sorted_list==sorted(input_list))=}")
