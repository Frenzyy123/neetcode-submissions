class WebSite():
    def __init__(self,url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = WebSite(homepage)
        self.currPage = self.head

    def visit(self, url: str) -> None:
        newPage = WebSite(url)
        self.currPage.next = newPage
        newPage.prev = self.currPage
        self.currPage = self.currPage.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.currPage.prev is None:
                break
            self.currPage = self.currPage.prev
        return self.currPage.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.currPage.next is None:
                break
            self.currPage = self.currPage.next
        return self.currPage.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)