class Task:
    def __init__(self, task_id, title, done):
        self.task_id = task_id
        self.title = title
        self.done = done
    def __str__(self):
        if self.done:
            status = "Done"
        else:
            status = "pending"
        return f"Task {self.task_id}: {self.title} - {status}"

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "done": self.done
        }