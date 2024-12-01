def expert_system():
    print("Welcome to the Medical Expert System!")
    print("Answer the following questions with 'yes' or 'no'.\n")

    # Initial symptoms
    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()
    headache = input("Do you have a headache? ").lower()

    # Rules
    if fever == "yes" and cough == "yes" and sore_throat == "yes":
        print("\nDiagnosis: You may have the flu. Please consult a doctor.")
    elif fever == "yes" and headache == "yes":
        print("\nDiagnosis: You may have a viral infection. Stay hydrated and rest.")
    elif cough == "yes" and sore_throat == "yes":
        print("\nDiagnosis: You may have a cold. Drink warm fluids and rest.")
    else:
        print("\nDiagnosis: Symptoms are unclear. Please consult a doctor for a proper diagnosis.")

# Run the expert system
expert_system()
