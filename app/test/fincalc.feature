Feature: Calculating an investment balance

  FinCalc is a financial calculator that can calculate an investment balance

#  Rule: Shouts have a range of approximately 1000 metres

  Scenario: Calculating an investment balance
      Given a financial calculator
      And some correct input parameters
      When we use the calculator
      Then we should receive a calculated investment balance

