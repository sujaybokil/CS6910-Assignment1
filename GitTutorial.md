# Welcome to the git tutorial !!!


1. Install Git for Windows/Linux/Mac from [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and configure it by entering your email Id and Username. For help visit this [link](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

2. Now use any shell of your choice Windows Powershell/Command Prompt/Ubuntu Terminal etc. and change directory to the one which you want to initialize a github repository in. Use the following command

    `cd path/to/directory`

3. Now, to initialize a repository in that directory, use the following command. 

    `git init`

    Else use `git clone url/of/repo` to clone an existing git repository

4. Before adding code, we have to configure a remote to the repo. A typical remote name used is "origin".

    `git remote add origin url`

5. Now, we are ready to make changes to the repo. Go ahead and add/change/delete some files. To stage your changes and commmit them, perform the following

    `git add -A && git commit -m "message"`

6. Now, let's push the changes to out repo so we can see them. If you are doing this for the first time, our remote branch has to be updated till the latest version of the repo, so we use the -f or force argument.

    `git push origin master -f`

    Now, from the next time, we can simply use the following command.

    `git push --set-upstream origin master` or `git push origin master`

7. Now, every time, you make changes and want to update them to the repository, we have to do a pull and push cycle after doing commits.

    `git pull origin master && git push origin master`

8. If Git asks for your Username and Password everytime u push code, do the following and the next time you push, it will remember your credentials.

    `git config credential.helper store`