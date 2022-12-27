#!/usr/bin/env python3

import random
import string
import unittest
from api import API

"""TODO: Import the `API` class from the api.py file"""

def generate_random_text(l=10):
    """ Helper to generate random text for creating new tasks.
    This is helpful and will ensure that when you run your tests,
    a new text string is created. It is also good for determining
    that two tasks are unique.
    Keyword arguments:
        l (int): How long the generated text should be (default 10)
    Returns:
        A randomly-generated string of length `l`
    """
    chars = string.hexdigits
    return "".join(random.choice(chars) for i in range(l)).lower()

def generate_random_date(year=None, month=None, date=None):
    """ Helper to generate random date for creating new tasks.
    This is helpful as another way of generating random tasks
    Keyword arguments:
        year: Specify a year (default None)
        month: Specify a month (default None)
        date: Specify a date (default None)
    Returns:
        A randomly-generated string representation of a date
    """
    if not year:
        year = str(random.randint(2000, 2025))
    if not month:
        month = str(random.randint(1, 12))
    if not date:
        date = str(random.randint(1, 28))
    return str(year) + "-" + str(month).zfill(2) + "-" + str(date).zfill(2) + "T00:00:00.000Z"

class TestAPI(unittest.TestCase):

    # TODO: update the cookie value and uncomment the desired `base_url, cookie` pair when ready to test
    base_url, cookie = "https://botnetcentral.hopto.org:1337", "s%3AzFTHQBea96vfkTAfZ2Ee_5P7NDaOLWA5.Es3%2BJkG1WVs2lPgX5HK1IUHv2Y9lrW%2B9o2oObBgUCEE" # For s1
    #base_url, cookie = "https://s2.byu-itc-210.net:1338", "s%3AZUSn3Ibaj8MGoAFT5sLtHrrHvsainRU3.3BVwcwP5ngPfnSBHyei2ZkcHkDmdj63HgO7IdQIbA2s" # For s2
    #base_url, cookie = "https://s3.byu-itc-210.net:1339", "s%3AZUSn3Ibaj8MGoAFT5sLtHrrHvsainRU3.3BVwcwP5ngPfnSBHyei2ZkcHkDmdj63HgO7IdQIbA2s" # For s3
    #base_url, cookie = "https://s4.byu-itc-210.net:1340", "s%3AZUSn3Ibaj8MGoAFT5sLtHrrHvsainRU3.3BVwcwP5ngPfnSBHyei2ZkcHkDmdj63HgO7IdQIbA2s" # For s4

    # This will be ran once, when you start your tests.
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.api = API(self.base_url)

    def test_create_task(self):
        """ Tests creating a task is successful.
        This is an example test:
            - Create the task w/dummy data
            - Verify that the task was created
            - Delete the task we created
        You will be required to implement the other tests
        that are defined in BaseTestCase. They will be marked
        with @abc.abstractmethod.
        """
        Text = generate_random_text()
        Date = generate_random_date()

        create_resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(create_resp.ok, msg=f"The Create Task failed: {create_resp.reason}.")
        task = create_resp.json()

        self.assertEqual(task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg=f"All tasks should have a UserId, matching the Id of the user who created it.")

        # cleanup - we don't want to conflict with other tests
        # or have a test task in our database.
        self.api.delete_task(self.cookie, task["_id"])

    def test_read_all_tasks(self):

        Text1 = generate_random_text()
        Date1 = generate_random_date()

        create_resp = self.api.create_task(self.cookie, Text1, Date1)
        self.assertTrue(create_resp.ok, msg=f"The Create Task failed: {create_resp.reason}.")
        task1 = create_resp.json()
        userId = task1["UserId"]

        Text2 = generate_random_text()
        Date2 = generate_random_date()
        self.api.create_task(self.cookie, Text2, Date2)

        read_all_resp = self.api.read_all_tasks(self.cookie)
        tasks = read_all_resp.json()

        for x in tasks:
           self.assertEqual(x.get("UserId"), userId, msg =f"The tasks have different user ID's. Should have the same user ID: {read_all_resp.reason}.")

    def test_read_one_task(self):

        Text = generate_random_text()
        Date = generate_random_date()

        create_resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(create_resp.ok, msg=f"The Create Task failed: {create_resp.reason}.")
        task = create_resp.json()

        read_resp = self.api.read_task(self.cookie, task["_id"])
        self.assertTrue(read_resp.ok, msg=f"The Read-One Task failed: {read_resp.reason}.")
        task = read_resp.json()

        self.assertEqual(task["Text"], Text, msg="The task's Text did not match the expected Text.")
        self.assertEqual(task["Date"], Date, msg="The task's Date did not match the expected Date.")
        self.assertFalse(task["Done"], msg="The task's Done returned True, expected False.")
        self.assertIn("UserId", task, msg=f"All tasks should have a UserId, matching the Id of the user who created it.")

        self.api.delete_task(self.cookie, task["_id"])

    def test_update_task(self):

        Text = generate_random_text()
        Date = generate_random_date()

        create_resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(create_resp.ok, msg=f"The Create Task failed: {create_resp.reason}.")
        task = create_resp.json()

        update_Resp = self.api.update_task(self.cookie, task["_id"], task["Done"])
        self.assertTrue(update_Resp.ok, msg=f"The Update Task failed: {update_Resp.reason}.")
        updatedTask = update_Resp.json()

        self.assertFalse(updatedTask["Done"], msg =f"Task was not marked to done.")

        self.api.delete_task(self.cookie, task["_id"])
        self.api.delete_task(self.cookie, updatedTask["_id"])

    def test_delete_task(self):
    
        Text = generate_random_text()
        Date = generate_random_date()

        create_resp = self.api.create_task(self.cookie, Text, Date)
        self.assertTrue(create_resp.ok, msg=f"The Create Task failed: {create_resp.reason}.")
        task = create_resp.json()

        delete_resp = self.api.delete_task(self.cookie, task["_id"])
        self.assertTrue(delete_resp.ok, msg=f"The Delete Task failed: {delete_resp.reason}.")

        read_resp = self.api.read_task(self.cookie, task["_id"])
        self.assertFalse(read_resp.ok, msg=f"Read-one Task didn't fail and it should have: {read_resp.reason}.")

        self.api.delete_task(self.cookie, task["_id"])

    def test_read_current_user(self):
        
        read_user_resp = self.api.read_current_user(self.cookie)

        self.assertTrue(read_user_resp.ok, msg=f"Read Current User failed: {read_user_resp.reason}.")
        task = read_user_resp.json()

        self.assertIn("Id", task, msg = "User has no ID")
        self.assertIn("UserName", task, msg = "User has no email on file")
        self.assertIn("Email", task, msg = "User has no username")        

    def test_read_one_fail(self) :
    
        id = generate_random_text(24)
        resp = self.api.read_task(self.cookie, id)
        self.assertFalse(resp.ok, msg=f"The Read-one function cannot read tasks that aren't there: {resp.reason}.")
        print(resp.status_code)

    def test_delete_fail(self) :

        id = generate_random_text(24)
        resp = self.api.delete_task(self.cookie, id)
        self.assertFalse(resp.ok, msg=f"The Delete function cannot delete tasks that aren't there: {resp.reason}.")
        print(resp.status_code)

    def test_update_fail(self) :

        id = generate_random_text(24)
        resp = self.api.update_task(self.cookie, id, False)
        self.assertFalse(resp.ok, msg=f"The Update function cannot update tasks that aren't there: {resp.reason}.")
        print(resp.status_code)

    def test_delete_fail_invalid(self) :

        id = generate_random_text(23)
        resp = self.api.delete_task(self.cookie, id)
        self.assertFalse(resp.ok, msg=f"The task's ID is totally invalid: {resp.reason}.")
        print(resp.status_code)

    def test_read_all_no_cookie(self) :

        cookie = generate_random_text(24).lower()
        resp = self.api.read_all_tasks(cookie)
        self.assertFalse(resp.ok, msg=f"There is no cookie because the user is not logged in: {resp.reason}.")
        print(resp.status_code)

    def test_create_fail_insufficient_data(self) :

        Text = generate_random_text
        Date = generate_random_date

        resp = self.api.create_task(self.cookie, Text, "")

        self.assertFalse(resp.ok, msg=f"Task should not have been created without necessary date: {resp.reason}.")

        resp = self.api.create_task(self.cookie, "", Date)

        self.assertFalse(resp.ok, msg=f"Task should not have been created without necessary text: {resp.reason}.")

        resp = self.api.create_task(self.cookie, "", "")

        self.assertFalse(resp.ok, msg=f"Task should not have been created without necessary text and date: {resp.reason}.")
        print(resp.status_code)

    # Make more methods that begin with 'test` to test all endpoints
    # properly work and fail when you expect them to.

# Inside this `if` statement will only run if we call the program as
# the top-level module, i.e. when we run this file, not when we import
# this file
if __name__ == "__main__":
    unittest.main()