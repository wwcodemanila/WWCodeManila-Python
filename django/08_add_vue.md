## Goals
- [ ] Install NPM
- [ ] Install VueCLI
- [ ] Add Vue to application

## Install NPM
Go to `https://nodejs.org/en/download/`, download the latest or the LTS version of Node. Install node with the recommended settings. Check if Node and NPM is installed by checking in your terminal:

```
> npm --version
6.14.14
> node --version
v14.17.4
```

## Install VueCLI
Once the NodeJS has been installed in your computer, you may now install the VueCLI. In your terminal, type this command:
```
sudo npm i -g @vue/cli
```
Then test if its working by typing 
```
vue create hello-vue
Vue CLI v4.5.13
? Please pick a preset: Manually select features
? Check the features needed for your project: Choose Vue version, Babel, Router, Linter
? Choose a version of Vue.js that you want to start the project with 2.x
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
? Pick a linter / formatter config: Prettier
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) N
```

Wait for a few minutes, then once completed, will show a prompt like this:

```
📄  Generating README.md...

🎉  Successfully created project hello-vue2.
👉  Get started with the following commands:

 $ cd hello-vue
 $ npm run serve
```

Go to `hello-vue` and type `npm run serve`. It will remind you to access to `http://localhost:<port>/`. Go to that url and check if Vue is showing. This indicates that Vue is properly installed to your computer. 


## Add Vue to application
We are going to create a simple Vue project in our Django project. Ensure that the project name is `frontend`, like so:
```
vue create frontend
```

Set the config like the ones below:
```
vue create hello-vue
Vue CLI v4.5.13
? Please pick a preset: Manually select features
? Check the features needed for your project: Choose Vue version, Babel, Router, Linter
? Choose a version of Vue.js that you want to start the project with 2.x
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
? Pick a linter / formatter config: Prettier
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) N
```

Then, we're going to install a package `webpack-bundle-tracker` to keep track of the code in our frontend application.
Go to `frontend` folder then install the webpack tracker:
```
cd frontend 

npm install --save-dev webpack-bundle-tracker@0.4.3
```

Next, create a file inside the folder `frontend`. Name it `vue.config.js`.
```
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    // on Windows you might want to set publicPath: "http://127.0.0.1:8080/" 
    publicPath: "http://127.0.0.1:8081/", 
    outputDir: './dist/',

    chainWebpack: config => {

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}])

        config.output
            .filename('bundle.js')

        config.optimization
        	.splitChunks(false)

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            // the first 3 lines of the following code have been added to the configuration
            .public('http://127.0.0.1:8080')    
            .host('127.0.0.1')    
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": ["\*"]})

    },

    // uncomment before executing 'npm run build' 
    // css: {
    //     extract: {
    //       filename: 'bundle.css',
    //       chunkFilename: 'bundle.css',
    //     },
    // }

};

```

Next, we are going to install a webpack loader in Django environment. This will help us read the changes given by the bundle tracker. 
```
pip install django-webpack-loader==0.7.0
```

Update the requirements.txt file.
```
pip freeze > requirements.txt
```

Then add the webpack_loader library to `settings.py`.
```
INSTALLED_APPS = [
    'webpack_loader',
]

// on the bottom of settings.py file
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': BASE_DIR / 'frontend' / 'webpack-stats.json'
    }
}
```

Add this code inside the file `templates/index.html`, on the first line of the code:
```
{% load render_bundle from webpack_loader %}
```
Also, add this inside the body of the code, after the div id app:
```
{% render_bundle 'app' %}
```

The index file should look this this:
```
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forum App</title>
</head>
<body>

    <h1> Vue JS</h1>

    <div id="app"></div>

    {% render_bundle 'app' %}
    
</body>
</html>
```

Run server of both django and vue separately. 
```
python manage.py runserver

npm run serve
```


(Optional) You may also explore the vue project by typing this command. 
```
vue ui
```