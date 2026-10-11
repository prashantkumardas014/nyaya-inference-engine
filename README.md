<div align="center">

# Nyaya Logic as an Inference Engine

### A Rule-Based Expert System Inspired by Indian Knowledge Systems

<br/>

**Prashant Kumar Das**  
T.Y.B.Sc. Computer Science — Semester V

**Under the guidance of**  
Asst. Prof. Sini. V.

**Smt. Devkiba Mohansinhji Chauhan College of Commerce & Science, Silvassa**  
*(Affiliated to University of Mumbai)*

**Academic Year: 2026–27**

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)](.)
[![Type](https://img.shields.io/badge/Type-Educational-blue?style=flat-square)](.)
[![License](https://img.shields.io/badge/License-Academic-lightgrey?style=flat-square)](.)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen?style=flat-square)](.)

</div>

---

## Abstract

This project presents an educational implementation of a **rule-based expert system** that performs **forward-chaining inference** using IF-THEN production rules. The system is designed as a computational analogue of **Nyaya**, one of the six orthodox schools of Indian philosophy, specifically drawing on the Nyaya theory of ***anumāna*** (inference) and the five-membered syllogism known as ***Pañcāvayava Vākya***.

The implementation demonstrates how selected concepts from an Indian Knowledge System (IKS) can be mapped onto the components of classical Artificial Intelligence — a rule base, a working memory, an inference engine, and a fact-derivation cycle. The program is written in Python 3, requires no external libraries, and serves as a pedagogical bridge between Indian philosophy and modern computational reasoning.

**Keywords:** Nyaya, Anumāna, Forward Chaining, Rule-Based Systems, Expert Systems, Indian Knowledge Systems, Artificial Intelligence.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Background](#2-background)
3. [System Design](#3-system-design)
4. [Conceptual Mapping](#4-conceptual-mapping)
5. [Algorithm](#5-algorithm)
6. [Implementation](#6-implementation)
7. [Testing](#7-testing)
8. [Complexity Analysis](#8-complexity-analysis)
9. [Limitations](#9-limitations)
10. [Conclusion](#10-conclusion)
11. [Repository Structure](#11-repository-structure)
12. [Author](#12-author)
13. [References](#13-references)

---

## 1. Introduction

Nyaya is one of the six orthodox (*āstika*) schools of Indian philosophy, traditionally attributed to Gautama (Akṣapāda). Its foundational text, the *Nyaya Sutra*, is principally concerned with logic, epistemology, and the methods of valid reasoning. In Nyaya, valid knowledge (*pramā*) is obtained through a *pramāṇa* — a means of valid knowledge.

This project focuses on ***anumāna*** (inference), the second of the four recognised pramāṇas. Nyaya presents a well-formed inference as a five-membered argument, the ***Pañcāvayava Vākya***:

| Member | Sanskrit | Function |
|:---:|:---|:---|
| 1 | **Pratijñā** | Proposition to be established |
| 2 | **Hetu** | Reason offered in support |
| 3 | **Udāharāṇa** | General rule with familiar example |
| 4 | **Upanaya** | Application to the present case |
| 5 | **Nigamana** | Conclusion |

The classical illustration — inferring fire on a hill from the presence of smoke — forms the textbook example used throughout this project.

---

## 2. Background

### 2.1 Indian Knowledge Systems (Nyaya)

Nyaya recognises four *pramāṇas*: *pratyakṣa* (perception), *anumāna* (inference), *upamāna* (comparison), and *śabda* (verbal testimony). This project models only *anumāna*, and only a simplified view of it. Nyaya's broader framework — sixteen *padārthas*, theories of doubt (*saṃśaya*), fallacious reasons (*hetvabhāsa*), and debate (*vāda*) — is not modelled.

### 2.2 Rule-Based Expert Systems (CS)

A rule-based expert system stores knowledge as **facts** and **IF-THEN production rules**. Its **inference engine** repeatedly matches rule antecedents against facts in working memory and adds the consequents of matching rules as new facts. When this process is data-driven (starting from known facts and moving towards conclusions), it is called **forward chaining**. The engine terminates when a complete pass produces no new fact.

### 2.3 Motivation

The two traditions — Nyaya inference and rule-based AI — share a recognisable pattern: *from what is already known, a general relation is applied to reach a new statement*. This project uses that pattern as a computational analogy, without claiming that the two are identical.

---

## 3. System Design

### 3.1 Architecture

```
┌──────────────────────┐
│   User Input         │
│   (initial facts)    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Working Memory     │
│   (fact set)         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Knowledge Base     │
│   (IF-THEN rules)    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Rule Matching      │
│   (antecedents vs.   │
│    facts)            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Inference Engine   │
│   (forward chaining) │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Output             │
│   (derived facts +   │
│    terminal facts)   │
└──────────────────────┘
```

### 3.2 Components

| Component | Description |
|:---|:---|
| **Working Memory** | Set of facts currently known to the system |
| **Knowledge Base** | Predefined list of `(antecedents, consequent)` IF-THEN rules |
| **Rule Matcher** | Tests whether all antecedents of a rule are present in working memory |
| **Inference Engine** | Iterates over rules until no new fact can be derived |
| **Output Module** | Displays all facts, derived facts, iteration count, and terminal facts |

### 3.3 Design Principles

- **Zero dependencies** — written in pure Python 3, no external libraries
- **Deterministic** — rules evaluated in a fixed order; no randomness
- **Transparent** — every derived fact is traced to the rule that produced it
- **Self-contained** — single-file executable with a CLI interface

---

## 4. Conceptual Mapping

The following table lists the correspondences used in this project. Each mapping is approximate: the Nyaya terms have philosophical meanings that a software component can only partially represent.

| Nyaya Concept | CS Representation | Remarks |
|:---|:---|:---|
| **Pramāṇa** | Facts + rules (KB + input) | Nyaya: means of knowing, not a data store |
| **Pratyakṣa** | Initial facts entered by user | Only perception-like input is modelled |
| **Anumāna** | Inference engine (forward chaining) | Only derivation step is modelled |
| **Vyāpti** | IF-THEN production rule | Nyaya requires invariable relation; here, only assumed implication |
| **Pakṣa** | Working memory (current facts) | Loose analogy — Pakṣa is a specific subject |
| **Hetu** | Rule antecedent (IF part) | Nyaya also checks whether the hetu is valid |
| **Sādhya** | Rule consequent (THEN part) | — |
| **Pañcāvayava Vākya** | Goal → facts → rule → match → fact | Used for comparison only |
| **Nigamana** | Derived fact / program output | — |
| **Tarka** | Backward chaining | Not implemented |
| **Nirṇaya** | No direct equivalent | Termination ≠ settled knowledge |

> **Note:** This mapping is pedagogical, not philosophical. Nyaya cannot be reduced to a computer program.

---

## 5. Algorithm

### 5.1 Input

A set of initial facts entered by the user as comma-separated names (e.g., `smoke, clouds, wet_ground`).

### 5.2 Output

1. The complete set of known facts.
2. The list of derived facts, in the order they were derived.
3. The number of iterations performed.
4. The **terminal derived facts** — derived facts that were not used as a condition by any fired rule.

### 5.3 Pseudocode

```
ALGORITHM Nyaya_Inference_Engine

1.  Initialize Working Memory    = {}
2.  Initialize Knowledge Base    = predefined rules
3.  Initialize Derived Facts     = []
4.  Initialize Used Facts        = {}
5.  Initialize iteration         = 0

6.  Read initial facts from the user
7.  Add all initial facts to Working Memory

8.  REPEAT
9.      iteration += 1
10.     new_fact_derived = FALSE
11.     FOR each rule in Knowledge Base DO
12.         IF all antecedents of rule are in Working Memory THEN
13.             IF consequent is NOT in Working Memory THEN
14.                 Add consequent to Working Memory
15.                 Append consequent to Derived Facts
16.                 Add all antecedents to Used Facts
17.                 new_fact_derived = TRUE
18.             END IF
19.         END IF
20.     END FOR
21. UNTIL new_fact_derived = FALSE

22. Terminal Derived Facts = Derived Facts − Used Facts
23. Display all facts, derived facts, iteration count, terminal facts

END ALGORITHM
```

### 5.4 Nyaya Correspondence

| Algorithm Step | Nyaya Concept (Analogy) |
|:---:|:---|
| Read initial facts | *Pratyakṣa* — perception-like input |
| Start a pass over rules | *Pakṣa* — current subject, loosely |
| Test rule antecedents | *Vyāpti* (rule) and *Hetu* (reason) |
| Derive consequent | *Upanaya* → conclusion |
| Stop when no new fact | Termination — no Nyaya equivalent |
| Display derived facts | *Nigamana* — conclusion |

---

## 6. Implementation

The program is written in Python 3 and uses no external libraries. It is saved as **`nyaya_engine.py`** and executed with:

```bash
python nyaya_engine.py
```

### 6.1 Sample Execution

```console
$ python nyaya_engine.py

NYAYA LOGIC AS AN INFERENCE ENGINE
IKS Concept as CS Concept
════════════════════════════════════════════════════════════════

Available facts you can use:
  - carry_umbrella
  - clouds
  - cold_weather
  - cold_wind
  - dark_clouds
  - fire
  - heat
  - high_humidity
  - high_temperature
  - hill_has_fire
  - hill_has_smoke
  - humid_weather
  - light
  - night
  - rain
  - rain_likely
  - smoke
  - sun_shining
  - visibility_possible
  - water_evaporating
  - wear_warm_clothes
  - wet_ground

Enter initial facts separated by commas.
Example: smoke, hill_has_smoke, clouds
Type 'exit' to quit.

Enter facts: smoke, hill_has_smoke

════════════════════════════════════════════════════════════════
NYAYA INFERENCE ENGINE - FORWARD CHAINING
════════════════════════════════════════════════════════════════

[Initial Facts - Pratyaksha]
  * hill_has_smoke
  * smoke

--- Iteration 1 ---
[New Facts Derived - Upanaya & Nigamana]
  Rule 1: IF ['smoke'] THEN fire
  Rule 2: IF ['fire'] THEN heat
  Rule 3: IF ['heat'] THEN high_temperature
  Rule 9: IF ['smoke', 'hill_has_smoke'] THEN hill_has_fire
  Rule 10: IF ['fire'] THEN light

--- Iteration 2 ---
  No new facts derived.

════════════════════════════════════════════════════════════════
FINAL RESULTS - NIGAMANA (CONCLUSION)
════════════════════════════════════════════════════════════════

[All Known Facts]
  * fire
  * heat
  * high_temperature
  * hill_has_fire
  * hill_has_smoke
  * light
  * smoke

[Total Facts]:    7
[Derived Facts]:  5
[Iterations]:     2

[Newly Derived Facts]
  + fire
  + heat
  + high_temperature
  + hill_has_fire
  + light

[Final Conclusion(s)]
  [OK] high_temperature
  [OK] hill_has_fire
  [OK] light
```

### 6.2 Knowledge Base

The program contains **16 production rules** (*vyāpti*), covering weather, visibility, temperature, and everyday reasoning scenarios. Rules are stored as a list of `(antecedents, consequent)` tuples, where antecedents are always a list (uniformity for single- and multi-antecedent rules).

---

## 7. Testing

Twelve test cases were executed to verify the engine's correctness. They cover single-fact chains, multi-antecedent rules, merged chains, and a negative case.

### 7.1 Summary

| Test | Initial Facts | Terminal Derived Facts |
|:---:|:---|:---|
| TC01 | `smoke` | `high_temperature`, `light` |
| TC02 | `clouds` | `wet_ground` |
| TC03 | `smoke, hill_has_smoke` | `high_temperature`, `hill_has_fire`, `light` |
| TC04 | `rain, cold_wind` | `wet_ground`, `wear_warm_clothes` |
| TC05 | `wet_ground, sun_shining` | `high_humidity` |
| TC06 | `high_humidity, dark_clouds` | `carry_umbrella` |
| TC07 | `light, night` | `visibility_possible` |
| TC08 | `fire, high_humidity` | `light`, `humid_weather` |
| TC09 | `clouds, cold_wind` | `wet_ground`, `wear_warm_clothes` |
| TC10 | `smoke, clouds, sun_shining` | `light`, `humid_weather` |
| TC11 | `rain, dark_clouds, sun_shining` | `carry_umbrella` |
| TC12 | `night, cold_wind` | *(none — negative test)* |

### 7.2 Result

In every case, the derived facts matched expected outputs, and terminal derived facts were computed correctly. Full details are documented in **[`TEST_CASES.md`](TEST_CASES.md)**.

---

## 8. Complexity Analysis

Let:

- **r** = number of rules
- **a** = average number of antecedents per rule
- **f** = number of facts in working memory
- **i** = number of iterations until no new fact is derived

### 8.1 Time Complexity

Each iteration examines every rule once. Testing a rule's antecedents against working memory (a hash set) costs *O(1)* per antecedent on average. Therefore:

**One iteration:** `O(r × a)`  
**Total time:** `O(i × r × a)`

Since every iteration except the last adds at least one new fact, `i ≤ d + 1`, where `d` is the number of derived facts (`d ≤ f`). In the worst case:

**Worst-case time:** `O(f × r × a)`

For the supplied program (r = 16, a ≤ 2, fixed fact vocabulary), the running time is effectively **O(1)**.

### 8.2 Space Complexity

| Component | Space |
|:---|:---|
| Working memory | `O(f)` |
| Derived facts list | `O(f)` |
| Rule base | `O(r × a)` |
| **Total** | **`O(f + r × a)`** |

Space grows linearly in the number of facts and rules and remains small for the fixed demonstration set.

---

## 9. Limitations

The implementation is an educational demonstration with the following scope constraints:

1. **Simplified Nyaya representation.** Only *anumāna* is modelled — Nyaya includes sixteen *padārthas*, four *pramāṇas*, and a theory of debate.
2. **Hand-written rules.** Some are simplified; for example, `clouds → rain` is not universally true and would not qualify as a *vyāpti* in the Nyaya sense.
3. **Redundant rule.** Rule 9 (`smoke + hill_has_smoke → hill_has_fire`) is redundant, since Rule 1 already derives `fire` from `smoke`.
4. **No validity checking.** The engine does not test whether a *hetu* is faulty (*hetvabhāsa*).
5. **No uncertainty.** Facts are either present or absent; *saṃśaya* (doubt) and probabilistic reasoning are not modelled.
6. **No backward chaining.** Only data-driven reasoning is implemented; goal-driven reasoning is not.
7. **Limited explanation.** The program shows which rule produced each fact but does not generate a full five-step Nyaya argument.
8. **Fixed rule order.** No conflict-resolution strategy is implemented.
9. **No learning or time.** Facts are static, rules are not learned, and time is not modelled.
10. **Educational purpose only.** The program has not been validated for real-world use.

---

## 10. Conclusion

This project implemented a small Nyaya-inspired rule-based inference engine and demonstrated how selected concepts from an Indian Knowledge System can be mapped onto components of classical Artificial Intelligence. The engine accepts initial facts, applies forward chaining over a predefined knowledge base, and derives new facts until no further inference is possible.

The conceptual mapping shows that initial facts correspond loosely to *pratyakṣa*, rules to *vyāpti*, rule antecedents to *hetu*, and derived facts to *nigamana* — while also stating clearly where the analogy does not hold. Testing across twelve cases confirmed correct behaviour on single chains, multi-antecedent rules, merged chains, and the negative case.

The project does **not** claim that Nyaya can be reduced to a computer program. Rather, it uses the analogy as a pedagogical bridge — helping students of computer science appreciate the logical sophistication of Indian Knowledge Systems, and helping students of IKS see how classical ideas can inform modern computational thinking.

---

## 11. Repository Structure

```
nyaya-inference-engine/
│
├── IKS_REPORT_PRASHANT_DAS.pdf    Full project report
├── nyaya_engine.py                 Python source code
├── README.md                       This file
└── TEST_CASES.md                   Detailed test documentation
```

---

## 12. Author

**Prashant Kumar Das**  
T.Y.B.Sc. Computer Science — Semester V  
Smt. Devkiba Mohansinhji Chauhan College of Commerce & Science, Silvassa  
*(Affiliated to University of Mumbai)*

**Guide:** Asst. Prof. Sini. V.  
**Academic Year:** 2026–27

[![GitHub](https://img.shields.io/badge/GitHub-prashantkumardas014-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/prashantkumardas014)

---

## 13. References

1. Gautama. *Nyaya Sutra*. (Trans. by various scholars.)
2. Chatterjee, S. C. *The Nyaya Theory of Knowledge*. University of Calcutta.
3. Matilal, B. K. *The Character of Logic in India*. SUNY Press.
4. Russell, S., & Norvig, P. *Artificial Intelligence: A Modern Approach*. Pearson.
5. Giarratano, J., & Riley, G. *Expert Systems: Principles and Programming*. Cengage.

---

<div align="center">

*This project is submitted as part of academic coursework for the*  
**Indian Knowledge Systems (IKS)** *component of the*  
*T.Y.B.Sc. Computer Science programme.*

**For educational purposes only.**

</div>
