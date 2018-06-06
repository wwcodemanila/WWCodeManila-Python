**Scenario: ** Partner A told Partner B that the client wants to input the dividend amount
instead of hardcoding it. Partner A will be on Boracay for a month long
vacation and she left to you this source file:

[explain_me](samples/explain_me.py ':include :type=code python')

As partner B, can you explain the code by just scanning it? Can you easily change
it to cater the new requirements?

Let's read [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.

From PEP8:
* Readability counts - code is read much more often that it is written!
* The guideline is intended to improve the readability of code and make it consistent.
* It is a guide not a law!

Now, which of the ff. are PEP8 compliant?

``` python
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

or

```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

```