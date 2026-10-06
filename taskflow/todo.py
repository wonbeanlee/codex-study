from dataclasses import dataclass


@dataclass
class Todo:
    """제목과 완료 여부로 할 일을 표현한다."""

    title: str
    completed: bool = False

    def complete(self) -> None:
        """할 일을 완료 상태로 변경한다."""
        self.completed = True
