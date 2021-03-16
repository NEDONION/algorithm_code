# python 实现链表
class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

# 头插法
def create_linklist(li):
    # 设置头结点
    head= ListNode(li[0])
    # 除开头结点，遍历
    for element in li[1:]:
        # 生成新节点
        node = ListNode(element)
        # 节点的指针指向头结点
        node.next = head
        # 把此节点变为头结点
        head = node
    return head

# 尾插法
def create_linklist_tail(li):
    # 设置头结点、尾结点
    head = ListNode(li[0])
    tail = head
    for element in li[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node

def print_linklist(lk):
    while lk:
        print(lk.item , end=' ')
        lk = lk.next

li = [1,2,3,4,5]
lk = create_linklist(li)
lk1 = create_linklist_tail(li)

print_linklist(lk)
#print_linklist(lk1)