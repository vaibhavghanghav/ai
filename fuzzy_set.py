import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
input1 = ctrl.Antecedent(np.arange(0, 101, 1), 'input1')
input2 = ctrl.Antecedent(np.arange(0, 101, 1), 'input2')
similarity = ctrl.Consequent(np.arange(0, 101, 1), 'similarity')

# Define membership functions
input1['low'] = fuzz.trimf(input1.universe, [0, 0, 50])
input1['medium'] = fuzz.trimf(input1.universe, [25, 50, 75])
input1['high'] = fuzz.trimf(input1.universe, [50, 100, 100])

input2['low'] = fuzz.trimf(input2.universe, [0, 0, 50])
input2['medium'] = fuzz.trimf(input2.universe, [25, 50, 75])
input2['high'] = fuzz.trimf(input2.universe, [50, 100, 100])

similarity['low'] = fuzz.trimf(similarity.universe, [0, 0, 50])
similarity['medium'] = fuzz.trimf(similarity.universe, [25, 50, 75])
similarity['high'] = fuzz.trimf(similarity.universe, [50, 100, 100])

# Define rules
rule1 = ctrl.Rule(input1['low'] & input2['low'], similarity['low'])
rule2 = ctrl.Rule(input1['medium'] | input2['medium'], similarity['medium'])
rule3 = ctrl.Rule(input1['high'] & input2['high'], similarity['high'])

# Create control system
similarity_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
similarity_simulation = ctrl.ControlSystemSimulation(similarity_ctrl)

# Simulate with inputs
similarity_simulation.input['input1'] = 30
similarity_simulation.input['input2'] = 70
similarity_simulation.compute()

# Print output
print(f"Similarity score: {similarity_simulation.output['similarity']}")

# 7. Visualize results
aspect_ratio.view()
symmetry.view()
stroke_curvature.view()
similarity.view(similarity_simulation)
