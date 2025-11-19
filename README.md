# Instructions to run the project 

Frontend
1. move inside frontend directory
2. run the following commands:
   
     ```sh
     npm install
     ```
     Followed by
     ```sh
      npm run dev
     ```

Backend
1. move into core_app
2. create a virtual environment

     ```sh
     python -m venv env
     ```
4. source the virtual environment
   
     ```sh
     source env/bin/activate
     ```
     the command above depends on the shell and os you are using,
   
   for window:
   
     ```sh
      ./env/bin/activate.bat
     ```

6. install the packages
   
     ```sh
     pip install -r app/requirements.txt
     ```
8. run the project
     ```sh
     fastapi dev app/main.py
     ```

To view all the apis for the project, visit the link "http://localhost:8000/docs" (assuming fastapi is on port 8000)
