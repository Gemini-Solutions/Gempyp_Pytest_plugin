#### Steps to execute pytest testcases with Gempyp plugin are as follows:
Step 1: Install gempyp in your system(v 1.0.70b7).<br>
Step 2: Create a pytest testcase file.<br>
Step 3: Create a pytest.ini file and it should contain suite details like project-name, report-name, jewel credentials, etc.<br>
Step 4: The command to execute testcase file is 'pytest filename/location of file --gempyp-enable'.<br>
**Jewel Report**: https://jewel-beta.gemecosystem.com/#/autolytics/execution-report?s_run_id=TEST_PY_beta_d2b213dd-3db3-4b66-b856-efb8363e2b44&p_id=18

#### Advantages of Gempyp plugin:
1. Simplify pytest report generation using Gempyp plugin by eliminating extra library imports and separate commands.<br>
2. Unlike pytest, Gempyp surpasses by providing comprehensive report generation and storage in the database, showcasing test steps for both failed and passed test cases, enhancing overall test reporting capabilities.<br>
3. Gempyp report contain detailed information of the execution run.<br>
4. Gempyp will soon extend its capabilities to support custom test step insertion for the test cases, providing even greater flexibility and control in reporting and original pytest command will also be supported by the gempyp.

