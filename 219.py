#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sensenliu
"""
class ListNode:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next 

def insert_node(head, val):
	new_node = ListNode(val)
	# case 1 
	if head is None:
		return new_node 
	# case 2
	if val <= head.val:
		new_node.next = head 
		return new_node 
	# case 3
	node = head
	while node and node.next:

		if node.val <= val and node.next >= val:
			new_node.next = node.next
			node.next = new_node
			return head 
		# dont forget 
		node = node.next 

	# last case
	node.next = new_node
	return head 