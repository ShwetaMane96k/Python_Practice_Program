def sort_dict_by_values(d):
    ascending=dict(sorted(d.items(),key=lambda item :item[1]))
    descending=dict(sorted(d.items(),key=lambda item :item[1],reverse=True))
    return ascending , descending
marks={
    'Shweta':90,
    'Dhanu':85,
    'Sita':80,
    'Gita':76,
    'Gautami':77
}
asc,desc =sort_dict_by_values(marks)
print("Original Dictionary :",marks)
print("Ascending Order :",asc)
print("Descending Order :",desc)