# #------------------------------------------------------------------------------
# # Name: Nathaniel Mickel
# # G# = 01137318
# # Homework 3
# # Due Date: 29/9/2019
# # -----------------------------------------------------------------------------
# # Honor Code Statement: I received no assistance on this assignment that
# # violates the ethical guidelines set forth by professor and class syllabus.
# # -----------------------------------------------------------------------------
# # Refernces: Homework 3 Guidelines
# # -----------------------------------------------------------------------------
# # Comments: N/A
# # -----------------------------------------------------------------------------
# # NOTE: width of the source code should be <= 80 characters readable on-screen.
# # 23456789012345678901234567890123456789012345678901234567890123456789012345678
# # 		10		  20		30		  40		50		  60		70		 80
# # -----------------------------------------------------------------------------
def zigzag(string):
	newStr = ""
	if len(string) % 2 == 0:
		for i in range(len(string)//2):
			newStr += string[i] + string[len(string) - i - 1]
	else:
		for i in range(len(string)//2):
			newStr += string[i] + string[len(string) - i - 1]
		newStr += string[len(string)//2]
	return newStr
def sum_gt_avg(num_list):
	if len(num_list) == 0:
		return 0
	avg = 0
	for i in num_list:
		avg += i;
	avg = avg / len(num_list)
	sum = 0
	for i in num_list:
		if i > avg:
			sum += i
	return sum
def count_pairs(num_list):
    pairs = 0
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] + num_list[j] in num_list:
                pairs += 1
    return pairs
