/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode p = head;      /*SLow*/
        ListNode q = head;      /*Fast*/
        ListNode r = null;

        while (q != null && q.next != null){
            q = q.next.next;
            ListNode temp = p.next;
            p.next = r;
            r = p;
            p = temp;
        }

        int res= 0;
        while(p != null)
        {
            res = Math.max(res,r.val+p.val);
            r = r.next;
            p = p.next;
        }
        return res;
    }
}