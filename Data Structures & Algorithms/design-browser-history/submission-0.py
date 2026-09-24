class ListNode:
    def __init__(self,url:str,prev=None,next=None):
        self.url = url
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = ListNode(homepage)


        

    def visit(self, url: str) -> None:
        self.curr_page.next = ListNode(url,self.curr_page)
        self.curr_page = self.curr_page.next


        

        

    def back(self, steps: int) -> str:
        while self.curr_page.prev and steps > 0:
            self.curr_page = self.curr_page.prev
            steps -= 1
        return self.curr_page.url 

        

    def forward(self, steps: int) -> str:
        while self.curr_page.next and steps > 0:
            self.curr_page = self.curr_page.next 
            steps -= 1
        return self.curr_page.url 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)