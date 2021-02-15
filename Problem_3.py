count = 0
for i in range(1000, 0, -1):
    print(i, end='\t')
    count += 1
    if count % 5 == 0:
        print()
        count = 0

# Another Way Solve This Problem

# number = 1000
# tracker = []
#
# for i in range(number, 0, -1):
#     tracker.append(i)
#     if len(tracker) == 5:
#         for j in tracker:
#             print(j, end='\t')
#         print()
#         tracker = []


# for n in range(999, -1, -1):
# 	print(n+1, end="\t")
# 	if n%5 == 0:
# 		print('')
