# =========================================
# Nyaya Logic as an Inference Engine
# Forward-Chaining Rule-Based Expert System
# =========================================

# =========================================
# KNOWLEDGE BASE (Vyapti - Universal Rules)
# Each rule is of the form: (antecedents_list, consequent)
# Antecedents are stored as a list; a single-antecedent rule
# still uses a list for uniformity.
# =========================================

RULES = [
    (["smoke"], "fire"),
    (["fire"], "heat"),
    (["heat"], "high_temperature"),
    (["clouds"], "rain"),
    (["rain"], "wet_ground"),
    (["rain"], "cold_wind"),
    (["cold_wind"], "cold_weather"),
    (["cold_weather"], "wear_warm_clothes"),
    (["smoke", "hill_has_smoke"], "hill_has_fire"),
    (["fire"], "light"),
    (["light"], "visibility_possible"),
    (["wet_ground", "sun_shining"], "water_evaporating"),
    (["water_evaporating"], "high_humidity"),
    (["high_humidity", "dark_clouds"], "rain_likely"),
    (["rain_likely"], "carry_umbrella"),
    (["high_temperature", "high_humidity"], "humid_weather"),
]

# =========================================
# FORWARD-CHAINING INFERENCE ENGINE
# =========================================

def forward_chain(initial_facts, rules, verbose=True):
    """
    Forward-chaining inference engine.
    Derives new facts from initial facts using IF-THEN rules.

    Returns:
        working_memory : set of all known facts
        derived_facts  : list of derived facts in order
        conclusions    : list of terminal derived facts
        iterations     : number of passes made
    """
    working_memory = set(initial_facts)
    derived_facts = []
    used_facts = set()
    iteration = 0

    if verbose:
        print("\n" + "=" * 60)
        print("NYAYA INFERENCE ENGINE - FORWARD CHAINING")
        print("=" * 60)
        print("\n[Initial Facts - Pratyaksha]")
        for fact in sorted(working_memory):
            print(f"  * {fact}")

    while True:
        iteration += 1
        new_fact_derived = False
        newly_added = []

        if verbose:
            print(f"\n--- Iteration {iteration} ---")

        for number, (antecedents, consequent) in enumerate(rules, 1):
            if all(ant in working_memory for ant in antecedents):
                if consequent not in working_memory:
                    working_memory.add(consequent)
                    derived_facts.append(consequent)
                    used_facts.update(antecedents)
                    newly_added.append((number, antecedents, consequent))
                    new_fact_derived = True

        if verbose:
            if newly_added:
                print("[New Facts Derived - Upanaya & Nigamana]")
                for number, ant, cons in newly_added:
                    print(f"  Rule {number}: IF {ant} THEN {cons}")
            else:
                print("  No new facts derived.")

        if not new_fact_derived:
            break

    # Terminal derived facts: derived facts not used as any antecedent
    conclusions = [f for f in derived_facts if f not in used_facts]

    return working_memory, derived_facts, conclusions, iteration


# =========================================
# OUTPUT / DISPLAY MODULE
# =========================================

def display_results(working_memory, derived_facts, conclusions, iterations):
    print("\n" + "=" * 60)
    print("FINAL RESULTS - NIGAMANA (CONCLUSION)")
    print("=" * 60)

    print("\n[All Known Facts]")
    for fact in sorted(working_memory):
        print(f"  * {fact}")

    print(f"\n[Total Facts]: {len(working_memory)}")
    print(f"[Derived Facts]: {len(derived_facts)}")
    print(f"[Iterations]: {iterations}")

    if derived_facts:
        print("\n[Newly Derived Facts]")
        for fact in derived_facts:
            print(f"  + {fact}")

    print("\n[Final Conclusion(s)]")
    if conclusions:
        for c in conclusions:
            print(f"  [OK] {c}")
    else:
        print("  No final conclusion could be derived.")


# =========================================
# MAIN PROGRAM
# =========================================

def main():
    print("NYAYA LOGIC AS AN INFERENCE ENGINE")
    print("IKS Concept as CS Concept")
    print("=" * 60)

    print("\nAvailable facts you can use:")
    all_facts = set()
    for ant, cons in RULES:
        all_facts.update(ant)
        all_facts.add(cons)
    for fact in sorted(all_facts):
        print(f"  - {fact}")

    print("\nEnter initial facts separated by commas.")
    print("Example: smoke, hill_has_smoke, clouds")
    print("Type 'exit' to quit.\n")

    user_input = input("Enter facts: ").strip().lower()

    if user_input == "exit":
        print("Exiting...")
        return

    initial_facts = [f.strip() for f in user_input.split(",") if f.strip()]

    if not initial_facts:
        print("No facts entered. Exiting.")
        return

    working_memory, derived_facts, conclusions, iterations = forward_chain(
        initial_facts, RULES
    )
    display_results(working_memory, derived_facts, conclusions, iterations)


# =========================================
# ENTRY POINT
# =========================================

if __name__ == "__main__":
    main()