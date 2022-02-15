

target = '90%'
target_int = int(target.split('%')[0])
print(target_int)
result = [{'name':'aa','similarity':77}, 
        {'name':'aa','similarity':65},
        {'name':'aa','similarity':99},
        {'name':'aa','similarity':88}]

def percent(n):
    return True if n['similarity']>target_int else False

res = filter(percent, result)

print(list(res))

