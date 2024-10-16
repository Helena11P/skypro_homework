from ProjectsAPI import Project
import pytest

xfail = pytest.mark.xfail

api = Project("https://yougile.com/")


# Создание проекта. Позитивная проверка
def test_create_new_project_positive():
    # получить список проектов
    projects_list = api.get_project_list()
    len_befor = len(projects_list)
    # добавить проект
    user_id = api.get_users_list()
    new_project = api.add_project("Тестовый проект", user_id, "admin")
    # снова получить список проектов
    projects_list = api.get_project_list()
    len_after = len(projects_list)
    # проверить, что проект добавлен
    assert len_after == len_befor + 1
    # проверить, что id последней компании такой же как у только что созданной
    assert projects_list[-1]["id"] == new_project["id"]


# Создание проекта. Негативные проверки
@xfail(strict=True)
def test_create_new_project_without_title_negative():
    projects_list = api.get_project_list()
    len_befor = len(projects_list)
    user_id = api.get_users_list()
    new_project = api.add_project("", user_id, "admin")
    projects_list = api.get_project_list()
    len_after = len(projects_list)
    assert len_after == len_befor + 1
    assert projects_list[-1]["id"] == new_project["id"]


@xfail(strict=True)
def test_create_new_project_without_user_id_negative():
    projects_list = api.get_project_list()
    len_befor = len(projects_list)
    new_project = api.add_project("Проект без айди пользователя", "", "admin")
    projects_list = api.get_project_list()
    len_after = len(projects_list)
    assert len_after == len_befor + 1
    assert projects_list[-1]["id"] == new_project["id"]


@xfail(strict=True)
def test_create_new_project_without_user_role_negative():
    projects_list = api.get_project_list()
    len_befor = len(projects_list)
    user_id = api.get_users_list()
    new_project = api.add_project("Проект без айди пользователя", user_id, "")
    projects_list = api.get_project_list()
    len_after = len(projects_list)
    assert len_after == len_befor + 1
    assert projects_list[-1]["id"] == new_project["id"]


# Позитивные проверки
def test_edit_title_positive():
    # создать проект
    user_id = api.get_users_list()
    new_project = api.add_project("Еще один проект", user_id, "admin")
    new_project_id = new_project["id"]
    # изменить название
    new_title = "Измененное название"
    change_title = api.edit_title(new_project_id, new_title)
    # получить список
    project_list = api.get_project_list()
    # проверить, что id измененного проекта равно id созданного проекта
    assert change_title == new_project_id
    assert project_list[-1]["title"] == new_title


def test_edit_user_role_positive():
    user_id = api.get_users_list()
    new_project = api.add_project("Роль юзера", user_id, "admin")
    new_project_id = new_project["id"]
    change_role = api.edit_user_role(new_project_id, user_id, "observer")
    project_list = api.get_project_list()
    assert change_role == new_project_id
    assert project_list[-1]["users"][f"{user_id}"] == 'observer'


def test_edit_title_and_user_role_positive():
    # создать проект
    user_id = api.get_users_list()
    new_project = api.add_project("Название и роль юзера", user_id, "admin")
    new_project_id = new_project["id"]
    # изменить название и роль юзера
    new_title = "Измененное название"
    change_title = api.edit_title(new_project_id, new_title)
    change_role = api.edit_user_role(new_project_id, user_id, "observer")
    # получить список
    project_list = api.get_project_list()
    # проверки
    assert change_title == new_project_id
    assert project_list[-1]["title"] == new_title
    assert change_role == new_project_id
    assert project_list[-1]["users"][f"{user_id}"] == 'observer'


def test_delete_positive():
    # создать проект
    user_id = api.get_users_list()
    new_project = api.add_project("Еще один проект", user_id, "admin")
    new_project_id = new_project["id"]
    # удалить проект
    delete = api.delete_project(new_project_id, True)
    # получить список
    project_list = api.get_project_list()
    # проверка
    assert delete == new_project_id
    assert project_list[-1]["id"] != delete


def test_edit_title_and_delete_positive():
    user_id = api.get_users_list()
    new_project = api.add_project("Название и роль юзера", user_id, "admin")
    new_project_id = new_project["id"]
    new_title = "Измененное название"
    change_title = api.edit_title(new_project_id, new_title)
    delete = api.delete_project(new_project_id, True)
    project_list = api.get_project_list()
    assert change_title == delete
    assert project_list[-1]["id"] != change_title


# негативные тесты
@xfail(strict=True)
def test_edit_whithout_title_negative():
    user_id = api.get_users_list()
    new_project = api.add_project("Еще один проект", user_id, "admin")
    new_project_id = new_project["id"]
    new_title = "Измененное название"
    change_title = api.edit_title("", new_project_id)
    project_list = api.get_project_list()
    assert change_title == new_project_id
    assert project_list[-1]["title"] == new_title


@xfail(strict=True)
def test_edit_without_user_id_negative():
    new_project = api.add_project("Роль юзера", "", "admin")
    new_project_id = new_project["id"]
    change_role = api.edit_user_role(new_project_id, "", "observer")
    assert change_role == new_project_id


@xfail(strict=True)
def test_whithout_user_role_negative():
    user_id = api.get_users_list()
    new_project = api.add_project("Роль юзера", user_id, "admin")
    new_project_id = new_project["id"]
    change_role = api.edit_user_role(new_project_id, user_id, "")
    assert change_role == new_project_id


@xfail(strict=True)
def test_wrong_user_role_negative():
    user_id = api.get_users_list()
    new_project = api.add_project("Роль юзера", user_id, "admin")
    new_project_id = new_project["id"]
    change_role = api.edit_user_role(new_project_id, user_id, "dude")
    assert change_role == new_project_id


# позитивная проверка
def test_get_project_by_id_positive():
    user_id = api.get_users_list()
    new_project = api.add_project("Еще один проект", user_id, "admin")
    new_project_id = new_project["id"]
    project_info = api.get_project_by_id(new_project_id)
    assert project_info["id"] == new_project_id
    assert "title" in project_info
    assert "timestamp" in project_info


@xfail(strict=True)
def test_get_project_by_id_negative():
    user_id = api.get_users_list()
    new_project = api.add_project("Еще один проект", user_id, "admin")
    new_project_id = new_project["id"]
    project_info = api.get_project_by_id("")
    assert project_info["id"] == new_project_id
    assert "title" in project_info
    assert "timestamp" in project_info
