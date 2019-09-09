#!/bin/python3

'''
    Input Format:

    The first line of input contains , the number of elements in the linked list.
    The next  lines contain one element each, which are the elements of the linked list.
'''
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    def insert_node(self, data):     
        new_node = SinglyLinkedListNode(data)
        if self.head == None:
            self.head = new_node
        else:
            if self.get_last_node() != None:
                self.get_last_node().next = new_node
    
    def get_last_node(self):
        if self.head == None:
            return None
        node_pointer = self.head
        while(node_pointer.next != None):
            node_pointer = node_pointer.next
        return node_pointer

    def print_linked_list(self, head):
        node_pointer = head
        while(node_pointer != None):
            print(node_pointer.data)
            node_pointer = node_pointer.next


class SinglyLinkedListNode():

    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    llist.print_linked_list(head)

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)