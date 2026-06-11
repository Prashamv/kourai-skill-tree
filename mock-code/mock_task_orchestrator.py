"""Safe mock example of a workflow orchestrator.

This is not production Kourai code. It is a simplified public example that
shows the general idea of running an approval-first AI workflow.
"""

from dataclasses import dataclass
from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    NEEDS_REVIEW = "needs_review"


@dataclass
class MockTask:
    name: str
    status: TaskStatus = TaskStatus.PENDING


class MockOrchestrator:
    def __init__(self) -> None:
        self.tasks = [
            MockTask("generate_strategy"),
            MockTask("create_draft"),
            MockTask("review_content"),
            MockTask("log_result"),
        ]

    def run(self) -> list[MockTask]:
        for task in self.tasks:
            if task.name == "review_content":
                task.status = TaskStatus.NEEDS_REVIEW
            else:
                task.status = TaskStatus.COMPLETE
        return self.tasks


if __name__ == "__main__":
    for item in MockOrchestrator().run():
        print(f"{item.name}: {item.status.value}")
