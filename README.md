# README #

### What is this repository for? ###

* Lambda function written in python3 which deletes AWS snapshots. This function can be invoked as long as there is a JSON payload sent.
* The purpose of seperating the delete function from the function which gathers the snapshots is if there were a need to delete 1000+ snapshots. It is best pratise to limit runtime for lambda functions.
* This function can be invoked multiple times,where a group of snapshot ID's can be sent.
* It is recommended to send no more than 100 spanshots.
* Version 1 

### How do I get set up? ###

#### Summary of set up ####
* Python script will utilize the following modules
      * boto3 - Used for querying the AWS API
      * Json, sys - Only used for manual execution via cli not AWS Lambda
      * botocore.config - Increase threshold on boto limits
#### Configuration ####
* Create lambda using Python Version 3.6
* In AWS setup a Lambda function, ensure the following permissions:
    * EC2 - Describe permissions
    * Cloudwatch - create groups and streams. Put logs
* create a test with the following json. You can replace the SnapId's with your own.
```json
{
  "SnapshotId": [
    "snap-1234",
    "snap-5678",
    "snap-9098"
  ]
}
```
* Configure lambda timeout to 1 Miunte 30 Seconds
#### Dependencies ####
* N/A
* How to run tests
  * Tests can be performed via linux CLI. Ensure the modules exampled above are installed. To run a test perform the following. `cat example_event.json| python3 main.py`
* Deployment instructions
  * Ensure tests are performed to the develop branch first, or checkout master in your own branch. Once tested, merge to master. Please ensure to create tags with each release to master.

### Who do I talk to? ###

* Repo owner or admin
* Nikola Sepentulevski
