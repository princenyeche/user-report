import requests
import json
import csv
from collections import deque
from requests.auth import HTTPBasicAuth
from typing import AnyStr, Any

user = "email_address"
token = "token"
url = "https://yourinstance.atlassian.net"
headers = {"Content-type": "application/json"}
auth = HTTPBasicAuth(user, token)
user_list = deque()


def populate(pull: str = AnyStr, user_type: str = "atlassian") -> Any:
    """
    Below Script helps to Generate the No of Users on Jira Cloud
    You can customize it to determine which user you're looking for.
    >> The below method here displays active or inactive users, so you'll be getting all users
    :param: pull (options)
            -> Both: pulls out inactive and active users
            -> active: pulls out only active users
            -> inactive: pulls out
    :param: user_type (options)
            -> atlassian: a normal Jira Cloud user
            -> customer: this will be your JSM customers
            -> app: this will be the bot users for any Cloud App
            -> unknown: as the name suggest unknown user type probably from oAuth
    """
    count_start_at = 0
    api = "/rest/api/3/myself".format(count_start_at)
    endpoint = "{}{}".format(url, api)
    validate = requests.get(endpoint, auth=auth, headers=headers)

    while validate.status_code == 200:
        api2 = "/rest/api/3/users/search?startAt={}&maxResults=50".format(count_start_at)
        endpoint2 = "{}{}".format(url, api2)
        extract = requests.get(endpoint2, auth=auth, headers=headers)
        results = json.loads(extract.content)
        user_activity(pull, user_type, results)
        count_start_at += 50
        print("Current Record - At Row", count_start_at)

        if str(results) == "[]":
            break


def report():
    # creates a report file in CSV format
    with open("users_report.csv", "a+") as f:
        loader = csv.writer(f, delimiter=",")
        read = [d for d in user_list]
        loader.writerows(read)


def user_activity(f: str = Any, s: str = Any, results=Any) -> Any:
    # get both active and inactive users
    if f == "both":
        for each_user in results:
            account_type = s
            if each_user["accountType"] == account_type:
                list_user = [each_user["accountId"], each_user["accountType"], each_user["displayName"],
                             each_user["active"]]
                user_list.append(list_user)
    # get only active users
    elif f == "active":
        for each_user in results:
            account_type = s
            if each_user["accountType"] == account_type and each_user["active"] is True:
                list_user = [each_user["accountId"], each_user["accountType"], each_user["displayName"],
                             each_user["active"]]
                user_list.append(list_user)
    # get only inactive users
    elif f == "inactive":
        for each_user in results:
            account_type = s
            if each_user["accountType"] == account_type and each_user["active"] is False:
                list_user = [each_user["accountId"], each_user["accountType"], each_user["displayName"],
                             each_user["active"]]
                user_list.append(list_user)


if __name__ == '__main__':
    populate(pull="both")
    report()
