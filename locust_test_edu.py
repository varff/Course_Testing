from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0, 15)

    def on_start(self):
        self.client.post("/login", {"username": "fpm.varfolom", "password": "1923080"})

    @task(1)
    def cabinet(self):
        self.client.get(url="/my")

    @task(2)
    def fizra(self):
        self.client.get(url="/course/view.php?id=454")
