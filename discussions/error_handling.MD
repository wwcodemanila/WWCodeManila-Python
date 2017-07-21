## Error handling

When you run the code below, do you expect it to be like a Eutopian world, one with no errors?

```python
age = input('Enter your age:')
print('You are {} next year!'.format(input + 1))
```

Nope. The user can input `19` but s/he can also input `foo` which is not a valid age/number. Can you try to input `foo` and see what happens?
Did you get also the following error?

```shell
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'foo'
```

My two cents - Do not be terrified when your best friend, the Python interpreter, returns/raises an error. S/he is just telling you that something bad happened and you can try to help her/him to handle the error.

### Your Challenge
1. As a Python ninja:
  *  Learn how to [handle exceptions](https://wiki.python.org/moin/HandlingExceptions).
  *  Learn how to ask for forgiveness but also know when to take caution first, [EAFP vs LBYL](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#eafp-vs-lbyl).
  *  Know that sometimes it's [okay to fail](https://realpython.com/blog/python/the-most-diabolical-python-antipattern/).
2. Rewrite the code above to handle error.
  * Be creative! *Tip*: You may just notify the user for his/her mistake or ask him/her for a new input ;)
3. Share your work and contribute to the community! Complete how-to share your work instruction [here](https://github.com/wwcodemanila/WWCodeManila-Python/blob/master/exercise_upload_step.md).
  * Create a Github account if none yet and create a repository for wwcode-python. You will upload your works there.
  * Please upload or push the file in your GIT repository.
  * Open an issue in our repository named `<Your name> - <topic>`. For example, `John Doe - Loops`.
  * Share the link of your work on the issue.
4. Present your work in front (#ApplaudHer)! You can also share your study group experience in social media and tag us!
5. Enjoy!
  
  
### Deep Dive
*  [Pep 463](http://legacy.python.org/dev/peps/pep-0463/): Exception-catching expressions
*  [Diaper Pattern](http://mike.pirnat.com/2009/05/09/the-diaper-pattern-stinks/) also known as [Pokemon Exception Handling](http://wiki.c2.com/?PokemonExceptionHandling)

## Further Challenge
* [Hackerrank](https://www.hackerrank.com/)
* [Checkio](https://checkio.org/)
* [Codefights](https://codefights.com/)
* [Codinggame](https://www.codingame.com/)
