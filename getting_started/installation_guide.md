We need to install the **Python interpreter** first! 

!> For our study group, we will be using `Python 3`, preferably >= `Python 3.6`.

You also need to have a **text editor** to write your code in. This can be (but not limited to) one of the following:

* [Atom](https://atom.io)
* [Gedit](https://wiki.gnome.org/Apps/Gedit)
* [Notepad++](https://notepad-plus-plus.org)
* [Sublime Text](https://www.sublimetext.com)
* [Visual Studio Code](https://code.visualstudio.com)



## Check existing Python installation

To check if Python is already installed in your system, open your terminal or command prompt.

- For Windows users, search for `cmd`
- For Linux and Mac users, search for `terminal`

After opening the terminal/command prompt(cmd), type the following command.
```shell
python --version
```

or

```shell
python3 --version
```

This will tell you what version of python is currently installed in your computer.

```shell
Python 3.6.0

```
> If python 3 is already installed, skip the next part.


## Tutorial

For a detailed installation process, you can [use this tutorial](https://tutorial.djangogirls.org/en/python_installation).

### Windows and OS X

1. Download the installer for the latest version from the [Python Software Foundation](https://www.python.org/downloads/release).
2. Run the installer by double-clicking it, and following the succeeding instructions.

!> For **Windows** users, please don't forget to add Python in your PATH as per below.

![Add Python to PATH](https://eavictor.files.wordpress.com/2016/05/add_python_3-5_to_pathinstall_now.png?w=594)


!> For **OS X** users, ensure your Mac settings allow installing packages that are not from the App Store. Go to `"System Preferences" > "Security & Privacy," > "General"`. Set "Allow apps downloaded from:" to "Mac App Store and identified developers."


### Linux

Check the Linux distrubution using the `terminal`

```
grep ^NAME= /etc/os-release
```

Type one of the following commands in the `termimal` depending on your respective Linux distribution.

* **Debian** or **Ubuntu**

    ```
    sudo apt install python3
    ```

* **Fedora**

    ```
    sudo dnf install python3
    ```

* **openSUSE**

    ```
    sudo zypper intall python3
    ```

You can also try [compiling from source](https://realpython.com/installing-python/#compiling-python-from-source) if you want the latest version or an alternative installation of Python.

### Chromebook

For Chromebook users, you'll need to connect to a cloud IDE provider. You can follow [these instructions](https://tutorial.djangogirls.org/en/chromebook_setup).  



Finally, [check if you have successfully installed Python](#check-existing-python-installation).


Done! You can now start coding in Python!

## Put your thinking cap on!

- What are my challenges upon installing Python? How did I solved them?
- [Do I need Python 2 or 3?](https://wiki.python.org/moin/Python2orPython3)
- What are the differences between Python 2 and 3?
