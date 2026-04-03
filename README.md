Running this website application from Visual Studio Code is straightforward. Here are the two most common and effective ways to do it:

Method 1: Using the "Live Server" Extension
This is a popular method for web development in VS Code if you are just working on static files, because it automatically refreshes your browser whenever you save changes to your HTML, CSS, or JS files.
1.	Open your project folder: Open Visual Studio Code, go to File > Open Folder, and select your CSC6220_PROJECT2 folder.
2.	Install the Extension:
o	Click on the Extensions icon in the left sidebar (or press Ctrl+Shift+X on Windows / Cmd+Shift+X on Mac).
o	Search for Live Server (by Ritwick Dey) and click Install.
3.	Run the Application:
o	Open your index.html file in the VS Code editor.
o	Right-click anywhere inside the code and select Open with Live Server from the context menu.
o	Alternatively, you can click the Go Live button that appears in the bottom right corner of the VS Code status bar.
4.	View the Site: Your default web browser will automatically open and display your website (usually at http://127.0.0.1:5500/index.html).

Method 2: Using Python to run your Flask App (app.py)
Since your project has a Python backend (app.py) and a virtual environment set up (venv), you can run the application directly from the VS Code terminal.
1.	Open your project folder: Open Visual Studio Code, go to File > Open Folder, and select your CSC6220_PROJECT2 folder.
2.	Open the Terminal: Go to Terminal > New Terminal (or press Ctrl+ [backtick]).
3.	Activate the Virtual Environment: In the terminal, run the activation script for Windows:
	.\venv\Scripts\activate
4.	Start the Server: With the environment active, run your Flask application using the following command:
	python app.py
5.	View the Site: Open your web browser and navigate to http://127.0.0.1:5000. You will see your website rendered there!
o	Note: Because you have debug=True set in your app.py, the Flask server will automatically reload if you make changes to your Python code. However, you will still need to manually refresh your browser window to see any changes.
