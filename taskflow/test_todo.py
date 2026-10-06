from todo import Todo


def test_new_todo_is_incomplete():
    todo = Todo(title="장보기")

    assert todo.title == "장보기"
    assert todo.completed is False


def test_todo_can_be_created_completed():
    todo = Todo(title="장보기", completed=True)

    assert todo.completed is True


def test_complete_marks_only_target_todo_completed():
    todo = Todo(title="장보기")
    other = Todo(title="청소하기")

    todo.complete()
    todo.complete()

    assert todo.completed is True
    assert other.completed is False
