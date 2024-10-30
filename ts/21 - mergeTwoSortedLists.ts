/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  if (!list1) return list2;
  if (!list2) return list1;

  const node = new ListNode(-1, null);

  let noderef = node;
  let list1Ref = list1;
  let list2Ref = list2;

  while (list1Ref && list2Ref){
    const l1Rval = list1Ref.val;
    const l2Rval = list2Ref.val;

    if (l1Rval <= l2Rval){
      noderef.next = list1Ref;
      list1Ref = list1Ref.next;
    }
    else if (l2Rval < l1Rval) {
      noderef.next = list2Ref;
      list2Ref = list2Ref.next;
    }
    noderef = noderef.next;
  }

  if (!list1Ref) noderef.next = list2Ref;
  if (!list2Ref) noderef.next = list1Ref;

  return node.next;
};