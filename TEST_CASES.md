
Save with `Ctrl+S`.

---

## STEP 3: Copy the TEST_CASES Content

Open `TEST_CASES.md` in VS Code and paste this:

```markdown
# Test Cases and Results

**Project:** Nyaya Logic as an Inference Engine

---

## Summary Table

| Test | Initial Facts | Derived Facts (in order) | Terminal Derived Facts |
|---|---|---|---|
| TC01 | smoke | fire, heat, high_temperature, light | high_temperature, light |
| TC02 | clouds | rain, wet_ground | wet_ground |
| TC03 | smoke, hill_has_smoke | fire, heat, high_temperature, hill_has_fire, light | high_temperature, hill_has_fire, light |
| TC04 | rain, cold_wind | wet_ground, cold_weather, wear_warm_clothes | wet_ground, wear_warm_clothes |
| TC05 | wet_ground, sun_shining | water_evaporating, high_humidity | high_humidity |
| TC06 | high_humidity, dark_clouds | rain_likely, carry_umbrella | carry_umbrella |
| TC07 | light, night | visibility_possible | visibility_possible |
| TC08 | fire, high_humidity | heat, high_temperature, light, humid_weather | light, humid_weather |
| TC09 | clouds, cold_wind | rain, wet_ground, cold_weather, wear_warm_clothes | wet_ground, wear_warm_clothes |
| TC10 | smoke, clouds, sun_shining | fire, heat, high_temperature, rain, wet_ground, light, water_evaporating, high_humidity, humid_weather | light, humid_weather |
| TC11 | rain, dark_clouds, sun_shining | wet_ground, water_evaporating, high_humidity, rain_likely, carry_umbrella | carry_umbrella |
| TC12 | night, cold_wind | None | None |

---

## Detailed Results

### TC01 — Single chain from one fact
**Initial facts:** smoke  
**Iteration 1:** Rule 1 → fire; Rule 2 → heat; Rule 3 → high_temperature; Rule 10 → light  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** high_temperature, light

### TC02 — Short chain (clouds to wet ground)
**Initial facts:** clouds  
**Iteration 1:** Rule 4 → rain; Rule 5 → wet_ground  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** wet_ground

### TC03 — Rule with two antecedents (Rule 9)
**Initial facts:** smoke, hill_has_smoke  
**Iteration 1:** Rule 1 → fire; Rule 2 → heat; Rule 3 → high_temperature; Rule 9 → hill_has_fire; Rule 10 → light  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** high_temperature, hill_has_fire, light

### TC04 — Chain through rain and cold wind
**Initial facts:** rain, cold_wind  
**Iteration 1:** Rule 5 → wet_ground; Rule 7 → cold_weather; Rule 8 → wear_warm_clothes  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** wet_ground, wear_warm_clothes

### TC05 — Two-antecedent chain
**Initial facts:** wet_ground, sun_shining  
**Iteration 1:** Rule 12 → water_evaporating; Rule 13 → high_humidity  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** high_humidity

### TC06 — Two-antecedent rule (Rule 14) followed by a chain
**Initial facts:** high_humidity, dark_clouds  
**Iteration 1:** Rule 14 → rain_likely; Rule 15 → carry_umbrella  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** carry_umbrella

### TC07 — Two-antecedent rule (Rule 11) only
**Initial facts:** light, night  
**Iteration 1:** Rule 11 → visibility_possible  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** visibility_possible

### TC08 — Chain from fire and high humidity
**Initial facts:** fire, high_humidity  
**Iteration 1:** Rule 2 → heat; Rule 3 → high_temperature; Rule 10 → light; Rule 16 → humid_weather  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** light, humid_weather

### TC09 — Two independent inputs giving a chain
**Initial facts:** clouds, cold_wind  
**Iteration 1:** Rule 4 → rain; Rule 5 → wet_ground; Rule 7 → cold_weather; Rule 8 → wear_warm_clothes  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** wet_ground, wear_warm_clothes

### TC10 — Independent chains that merge at Rule 16
**Initial facts:** smoke, clouds, sun_shining  
**Iteration 1:** Rule 1 → fire; Rule 2 → heat; Rule 3 → high_temperature; Rule 4 → rain; Rule 5 → wet_ground; Rule 10 → light; Rule 12 → water_evaporating; Rule 13 → high_humidity; Rule 16 → humid_weather  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** light, humid_weather

### TC11 — Chain through rain, dark clouds, and sun
**Initial facts:** rain, dark_clouds, sun_shining  
**Iteration 1:** Rule 5 → wet_ground; Rule 12 → water_evaporating; Rule 13 → high_humidity; Rule 14 → rain_likely; Rule 15 → carry_umbrella  
**Iteration 2:** No new fact; engine stops.  
**Terminal derived facts:** carry_umbrella

### TC12 — Negative test: no rule applies
**Initial facts:** night, cold_wind  
**Iteration 1:** No rule matches, so no new fact is derived.  
**Terminal derived facts:** None