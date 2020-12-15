# User report
A Script to help generate report on Jira Cloud users.

## Configurations
Have python3 installed on your machine. There's only one external library required. Install by
```bash
pip install -r requirements.txt
```

### Example Usage
The script is already configured, if you want to alter the behaviour, add the parameter required on
the populate function as shown below.

```python
if __name__ == '__main__':
    populate(pull="both", user_type="customer")
    report()
    """
>> The below method here displays active or inactive users, so you'll be getting all users
    :param: pull (options)
            -> both: pulls out inactive and active users
            -> active: pulls out only active users
            -> inactive: pulls out
    :param: user_type (options)
            -> atlassian: a normal Jira Cloud user
            -> customer: this will be your JSM customers
            -> app: this will be the bot users for any Cloud App
            -> unknown: as the name suggest unknown user type probably from oAuth
            """
 ```
 
 

