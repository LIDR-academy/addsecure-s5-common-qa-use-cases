Feature: Python/C++ numeric equivalence for (a + b) * c
  As a QA engineer
  I want to verify that the Python and C++ implementations of (a + b) * c
  produce the same normalized output under IEEE 754 double-precision rules

  Background:
    Given the normalization contract uses IEEE 754 double-precision with 16 decimal places and ROUND_HALF_EVEN

  # ── Easy: integers and exact arithmetic ──────────────────────────────────────

  Scenario: C001 - Integer addition with exact result
    Given the inputs a=1, b=2, c=3
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C002 - Representation error from 0.1 + 0.2
    Given the inputs a=0.1, b=0.2, c=10
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C003 - Small numbers scaled back to human range
    Given the inputs a=1e-9, b=2e-9, c=1e9
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C004 - Large integer base with small addend
    Given the inputs a=1e15, b=1, c=2
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C005 - Mixed signs yielding a negative result
    Given the inputs a=-1.5, b=2.5, c=-3.0
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  # ── Medium: representation errors and identity ────────────────────────────────

  Scenario: C006 - All-zero inputs
    Given the inputs a=0.0, b=0.0, c=0.0
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C007 - Catastrophic cancellation amplified by large multiplier
    Given the inputs a=1e-15, b=-1e-15, c=1e15
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C008 - Representation error with fractional multiplier
    Given the inputs a=0.1, b=0.7, c=0.3
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C009 - Overflow to positive infinity
    Given the inputs a=1e308, b=1e308, c=1
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C010 - Catastrophic cancellation of large values
    Given the inputs a=-1e308, b=1e308, c=2
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  # ── Hard: corner cases from the normalization contract ───────────────────────

  Scenario: C011 - Representation error in all three operands
    Given the inputs a=0.3, b=0.6, c=0.1
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C012 - Negative zero normalization
    Given the inputs a=-0.0, b=0.0, c=5.0
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C013 - Identity operation preserving representation error
    Given the inputs a=0.1, b=0.0, c=1
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C014 - Representation error with unit multiplier
    Given the inputs a=0.3, b=0.6, c=1
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal

  Scenario: C015 - Subnormal number (smallest positive normal double)
    Given the inputs a=2.2e-308, b=0, c=1
    When Python evaluates (a + b) * c
    And C++ evaluates (a + b) * c
    Then the normalized outputs of Python and C++ are equal
