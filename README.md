# MRoster
Marshall Roster Generator for The Warsong LARP Brisbane

- Script requires a csv file named 'authorised-marshals.csv' where the first column indicates if the person is a full marshal or not, second column depicts if they are a Head Marshal or not, third column depicts if they are a Grey Leader or not and fourth column has their fullname. 
- As long as the Marshal/Head Marshal/Grey Leader columns have a number greater than 0 in it, then the person is deemed a full Marshal/Head Marshal/Grey Leader.
- Script runs and creates the new 8 weeks worth of Roster from the current date for every Thursday with the respective event type of "Chronicles" of "Arena". 
- An Event is deemed an "Arena" event every 3 weeks.

Depends on numpy to run and depends on pyinstaller to generate the .exe

Install pyinstaller

    pip install pyinstaller
    
    
Compile and export to .exe

    pyinstaller --onefile generate-roster.py
