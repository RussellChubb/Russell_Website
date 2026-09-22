# Virtual Environments Script

Today’s a wonderful day, as we get to talk about Virtual Environments in Python.
A virtual environment is an isolated workspace that allows you to manage dependencies for your Python projects. This allows you to work on multiple projects from the same machine, each with its own set of libraries and packages, without conflicts.

So you ask “Russell, why do I even need to use virtual environments?”, look at you, you sweet summer child.
Imagine you’re working on multiple Python projects, where one project requires a specific version of a library and another project requires a different version.

Without virtual environments, you’d run into a bunch of issues, and likely have to give up coding, spiraling into a deep depression that inevitably ends really badly for you… But, yeah, if you’re using Virtual Environments you’re all good aye.

Enough yapping, let’s spin up our first virtual environment. Open your terminal, and navigate to your project directory. You’re going to run this command “python -m venv myenv_test”

Terminal Example: python -m venv myenv_test

You can replace “myenv_test” with whatever name you want. However, I’m going to keep mine as “myenv_test”
After executing this command, you’ll see a new folder in your project directory named “myenv_test” (or whatever you named your virtual environment).

Congratulations, you've created a virtual environment. The fun doesn’t end here though, as we still need to:
Activate it.

Install Libraries.
Handle a “requirements.txt” file.

The activation command varies depending on your operating system. If you're on Windows, type:

“myenv\Scripts\activate” and hit Enter

Terminal Example: myenv\Scripts\activate

For macOS or Linux users, you'll need to type: “source myenv/bin/activate”.

Terminal Example: source myenv/bin/activate

Once your virtual environment has been activated, you’ll notice that your terminal changes to include the name of your virtual environment (indicating that the environment is active). Nice, any packages you install now will be isolated within this environment.

If you’d like to deactivate this environment at any point, type deactivate and hit Enter. Your terminal will return to its normal state.

Terminal Example: deactivate

Once your virtual environment has been activated, you can install packages using pip as usual. For example, let’s install the “requests” library, by typing.

Terminal Example: pip install requests
Once executed, this command installs the requests library to the virtual environment.

NOTE: If you deactivate the environment and try to use the requests library, it won't work unless requests are also installed globally.

A good practice when working with virtual environments is to keep track of your dependencies using a requirements.txt file. You can generate this file by running:

Terminal Example: pip freeze > requirements.txt

This command lists all installed packages and their versions, and pipes them to a requirements.txt file, which you can then share with others, or use it to recreate the same environment on another machine.

To install dependencies from a requirements.txt file, just run:

Terminal Example: pip install -r requirements.txt

If you ever want to remove a virtual environment, just delete the environment folder (myen_test in my case).
Terminal Example: "Delete the myenv folder to remove the environment."

If you found this video helpful, don’t forget to give it a thumbs up and subscribe for more Python tips and tutorials.

Thanks for watching, and I’ll see you in the next one!
