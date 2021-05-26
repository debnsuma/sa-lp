# Initial setup 
0. Setup a virtual environment 
    $ python --version

    $ pip install virtualenv

    $ virtualenv ~/.virtualenvs/liveproject

    $ source ~/.virtualenvs/liveproject/bin/activate

1. Setup and configure AWS CLI

    - Install and configure AWS cli 
    
    $ sudo python -m pip install awscli

    $ aws configure --profile liveproject 
    < Provide the Access Key ID and Secret Access Key >

    # To check the configuration, run any AWS listing command, like here we are running `s3 ls` command
    $ aws s3 ls --profile liveproject

2. Install and setup AWS Chalice

    $ pip install chalice

    $ chalice --version 

    # Saving the packages in requirements.text file 
    $ pip freeze > requirements.txt 

3. Create first project with Chalice

    $ chalice new-project serverlessbackend
    
    $ cd serverlessbackend

    <We are not deploying the project, as its not mentioned in the steps>

4. Create an S3 Bucket

    $ aws s3 mb s3://liveproject2021

    $ aws s3 ls | grep liveproject2021

    # Modify the .chalice/config.json to give custom policy permissions to the lambda functions to write to S3

5. Build logic for generating the presigned-url as a URL get request

    # Edit the app.py file (also hash the mail of the user requesting the presigned url)

6. Add security and authentication

    # At this point I am stuck 



    


