Steps to run the script

Step 1:
Navigate to the  project folder from command prompt.

Step 2:
Run command `pip install -r requirements.txt`

Step 3: 
Run command `py.test -s --driver Firefox --base-url https://www.gmail.com/ --html <path to generate report file>/repots.html`


Two test cases will be found by pytest package and executed.
User can see the report in the reports.html file (Path provided by user).
Report will consist of screenshot and URL of the page where the script has failed.
