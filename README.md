# Continus Integration (automatic testing)

this repository contains code for automated testing. 

The folder named dummyProject contains python-functions in the folder utils and unit tests for those functions 
in the file test_utils. The unit tests in this folder are being run by the Continious Integration (automatic testing)
code. In order to test out the code run the following from the command line:  
  
python main.py
<br>
<br>  
  
In order for the CI to (re)run the automated tests, you must make any change (and save) to any of the files in the 
dummyProject folder. Currently only adding unit-tests works as intended. Removing unit tests will currently not be 
dealt with properly. 