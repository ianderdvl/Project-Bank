#!/usr/bin/env python3

from urllib.parse import urljoin

import requests
import random

class API(object):

    def __init__(self, base_url):
        """ Creates the API client.
        Parameters:
            base_url (str): The base URL for the API.
        Returns:
            None
        """
        self.base_url = base_url
        payload={}
        headers = {}

    def create_task(self, cookie, Text, Date):
        """ Create a new task
        Parameters:
            cookie (str): Pre-authorized cookie
            Text (str): Text/description of the task.
            Date (str): Due date of the task
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks")
        data = '{ "Text": "%s", "Date": "%s" }' % (Text, Date)
        # For future reference
        headers = {
            'Content-Type': 'application/json',
            'Cookie': 'it210_session=' + cookie
        }
        response = requests.request("POST", url, headers=headers, data=data)
        return response

    def read_all_tasks(self, cookie):
        """ Read all the tasks in a task list
        Parameters:
            cookie (str): Pre-authorized cookie
        Returns:
            The full list of tasks
        """
        url = urljoin(self.base_url, "api/v1/tasks")

        payload={}
        headers = {
            'Cookie': 'it210_session=' + cookie
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response

    def read_task(self, cookie, task_id):
        """ Read a task as specified by its unique id
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (int): Task objects' unique id number
        Returns:
            An individual task
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)

        payload={}
        headers = {
            'Cookie': 'it210_session=' + cookie
        }   

        response = requests.request("GET", url, headers=headers, data=payload)

        return response        

    def update_task(self, cookie, task_id, Done):
        """ Toggles true or false the "done" atribute of a task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (int): Task objects' unique id number
            Done (bool): State of the task -- done or not
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)
        payload={}
        files=[

        ]
        headers = {
        'Cookie': 'it210_session=' + cookie,
        'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload, files=files)

        return response

    def delete_task(self, cookie, task_id):
        """ Delete's a task
        Parameters:
            cookie (str): Pre-authorized cookie
            task_id (int): Task objects' unique id number
        Returns:
            Response from the server
        """
        url = urljoin(self.base_url, "api/v1/tasks/" + task_id)
        payload={}
        headers = {
        'Cookie': 'it210_session=' + cookie
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        return response
    def read_current_user(self, cookie):
        """ Identifies which user's data to pull from database
        Parameters:
            cookie (str): Pre-authorized cookie
        Returns:
            Server's response
        """
        url = urljoin(self.base_url, "api/v1/user")
        payload={}
        headers = {
        'Cookie': 'it210_session=' + cookie
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response
if __name__ == "__main__":
    # Remember, this section of code is for you. Do with
    # it what you will, to see what the code looks like
    # for different requests. You may add more api calls
    # or remove them. I have found that if I add too
    # many `print()`s, the output becomes overloaded and
    # unhelpful, but again, this is personal preference.
    base_url = "https://botnetcentral.hopto.org:1337/api/v1/tasks"
    cookie = "s%3AzFTHQBea96vfkTAfZ2Ee_5P7NDaOLWA5.Es3%2BJkG1WVs2lPgX5HK1IUHv2Y9lrW%2B9o2oObBgUCEE"
    api = API(base_url)
    task_id = random.randint(1, 10)

    createResponse = api.create_task(cookie, "Test the API", "2020-02-20")

    print(createResponse.ok)
    print(createResponse.status_code)
    print(createResponse.text)
    print(createResponse.json())