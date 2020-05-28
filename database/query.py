from mongoengine import *
from datetime import datetime
from database.models import User
from database.connection import MongoDB
import random

mongo = MongoDB()
mongo.connect_db()


def generate_uuid(size=15):
    token = "qwertyuiopasdfghjklmnbvcxza1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    now = datetime.now()
    uuid = str(datetime.timestamp(now))
    uuid = uuid.replace(".", "")
    for index in range(size):
        i = random.randint(0, len(token) - 1)
        uuid += token[i]
    return str(uuid)


def insert_user_2_db(user_id, user_name):
    """
    todo: insert new user into database
    :param user_id (string, unique): id của user
    :param user_name (string): tên của user
    :return: trạng thái insert thành công hay thất bại
    """
    user = User(user_id=str(user_id), user_name=str(user_name))
    try:
        user.save()
    except Exception as e:
        return False
    return True


def get_all_user():
    """
    todo: get all user in database
    """
    users = User.objects().all()
    results = []
    for user in users:
        results.append({
            "user_id": user.user_id,
            "id": str(user.id),
            "user_name": user.user_name,
            "language": user.language,
        })
    return results


def update_setting(user):
    """
    todo: thực hiện update thông tin user
    :argument
    user (dict) bao gồm: user_id, user_name, setting khác
    :return: status after updating
    """
    try:
        user_id = user['user_id']  # string
        user_name = user['user_name']  # string
        language = user['language']  # string

        user = User.objects(user_id=user_id)
        status = user.update(language=language, user_name=user_name)
        if status != 1:
            return {"status": "fail"}
        return {"status": "success"}
    except Exception as e:
        return {"status": "fail", "cause": str(e)}


def get_information_user(user_id):
    """
    todo: lấy thông tin của một user dựa vào user_id
    :argument
    use_id (string):  user_id của user.
    :param user_id:
    :return: trả về thông tin user cùng với status
    """
    try:
        users = User.objects(user_id=user_id)
        if len(users) == 0:
            return {"status": "fail",
                    "user": None}
        else:
            user = users[0]
            return {
                "status": "success",
                "user": {
                    "user_id": user.user_id,
                    "user_name": user.user_name,
                    "language": user.language
                }

            }
    except Exception as e:
        return {"status": "fail",
                "cause": str(e)}


if __name__ == "__main__":
    info = get_information_user(user_id="hungnm")
