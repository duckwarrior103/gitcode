head = ListNode()
answer = head
carry = 0
while l1 or l2: 	
	head.next = ListNode()
	head = head.next
	head.val = carry
	carry = 0
	if l1 and l2:
		head.val += l1.val + l2.val
		l1 = l1.next 
		l2 = l2.next 
	elif l1:
		head.val += l1.val 
		l1 = l1.next 
	elif l2: 
		head.val += l2.val
		l2 = l2.next 
	if head.val > 9:
		head.val -= 10 
		carry = 1

if carry > 0
    head.next = ListNode(1)


return answer.next

### time 1: 24m 50s - 28/7/24
