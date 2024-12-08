import math

#Select priorities as per Manual
def get_unique_priorities(categories, priority_values):
    priorities = {}
    for category in categories:
        while True:
            try:
                priority = int(input(f"Enter a priority level (0-4) for {category}: "))
                if priority not in range(5):
                    print("Priority must be between 0 and 4.")
                elif priority in priorities.values():
                    print("Priority already assigned. Choose a different one.")
                else:
                    priorities[category] = priority
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 4.")
    return priorities

def spend_advantage_points(advantage_points, race):
    print(f"\nYou have {advantage_points} advantage points to spend on the following advantages:")

    # List of advantages with costs
    advantages = {
        "Ambidextrous": 1,
        "Exceptional Attribute": 2,  # Only for Human characters
        "Extra Edge": [1, 2, 3],  # Variable cost
        "Land Grant": 1,
        "Natural Aptitude (Non-Combat Skill)": 2,
        "Natural Aptitude (Combat Skill)": 3,
        "Sixth Sense": 2,
        "Title (Knight)": 1,
        "Title (Baronet)": 2,
        "Title (Baron)": 3,
        "Toughness": 2,
        "Wealth (5,000 C-Bills)": 1,
        "Wealth (50,000 C-Bills)": 2,
        "Wealth (500,000 C-Bills)": 3,
        "Well-Equipped (1,000 C-Bills)": 1,
        "Well-Equipped (5,000 C-Bills)": 2,
        "Well-Equipped (25,000 C-Bills)": 3
    }

    purchased_advantages = {}
    exceptional_attribute = None
    remaining_points = advantage_points

    # Automatically add "Toughness" for Elementals
    if race == "Elemental":
        purchased_advantages["Toughness"] = "Included (Free) 0"
        print("As an Elemental, you already have 'Toughness' included for free and cannot purchase it again.")

    while remaining_points > 0:
        print(f"\nRemaining Advantage Points: {remaining_points}")
        print("\nAvailable Advantages:")
        for i, (advantage, cost) in enumerate(advantages.items(), start=1):
            if advantage in purchased_advantages:
                continue  # Skip already purchased advantages
            if isinstance(cost, list):
                cost_str = f"{cost[0]}-{cost[-1]} points"
            else:
                cost_str = f"{cost} points"
            print(f"{i}. {advantage} ({cost_str})")

        try:
            # Select an advantage
            choice = int(input("Enter the number of the advantage you want to purchase: ")) - 1
            if choice < 0 or choice >= len(advantages):
                print("Invalid choice. Please select a valid advantage number.")
                continue

            selected_advantage = list(advantages.keys())[choice]
            cost = advantages[selected_advantage]

            # Check if the advantage has already been purchased
            if selected_advantage in purchased_advantages:
                print(f"You have already purchased {selected_advantage}. Each advantage can only be purchased once.")
                continue

            # Handle race-specific restrictions
            if selected_advantage == "Toughness" and race == "Elemental":
                print("Elementals already have Toughness and cannot purchase it again.")
                continue

            if selected_advantage == "Exceptional Attribute":
                if race != "Human":
                    print("The Exceptional Attribute advantage is only available to Human characters.")
                    continue
                exceptional_attribute = input("Select the attribute (BUILD, REFLEX, LEARN, CHARISMA, INTUITION) to exceed the racial maximum: ").strip().upper()
                if exceptional_attribute not in ["BUILD", "REFLEX", "LEARN", "CHARISMA", "INTUITION"]:
                    print("Invalid attribute. Please select a valid attribute.")
                    continue

            # Handle variable cost advantages
            if isinstance(cost, list):
                cost = int(input(f"Enter the cost for {selected_advantage} ({cost[0]}-{cost[-1]} points): "))
                if cost not in advantages[selected_advantage]:
                    print(f"Invalid cost. Please select a cost within the range {advantages[selected_advantage]}.")
                    continue

            # Check if enough points are available
            if remaining_points >= cost:
                purchased_advantages[selected_advantage] = purchased_advantages.get(selected_advantage, 0) + cost
                remaining_points -= cost
                print(f"Purchased {selected_advantage} for {cost} points.")
            else:
                print(f"Not enough points to purchase {selected_advantage}. You need {cost} points.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid choice. Please select a valid advantage number.")

        # Stop if no points remain
        if remaining_points <= 0:
            print("\nYou have used all your advantage points.")
            break

    print("\nAdvantage Purchase Complete:")
    for advantage, cost in purchased_advantages.items():
        print(f"{advantage}: {cost} points")

    return purchased_advantages, exceptional_attribute

def assign_attribute_points(attributes_points, race, exceptional_attribute=None):
    print(f"\nYou have {attributes_points} attribute points to distribute among the five attributes: BUILD, REFLEX, LEARN, CHARISMA, and INTUITION.")
    print(f"The maximum values for attributes are based on your race ({race}):")

    # Define race-specific maximums and modifiers
    race_data = {
        "Human": {
            "modifiers": {"BUILD": 0, "REFLEX": 0, "LEARN": 0, "CHARISMA": 0, "INTUITION": 0},
            "maximums": {"BUILD": 6, "REFLEX": 6, "LEARN": 6, "CHARISMA": 6, "INTUITION": 6}
        },
        "Clan Warrior": {
            "modifiers": {"BUILD": 0, "REFLEX": 1, "LEARN": 0, "CHARISMA": 0, "INTUITION": 1},
            "maximums": {"BUILD": 6, "REFLEX": 7, "LEARN": 6, "CHARISMA": 6, "INTUITION": 7}
        },
        "Clan Pilot": {
            "modifiers": {"BUILD": -1, "REFLEX": 2, "LEARN": 0, "CHARISMA": 0, "INTUITION": 1},
            "maximums": {"BUILD": 5, "REFLEX": 8, "LEARN": 6, "CHARISMA": 6, "INTUITION": 7}
        },
        "Elemental": {
            "modifiers": {"BUILD": 1, "REFLEX": 1, "LEARN": 0, "CHARISMA": -1, "INTUITION": 0},
            "maximums": {"BUILD": 8, "REFLEX": 7, "LEARN": 6, "CHARISMA": 5, "INTUITION": 6}
        }
    }

    modifiers = {}
    modifiers = race_data[race]["modifiers"]
    maximums = race_data[race]["maximums"]

    if exceptional_attribute:
        print(f"Exceptional Attribute selected: {exceptional_attribute}. It can exceed the racial maximum by 1.")
        maximums[exceptional_attribute] += 1

    assigned_points = {attr: 0 for attr in ["BUILD", "REFLEX", "LEARN", "CHARISMA", "INTUITION"]}
    remaining_points = attributes_points - sum(assigned_points.values())

    print(f"Racial Modifiers: {modifiers}")

    # Adjusted base values with racial modifiers
    for attribute in ["BUILD", "REFLEX", "LEARN", "CHARISMA", "INTUITION"]:
        print(f"{attribute} Maximum: {maximums[attribute]} (Racial Modifier: {modifiers[attribute]})")

    while remaining_points > 0:
        for attribute in ["BUILD", "REFLEX", "LEARN", "CHARISMA", "INTUITION"]:
            current_value = assigned_points[attribute] + modifiers[attribute]
            max_value = maximums[attribute]

            # Special handling for INTUITION
            if attribute == "INTUITION":
                current_value = math.floor(assigned_points[attribute] / 2) + modifiers[attribute]
                max_value = math.floor(maximums[attribute] * 2)

            if current_value >= max_value:
                print(f"{attribute} is already at its maximum ({max_value}).")
                continue

            while True:
                try:
                    max_points_to_assign = min(remaining_points, max_value - current_value)
                    if max_points_to_assign <= 0:
                        break
                    print(f"\nRemaining Points: {remaining_points}")
                    value = int(input(f"Assign points to {attribute} (Max: {max_points_to_assign}, Current: {current_value}): "))
                    if 0 <= value <= max_points_to_assign:
                        assigned_points[attribute] += value
                        remaining_points -= value
                        break
                    else:
                        print(f"Invalid value. Must be between 0 and {max_points_to_assign}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        if remaining_points == 0:
            break

    print("\nAttribute Assignment Complete:")
    for attribute, value in assigned_points.items():
        if attribute == "INTUITION":
            final_value = current_value = math.floor(value / 2) + modifiers[attribute]
        else:
            final_value = value + modifiers[attribute]
        print(f"{attribute}: {final_value} (Base: {value}, Modifier: {modifiers[attribute]})")

    attributes = {  # Return final adjusted attributes
        attr: (math.floor(val / 2) + modifiers[attr] if attr == "INTUITION" else val + modifiers[attr])
        for attr, val in assigned_points.items()
}
    assigned_attributes = {  # Return final adjusted attributes
        attr: (math.floor(val / 2) + modifiers[attr] if attr == "INTUITION" else val + modifiers[attr])
        for attr, val in assigned_points.items()
    }

# Calculate saving throws
    saving_throws = calculate_saving_throws(attributes)

# Display saving throws
    print("\nSaving Throws:")
    for attribute, roll in saving_throws.items():
        print(f"{attribute}: {roll}")

    # Calculate characteristics
    characteristics = calculate_characteristics(assigned_attributes)

    # Display characteristics
    print("\nCharacteristics:")
    for characteristic, value in characteristics.items():
        print(f"{characteristic}: {value}")

#    return attributes, saving_throws, characteristics and modifiers
    return assigned_attributes, saving_throws, characteristics, modifiers


def calculate_saving_throws(attributes):
    """
    Calculate saving throws for each attribute.
    Saving Throw Formula: 18 - (2 * attribute_value)
    """
    saving_throws = {}
    for attribute, value in attributes.items():
        saving_throws[attribute] = 18 - (2 * value)
    return saving_throws

def calculate_characteristics(attributes):
    """
    Calculate characteristics based on the attributes.
    Formula for each characteristic:
        Athletic: 18 - (Build + Reflexes)
        Physical: 18 - (Reflexes + Intuition)
        Mental:   18 - (Intuition + Learn)
        Social:   18 - (Intuition + Charisma)
    """
    characteristics = {
        "Athletic": 18 - (attributes["BUILD"] + attributes["REFLEX"]),
        "Physical": 18 - (attributes["REFLEX"] + attributes["INTUITION"]),
        "Mental": 18 - (attributes["INTUITION"] + attributes["LEARN"]),
        "Social": 18 - (attributes["INTUITION"] + attributes["CHARISMA"]),
    }
    return characteristics

def purchase_skills(skill_points, learn_attribute, race):
    print(f"\nYou have {skill_points} skill points to purchase initial skills.")
    print(f"Note: No skill level may exceed your LEARN attribute value ({learn_attribute}).")

    # List of available skills
    skills = [
        "Acrobatics", "Administration", "Alternate Identity", "Appraisal", "Archery",
        "Blade", "Bureaucracy", "Career Skills", "Climbing", "Communications",
        "Computer", "Cryptography", "Demolitions", "Disguise", "Drive", "Engineering",
        "Escape Artist", "Forgery", "Gambling", "Gunnery", "Impersonation", "Interrogation",
        "Jump Pack", "Leadership", "Medtech", "Navigation", "Negotiation", "Perception",
        "Piloting", "Protocol", "Quickdraw", "Running", "Scrounge", "Security Systems",
        "Seduction", "Small Arms", "Special Interests", "Stealth", "Strategy",
        "Streetwise", "Support Weapons", "Survival", "Swimming", "Tactics", "Technician",
        "Throwing Weapons", "Tinker", "Tracking", "Training", "Unarmed Combat",
        "Gunnery/Mech", "Tech/Mechanic", "Tech/Electronics", "Piloting/Mech", "Gunnery/Aerospace",
        "Tech/Aerospace", "Piloting/Aerospace", "Gunnery/Battle Armor", "Tech/Battle Armor",
        "Piloting/Battle Armor", "Gunnery/Artillery", "Gunnery/Conventional", "Piloting/Vtol",
        "Gunnery/Spacecraft", "Piloting/Spacecraft", "Zero-G Operations", "Gunnery/Battlesuit",
        "Tech/Battlesuit", "Piloting/Battlesuit", "Tech/Mech", "Drive/Ground", "Tech/Electronics",
        "Tech/Spacecraft", "Piloting/Vtol", "Communications/Conventional"]

    purchased_skills = {}
    selected_package_name ={}
    eligible_packages = {}
    remaining_points = skill_points

    # Skill packages by race
    skill_packages = {
        "Clan Warrior": {
            "Primary Clan Warrior": {
                "cost": 20,
                "skills": {
                    "Gunnery/Mech": 4,
                    "Interrogation": 1,
                    "Leadership": 1,
                    "Medtech": 1,
                    "Piloting/Mech": 3,
                    "Small Arms": 2,
                    "Survival": 1,
                    "Tactics": 2,
                    "Tech/Mech": 2,
                    "Unarmed Combat": 1
                }
            },
            "Secondary Clan Warrior": {
                "cost": 12,
                "skills": {
                    "Gunnery/Mech": 3,
                    "Leadership": 1,
                    "Medtech": 2,
                    "Piloting/Mech": 2,
                    "Small Arms": 2,
                    "Survival": 1,
                    "Tactics": 1,
                    "Tech/Mech": 1,
                    "Unarmed Combat": 1
                }
            }
        },
    # Add packages for other races
    "Clan Pilot": {
        "Clan Pilot": {
            "cost": 16,
            "skills": {
                "Gunnery/Aerospace": 4,
                "Medtech": 1,
                "Piloting/Aerospace": 3,
                "Small Arms": 1,
                "Tactics": 2,
                "Tech/Aerospace": 2
            }
        }
    },
    # Add packages for other races
    "Elemental": {
        "Elemental Package": {
            "cost": 16,
            "skills": {
                "Gunnery/Battle Armor": 3,
                "Interrogation": 1,
                "Medtech": 1,
                "Piloting/Battle Armor": 3,
                "Small Arms": 2,
                "Survival": 1,
                "Tactics": 1,
                "Tech/Battlesuit": 1,
                "Unarmed Combat": 1
              }
          }
        },
        "Human": {
            "Basic Academy Package - BATTLEMECH PILOT MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Mech", "Gunnery/Mech"],
                "elective_skills": ["Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - BATTLEMECH PILOT MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Mech", "Gunnery/Mech"],
                "elective_skills": ["Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic Academy Package - AEROSPACE PILOT MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Aerospace", "Gunnery/Aerospace"],
                "elective_skills": ["Tech/Aerospace", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - AEROSPACE PILOT MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Aerospace", "Gunnery/Aerospace" ],
                "elective_skills": ["Tech/Aerospace", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - LAM PILOT MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": [ "Gunnery/Mech", "Piloting/Mech", "Gunnery/Aerospace", "Piloting/Aerospace", "Medtech", "Small Arms" ],
                "elective_skills": [ "Tech/Aerospace", "Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic Academy Package - MARINE MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Zero-G Operations", "Gunnery/Spacecraft"],
                "elective_skills": [ "Demolitions",  "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - MARINE MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Zero-G Operations", "Gunnery/Spacecraft"],
                "elective_skills": [ "Demolitions",  "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic Academy Package - ARMORED INFANTRY MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Gunnery/Battlesuit", "Piloting/Battlesuit" ],
                "elective_skills": [ "Demolitions", "Tech/Battlesuit", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"  ]
                  },
            "Basic University Package - ARMORED INFANTRY MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Gunnery/Battlesuit", "Piloting/Battlesuit" ],
                "elective_skills": [ "Demolitions", "Tech/Battlesuit", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Basic Academy Package - INFANTRY MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Unarmed Combat", "Support Weapons" ],
                "elective_skills": [ "Drive/Ground", "Gunnery/Artillery", "Bureaucracy", "Blade", "Leadership",  "Survival" ]
                  },
            "Basic University Package - INFANTRY MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 2   # 4 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Unarmed Combat", "Support Weapons" ],
                "elective_skills": [ "Drive/Ground", "Gunnery/Artillery", "Bureaucracy", "Blade", "Leadership",  "Survival" ]
                  },
            "Basic Academy Package - CAVALRY MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": ["Drive/Ground", "Piloting/Vtol", "Gunnery/Conventional", "Medtech", "Small Arms" ],
                "elective_skills": [ "Gunnery/Artillery", "Tech/Mech", "Bureaucracy", "Blade", "Leadership",  "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - CAVALRY MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Drive/Ground", "Piloting/Vtol", "Gunnery/Conventional", "Medtech", "Small Arms" ],
                "elective_skills": [ "Gunnery/Artillery", "Tech/Mech", "Bureaucracy", "Blade", "Leadership",  "Survival", "Unarmed Combat" ]
                  },
            "Basic Academy Package - DROPSHIP PILOT MOS": {
                "cost": 9,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": ["Piloting/Spacecraft", "Zero-G Operations", "Medtech", "Small Arms" ],
                "elective_skills": [ "Communications/Conventional", "Computer", "Gunnery/Spacecraft", "Bureaucracy", "Blade", "Leadership",  "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - DROPSHIP PILOT MOS": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Piloting/Spacecraft", "Zero-G Operations", "Medtech", "Small Arms" ],
                "elective_skills": [ "Communications/Conventional", "Computer", "Gunnery/Spacecraft", "Bureaucracy", "Blade", "Leadership",  "Survival", "Unarmed Combat" ]
                  },
            "Advanced Academy Package - BATTLEMECH PILOT MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Mech", "Gunnery/Mech"],
                "elective_skills": ["Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Advanced University Package - BATTLEMECH PILOT MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Mech", "Gunnery/Mech"],
                "elective_skills": ["Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
            },
            "Advanced Academy Package - AEROSPACE PILOT MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Aerospace", "Gunnery/Aerospace"],
                "elective_skills": [ "Tech/Aerospace", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"  ]
            },
            "Advanced University Package - AEROSPACE PILOT MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Piloting/Aerospace", "Gunnery/Aerospace"],
                "elective_skills": [ "Tech/Aerospace", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"  ]
                  },
            "Advanced University Package - LAM PILOT MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": [ "Gunnery/Mech", "Piloting/Mech", "Gunnery/Aerospace", "Piloting/Aerospace", "Medtech", "Small Arms"  ],
                "elective_skills": [  "Tech/Aerospace", "Tech/Mech", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
            },
            "Advanced Academy Package - MARINE MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Zero-G Operations", "Gunnery/Spacecraft"],
                "elective_skills": [ "Demolitions", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"    ]
                  },
            "Advanced University Package - MARINE MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 3   # 5 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Zero-G Operations", "Gunnery/Spacecraft"],
                "elective_skills": [ "Demolitions", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"    ]
                  },
            "Advanced Academy Package - ARMORED INFANTRY MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Gunnery/Battlesuit", "Piloting/Battlesuit"],
                "elective_skills": [ "Demolitions", "Tech/Battlesuit", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Advanced University Package - ARMORED INFANTRY MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Gunnery/Battlesuit", "Piloting/Battlesuit"],
                "elective_skills": [ "Demolitions", "Tech/Battlesuit", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Advanced Academy Package - INFANTRY MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Unarmed Combat", "Support Weapons" ],
                "elective_skills": [ "Drive/Ground", "Gunnery/Artillery", "Bureaucracy", "Blade", "Leadership", "Survival"  ]
                  },
            "Advanced University Package - INFANTRY MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 2   # 2 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms", "Unarmed Combat", "Support Weapons" ],
                "elective_skills": [ "Drive/Ground", "Gunnery/Artillery", "Bureaucracy", "Blade", "Leadership", "Survival"  ]
                  },
            "Advanced Academy Package - CAVALRY MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 5   # 5 skills at Level 0
                },
                "required_skills": [ "Drive/Ground", "Piloting/Vtol", "Gunnery/Conventional", "Medtech", "Small Arms" ],
                "elective_skills": [  "Gunnery/Artillery", "Tech/Mechanical", "Bureaucracy", "Blade", "Leadership", "Survival" ]
                  },
            "Advanced University Package - CAVALRY MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 3   # 3 skills at Level 0
                },
                "required_skills": [ "Drive/Ground", "Piloting/Vtol", "Gunnery/Conventional", "Medtech", "Small Arms" ],
                "elective_skills": [  "Gunnery/Artillery", "Tech/Mechanical", "Bureaucracy", "Blade", "Leadership", "Survival" ]
                  },
            "Advanced Academy Package - DROPSHIP PILOT MOS": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,  # 2 skills at Level 1
                    0: 6   # 6 skills at Level 0
                },
                "required_skills": [ "Piloting/Spacecraft", "Zero-G Operations", "Medtech", "Small Arms" ],
                "elective_skills": [  "Communications/Conventional", "Computer", "Gunnery/Spacecraft", "Bureaucracy", "Blade", "Leadership", "Survival", "Unarmed Combat" ]
                  },
            "Advanced University Package - DROPSHIP PILOT MOS": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 4   # 4 skills at Level 0
                },
                "required_skills": [ "Piloting/Spacecraft", "Zero-G Operations", "Medtech", "Small Arms" ],
                "elective_skills": [  "Communications/Conventional", "Computer", "Gunnery/Spacecraft", "Bureaucracy", "Blade", "Leadership", "Survival", "Unarmed Combat" ]
                  },
            "Basic University Package - DROPSHIP PILOT MOS AND JUMPSHIP PILOT FOS ": {
                "cost": 12,
                "skills_at_level": {
                    3: 0,  # 0 skills at Level 3
                    2: 4,  # 4 skills at Level 2
                    1: 4,  # 4 skills at Level 1
                    0: 7   # 7 skills at Level 0
                },
                "required_skills": ["Piloting/Spacecraft", "Zero-G Operations", "Computer", "Navigation", "Medtech", "Small Arms"  ],
                "elective_skills": [ "Communications/Conventional", "Gunnery/Spacecraft", "Strategy", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
                  },
            "Advanced University Package - DROPSHIP PILOT MOS AND JUMPSHIP PILOT FOS ": {
                "cost": 18,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 3,  # 3 skills at Level 2
                    1: 3,  # 3 skills at Level 1
                    0: 7   # 7 skills at Level 0
                },
                "required_skills": ["Piloting/Spacecraft", "Zero-G Operations", "Computer", "Navigation", "Medtech", "Small Arms"  ],
                "elective_skills": ["Communications/Conventional", "Gunnery/Spacecraft", "Strategy", "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat" ]
            },
            "Combat Academy Package": {
                "cost": 15,
                "skills_at_level": {
                    3: 2,  # 2 skills at Level 3
                    2: 2,  # 2 skills at Level 2
                    1: 2,   # 2 skills at Level 1
                    0: 2   # 2 skills at Level 0
                },
                "required_skills": ["Medtech", "Small Arms"],
                "elective_skills": [ "Bureaucracy", "Blade", "Leadership", "Support Weapons", "Survival", "Unarmed Combat"  ]
            }
    },
    "Generic": {
        "MechWarrior Package": {
            "cost": 13,
            "skills": {
                "Gunnery/Mech": 2,
                "Leadership": 1,
                "Piloting/Mech": 2,
                "Small Arms": 2,
                "Survival": 1,
                "Tech/Mech": 1,
                "Unarmed Combat": 2
                    }
        },
        "Infantry Package": {
            "cost": 15,
            "skills": {
                "Blade": 1,
                "Drive/Ground": 1,
                "Medtech": 1,
                "Quickdraw": 1,
                "Small Arms": 3,
                "Stealth": 2,
                "Support Weapons": 1,
                "Survival": 1,
                "Unarmed Combat": 2
           }
        },
        "Cavalry Package": {
    "cost": 13,
    "skills": {
    "Drive/Ground": 2,
    "Gunnery/Artillery": 1,
    "Gunnery/Conventional": 2,
    "Small Arms": 2,
    "Survival": 1,
    "Tech/Mechanical": 1,
    "Unarmed Combat": 2
       }
  },
"Guerrilla Fighter Package": {
"cost": 19,
"skills": {
"Blade": 1,
"Demolitions": 1,
"Disguise": 1,
"Impersonation": 1,
"Medtech": 1,
"Perception": 2,
"Scrounge": 1,
"Security Systems": 1,
"Small Arms": 2,
"Stealth": 2,
"Survival": 2,
"Tracking": 1,
"Unarmed Combat": 2,
            }
        }
    }
}

    selected_package_name = None
    selected_package_details = None

    race_packages = skill_packages.get(race, {})
    generic_packages = skill_packages.get("Generic", {})

    # Merge race-specific and generic packages
    all_packages = {**race_packages, **generic_packages}

    eligible_packages = {
        name: data
        for name, data in all_packages.items()
        if data["cost"] <= skill_points and (
        # Check for fixed-skill packages
            ("skills" in data and all(level <= learn_attribute for level in data["skills"].values())) or
        # Check for flexible-skill packages
            ("skills_at_level" in data and all(
            level <= learn_attribute or count == 0  # Allow levels with a count of 0
            for level, count in data["skills_at_level"].items()

        ))
    )
}


    if not eligible_packages:
       insufficient_points = any(data["cost"] > skill_points for data in all_packages.values())
       low_learn_attribute = any("skills" in data and any(level > learn_attribute for level in data["skills"].values()) for data in all_packages.values())

       if insufficient_points and low_learn_attribute:
           print("No skill packages are available due to both insufficient skill points and a low LEARN attribute.")
       elif insufficient_points:
           print("No skill packages are available due to insufficient skill points.")
       elif low_learn_attribute:
           print("No skill packages are available due to a low LEARN attribute.")
       else:
           print("No skill packages are available for your character.")
           # Skip package selection if no packages are eligible
           print("Skipping package selection.")

    #else:
    if eligible_packages:
        print("\nAvailable Skill Packages:")
    for i, (package_name, package_data) in enumerate(eligible_packages.items(), start=1):
        print(f"{i}. {package_name} (Cost: {package_data['cost']} Skill Points)")
        if "skills" in package_data:  # Fixed-skill package
            for skill, level in package_data["skills"].items():
                print(f"   - {skill}: Level {level}")
        else:  # Flexible-skill package
            for level, count in package_data["skills_at_level"].items():
                if count > 0 and level > 0:
                    print(f"   - {count} skills at Level {level}")
            print("   Required Skills:", ", ".join(package_data["required_skills"]))
            print("   Elective Skills:", ", ".join(package_data["elective_skills"]))

    while True:
        try:
            choice = input("\nWould you like to purchase a skill package? Enter the package number or 'n' to skip: ").lower()
            if choice == 'n':
                break

            package_index = int(choice) - 1
            if package_index < 0 or package_index >= len(eligible_packages):
                print("Invalid choice. Please select a valid package number.")
                continue

            selected_package_name = list(eligible_packages.keys())[package_index]
            selected_package = eligible_packages[selected_package_name]
            package_cost = selected_package["cost"]

            if package_cost > skill_points:
                print("Not enough skill points to purchase this package.")
                continue

            if "skills" in selected_package:  # Fixed-skill package
                print(f"You have purchased the {selected_package_name} package!")
                purchased_skills.update(selected_package["skills"])
            else:  # Flexible-skill package
                print(f"You have selected the {selected_package_name} package!")
                required_skills = selected_package["required_skills"]
                elective_skills = selected_package["elective_skills"]
                skills_to_select = selected_package["skills_at_level"].copy()

                # Assign all skills manually
                print("\nYou need to assign all skills manually, including required skills.")

                # Assign required skills
                for skill in required_skills:
                    print(f"\nRequired Skill: {skill}")
                    print("Remaining skill slots:", skills_to_select)

                    while True:
                        try:
                            level = int(input(f"Choose a level for {skill} ({list(skills_to_select.keys())}): "))
                            if level in skills_to_select and skills_to_select[level] > 0:
                                purchased_skills[skill] = level
                                skills_to_select[level] -= 1
                                break
                            else:
                                print("Invalid level or no slots available for this level.")
                        except ValueError:
                            print("Invalid input. Please enter a valid level.")

                # Assign elective skills
                for skill in elective_skills:
                    print(f"\nelective_skills: {skill}")
                    print("Remaining skill slots:", skills_to_select)
                    while True:
                        try:
                            level = int(input(f"Choose a level for {skill} ({list(skills_to_select.keys())}): "))
                            if level in skills_to_select and skills_to_select[level] > 0:
                                purchased_skills[skill] = level
                                skills_to_select[level] -= 1
                                break
                            else:
                                print("Invalid level or no slots available for this level.")
                        except ValueError:
                            print("Invalid input. Please enter a valid level.")

            skill_points -= package_cost
            remaining_points = skill_points
            break

        except ValueError:
            print("Invalid input. Please enter a valid number or 'n' to skip.")

# continue spending skill points after package slection.
    while remaining_points > 0:
        print(f"\nRemaining Skill Points: {remaining_points}")
        print("\nAvailable Skills:")
        for i, skill in enumerate(skills, start=1):
            current_level = purchased_skills.get(skill, 0)
            print(f"{i}. {skill} (Current Level: {current_level})")

        try:
            # Select a skill
            choice = int(input("Enter the number of the skill you want to purchase: ")) - 1
            if choice < 0 or choice >= len(skills):
                print("Invalid choice. Please select a valid skill number.")
                continue

            selected_skill = skills[choice]
            current_level = purchased_skills.get(selected_skill, 0)

            # Calculate the cost for the next level
            next_level = current_level + 1
            if next_level > learn_attribute:
                print(f"You cannot raise {selected_skill} above your LEARN attribute value ({learn_attribute}).")
                continue

            next_level_cost = next_level
            if next_level_cost > skill_points:
                print(f"Not enough points to raise {selected_skill} to level {next_level} (Cost: {next_level_cost}).")
                continue

            # Confirm purchase
            confirm = input(f"Spend {next_level_cost} points to raise {selected_skill} to level {next_level}? (y/n): ").lower()
            if confirm == 'y':
                purchased_skills[selected_skill] = next_level
                skill_points -= next_level_cost
                remaining_points = skill_points

                print(f"{selected_skill} raised to level {next_level}.")
            else:
                print("Purchase canceled.")

        except ValueError:
            print("Invalid input. Please enter a number.")

        print("\nSkill Purchase Complete:")
        if selected_package_name:
            print("\nSelected Skill Package:")
            print(f" {selected_package_name}")      
#        print("\nSkill Purchase Complete:")      
#        for skill, level in purchased_skills.items():
#            if level > 0:  # Only include skills with levels greater than 0
#                print(f"{skill}: Level {level}")
#            if selected_package_name:
#                print("\nSelected Skill Package:")
#                print(f" {selected_package_name}")


    return purchased_skills

def display_attribute_report(assigned_points, modifiers):
    """
    Generate and display the Attribute Assignment report.
    """
    print("\nAttribute Assignment Report:")
    for attribute, base_value in assigned_points.items():
        if attribute == "INTUITION":
            final_value = math.floor(base_value ) 
        else:
            final_value = base_value 
        print(f"{attribute}: {final_value} ")

def calculate_skill_targets(assigned_attributes, purchased_skills):
    """
    Calculate the skill targets based on the character's assigned attributes and skills.

    :param assigned_attributes: Dictionary of assigned attributes (e.g., {'BUILD': 8, 'REFLEX': 7, ...})
    :param skills: Dictionary of skills with their skill levels (e.g., {'Acrobatics': 3, 'Administration': 2, ...})

    :return: Dictionary of skill targets (e.g., {'Acrobatics': 5, 'Administration': 4, ...})
    """
    # Define the Master Skill List (mapping skills to characteristics)
    master_skill_list = { "Acrobatics":"Athletic",
"Administration":"Mental",
"Alternate Identity":"Mental",
"Appraisal":"Mental",
"Archery":"Athletic",
"Blade":"Athletic",
"Bureaucracy":"Social",
"Career Skills":"Mental",
"Climbing":"Athletic",
"Communications":"Mental",
"Communications/Conventional":"Mental",
"Computer":"Mental",
"Cryptography":"Mental",
"Demolitions":"Mental",
"Disguise":"Mental",
"Drive":"Physical",
"Drive/Ground":"Physical",
"Engineering":"Mental",
"Escape Artist":"Physical",
"Forgery":"Mental",
"Gambling":"Mental",
"Gunnery":"Physical",
"Gunnery/Aerospace":"Physical",
"Gunnery/Artillery":"Physical",
"Gunnery/Conventional":"Physical",
"Gunnery/Battle Armor":"Physical",
"Gunnery/Battlesuit":"Physical",
"Gunnery/Mech":"Physical",
"Gunnery/Spacecraft":"Physical",
"Impersonation":"Social",
"Interrogation":"Social",
"Jump Pack":"Athletic",
"Leadership":"Social",
"Medtech":"Mental",
"Navigation":"Mental",
"Negotiation":"Social",
"Perception":"Mental",
"Piloting":"Physical",
"Piloting/Aerospace":"Physical",
"Piloting/Battle Armor":"Physical",
"Piloting/Battlesuit":"Physical",
"Piloting/Mech":"Physical",
"Piloting/Vtol":"Physical",
"Piloting/Spacecraft":"Physical",
"Protocol":"Social",
"Quickdraw":"Physical",
"Running":"Athletic",
"Scrounge":"Social",
"Security Systems":"Mental",
"Seduction":"Social",
"Small Arms":"Physical",
"Special Interests":"Mental",
"Stealth":"Physical",
"Strategy":"Mental",
"Streetwise":"Social",
"Support Weapons":"Physical",
"Survival":"Mental",
"Swimming":"Athletic",
"Tactics":"Mental",
"Technician":"Mental",
"Tech/Aerospace":"Mental",
"Tech/Battle Armor":"Mental",
"Tech/Battlesuit":"Mental",
"Tech/Electronics":"Mental",
"Tech/Mech":"Mental",
"Tech/Mechanicical":"Mental",
"Tech/Spacecraft":"Mental",
"Throwing Weapons":"Physical",
"Tinker":"Mental",
"Tracking":"Mental",
"Training":"Social",
"Unarmed Combat":"Athletic",
"Zero-G Operations":"Physical"
 }

    skill_targets = {}
    skills = {}

    # Iterate over each skill the character possesses
    for skill, skill_level in purchased_skills.items():
        if skill_level > 0:
            if skill in master_skill_list:
            # Find the characteristic corresponding to the skill
                characteristic = master_skill_list[skill]
            # Calculate the base skill target: Characteristic value - Skill level
                if characteristic in assigned_attributes:
                    characteristic_value = assigned_attributes[characteristic]
                    skill_target = characteristic_value - skill_level
                    skill_targets[skill] = skill_target
                else:
                    print(f"Error: Missing characteristic value for {characteristic} for skill {skill}.")
            else:
                print(f"Error: {skill} is not in the master skill list.")

    return skill_targets

def display_skill_targets(skill_targets):
    """Display the skill targets in a readable format."""
    print("\nSkill Targets:")
    for skill, target in skill_targets.items():
#        if target >= 0:  # Skip skills with a level of 0
        print(f"{skill}: {target}")

def main():
    print("To begin character construction, the player must assign a Priority Level from 0 to 4 to each of the five categories listed on the Master Character Table.")
    print("All five Priority Levels (0, 1, 2, 3, and 4) must be assigned.")

    # Categories for the RPG character
    categories = ["Race", "Attributes", "Skills", "Advantages", "Vehicle Class"]

    # Predefined values for each priority level per category
    priority_values = {
        "Race": {
            0: "Human",
            1: "Human",
            2: "Clan Warrior",
            3: "Clan Pilot",
            4: "Elemental"
        },
        "Attributes": {
            0: 18,
            1: 21,
            2: 24,
            3: 27,
            4: 30
        },
        "Skills": {
            0: 8,
            1: 12,
            2: 16,
            3: 20,
            4: 24
        },
        "Advantages": {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4
        },
        "Vehicle Class": {
            0: "None",
            1: "Light",
            2: "Medium",
            3: "Heavy",
            4: "Assault"
        }
    }


    # Get assigned priorities from the user
    assigned_priorities = get_unique_priorities(categories, priority_values)

    print("\nCharacter Priority Assignment Complete:")
    for category, priority in assigned_priorities.items():
        # Use priority_values to map the priority to the specific value
        value = priority_values[category][priority]
        print(f"{category}: Priority {priority} ({value})")

    # Get race and attributes points from assigned priorities
    race = priority_values["Race"][assigned_priorities["Race"]]
    attributes_points = priority_values["Attributes"][assigned_priorities["Attributes"]]

    # Get advantage points from assigned priorities
    advantage_points = priority_values["Advantages"][assigned_priorities["Advantages"]]

    # Spend advantage points and get exceptional attribute (if any)
    purchased_advantages, exceptional_attribute = spend_advantage_points(advantage_points, race)

    #Spend Advantage Points
    assigned_attributes, saving_throws, characteristics, modifiers   = assign_attribute_points(attributes_points, race, exceptional_attribute)
    characteristics = calculate_characteristics(assigned_attributes)

    # Get the LEARN attribute value
    learn_attribute = assigned_attributes["LEARN"]

    # Skill purchasing
    skill_points = priority_values["Skills"][assigned_priorities["Skills"]]
    purchased_skills = purchase_skills(skill_points, learn_attribute, race)
    print("\nCharacter Creation Summary:")
    print("\nSkill Purchase Complete:")
    for skill, level in purchased_skills.items():
        if level > 0:  # Only include skills with levels greater than 0
            print(f"{skill}: Level {level}")
            # Include the selected package in the final report

    # Display saving throws
    print("\nSaving Throws:")
    for attribute, roll in saving_throws.items():
        print(f"{attribute}: {roll}")

    # Display characteristics
    print("\nCharacteristics:")
    for characteristic, value in characteristics.items():
        print(f"{characteristic}: {value}")

    # Calculate the skill targets
    skill_targets = calculate_skill_targets(characteristics, purchased_skills)

    # Display the calculated skill targets
    display_skill_targets(skill_targets)

    #final reports
    print("\nCharacter Priority Assignment Complete:")
    for category, priority in assigned_priorities.items():
        #Use priority_values to map the priority to the specific value
        value = priority_values[category][priority]
        print(f"{category}: Priority {priority} ({value})")

    display_attribute_report(assigned_attributes, modifiers)

    # more reports
    print("\nAdvantage Purchase Complete:")
    for advantage, cost in purchased_advantages.items():
        print(f"{advantage}: {cost} points")

    print("\n--- Final Report ---")

if __name__ == "__main__":
    main()
