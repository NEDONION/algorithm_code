# 实现链表
class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

# 反转链表函数
def reverseList(li):
    # 申请两个节点,pre和cur
    pre = None
    cur = head
    while cur:
        # 申请新节点tmp，指向cur
        tmp = cur.next
        cur.next = pre
        # pre和cur往后移位
        pre = cur
        cur = tmp
    return pre

# 打印链表函数
def print_linklist(lk):
    while lk:
        print(lk.item , end=' ')
        lk = lk.next

# 手动创建链表，3-2-1
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next = b
b.next = c

# 手动设置头结点
head = a

# 设置输出链表结果
output_li = reverseList(a)

# 打印反转链表
print_linklist(output_li)
