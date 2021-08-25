import json
import pytest

@pytest.mark.parametrize('mock_task, task_filename', [
    ('sample_task.json', 'sample_task.json'),
    ('task_no_app.json', 'task_no_app.json')
    ], indirect=['mock_task'], ids=['task_with_app', 'task_no_app']
    )
def test_task_init(mock_task, test_data, task_filename):
    task_json = json.load(test_data.joinpath(task_filename).open())
    task_name = task_json.get('name')
    task_id = task_json.get('id')
    task_app_id = task_json.get('applicationId')
    task_script = task_json.get('action').get('script')
    assert mock_task.id == task_id
    assert mock_task.name == task_name
    assert mock_task.app_id == task_app_id
    assert mock_task.script == task_script
    assert str(mock_task) == task_name
    assert mock_task.__repr__() == '<Task: {task_name}>'.format(task_name=task_name)
    assert mock_task.__hash__() == hash((task_app_id, task_id, task_name, task_script))
