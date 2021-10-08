from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0, 15)

    @task(1)
    def pull_requests(self):
        self.client.get(url="/pulls")

    @task(2)
    def explore(self):
        self.client.get(url="/explore")
