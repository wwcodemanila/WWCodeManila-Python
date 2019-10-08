##  Goals

- [ ] Deploy your first Flask application to Heroku via GitHub

## Heroku

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

While they have a free plan that is ideal for experimenting with cloud applications in a limited sandbox, they also have good pricing options based on dynos consumed. Dynos are smart, lightweight containers built for modern languages and developer productivity. Basically, you only pay for what you use, prorated to the second.

## Creating a Heroku application

After signing up and logging in, you will be redirected to the dashboard.

It displays your account type, where the default is Personal. You can also create teams to collaborate with other people, although you need to add a valid credit card to do so. Below that, it lists all the applications that you have so far, its name (alyssonalvaran), application type (Python), stack type (heroku-16), and region (United States).

To create a new app, click the New button across your account type located on the upper right portion of your dashboard and select Create new app.

You will be asked to provide an app name and region. For demonstration purposes, I created an app named pineapples-on-pizza.

Once you select Create app, the next screen that will appear is the deploy tab of your newly created application. At this point, you can already access your app by selecting the Open app button on the upper right portion of your dashboard or going to <project-name>.herokuapp.com, which is my case is https://pineapples-on-pizza.herokuapp.com/.

Now that you’re done creating a Heroku app, the next thing that you have to do is to prepare your Flask app.

## Green unicorn

Green unicorn, or simply Gunicorn, is a Python Web Server Gateway Interface (WSGI) HTTP server for UNIX, ported from Ruby’s Unicorn project. Basically, this lightweight pre-fork worker model will enable us to deploy our Flask app to Heroku.

You can install this easily through pip.

```
$ pip3 install gunicorn
```

After installing, create a file named Procfile (yes, without an extension) and add this line here inside:

```
web: gunicorn app:app
```

## requirements.txt

That’s it! The final preparation that you have to do is to make sure that all of your packages are frozen to the text file requirements.txt. You can do this by simply entering this in the command line:

```
$ pip3 freeze > requirements.txt
```

## Connecting your Heroku app to a GitHub repository

Assuming that you have already pushed your latest changes to your GitHub repository, go back to the deploy tab of your Heroku application. In the Deployment method section, select GitHub. This opens the Connect to GitHub where you can search for a repository to connect to. Just search the name of your repository, which in my case is pineapples-on-pizza, and select the connect button.

Congratulations! Your Flask app is now deployed at pineapples-on-pizza.herokuapp.com!

## Bonus: Automatic deploys

You can automatically deploy your Heroku app everytime you push something to your GitHub repository by simply choosing a branch to deploy (default is Master) and selecting the Enable Automatic Deploys button in the Automatic deploys section of your Heroku app’s deploy tab.