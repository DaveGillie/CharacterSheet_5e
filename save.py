from tkinter import messagebox
import json

key_strength = 'strength'
key_dexterity = 'dexterity'
key_constitution = 'constitution'
key_intelligence = 'intelligence'
key_wisdom = 'wisdom'
key_charisma = 'charisma'

key_modifier = 'modifier'
key_value = 'value'

key_saving_throws = 'saving_throws'
key_proficient = 'proficient'
key_bonus = 'bonus'
key_modifiers = 'modifiers'

key_initiative = 'initiative'
key_armor_class = 'armor_class'
key_proficiency = 'proficiency'
key_inspiration = 'inspiration'
key_proficiencies = 'proficiencies'

key_skills = 'skills'
key_acrobatics = 'acrobatics'
key_animal_handling = 'animal_handling'
key_arcana = 'arcana'
key_athletics = 'athletics'
key_decption = 'deception'
key_history = 'history'
key_insight = 'insight'
key_intimidation = 'intimidation'
key_investigation = 'investigation'
key_medicine = 'medicine'
key_nature = 'nature'
key_perception = 'perception'
key_performance = 'performance'
key_persuasion = 'persuasion'
key_religion = 'religion'
key_sleight_of_hand = 'sleight_of_hand'
key_stealth = 'stealth'
key_survival = 'survival'

key_max_hp = 'max_hp'
key_temp_hp = 'temp_hp'
key_current_hp = 'current_hp'
key_hit_dice = 'hit_dice'

key_success_1 = 'success_1'
key_success_2 = 'success_2'
key_success_3 = 'success_3'
key_failure_1 = 'failure_1'
key_failure_2 = 'failure_2'
key_failure_3 = 'failure_3'

key_feat_trait = 'feat_trait'

key_items = 'items'
key_name = 'name'
key_description = 'description'

key_copper = 'copper'
key_silver = 'silver'
key_gold = 'gold'

key_journal = 'journal'
key_title = 'title'
key_note = 'note'


def save(data):
    '''Expect data to be a dictionary with specific structure'''
    write = {
        key_strength: {
            key_modifier: data[key_strength][key_modifier].get(),
            key_value: data[key_strength][key_value].get()
        },
        key_dexterity: {
            key_modifier: data[key_dexterity][key_modifier].get(),
            key_value: data[key_dexterity][key_value].get()
        },
        key_constitution: {
            key_modifier: data[key_constitution][key_modifier].get(),
            key_value: data[key_constitution][key_value].get()
        },
        key_intelligence: {
            key_modifier: data[key_intelligence][key_modifier].get(),
            key_value: data[key_intelligence][key_value].get()
        },
        key_wisdom: {
            key_modifier: data[key_wisdom][key_modifier].get(),
            key_value: data[key_wisdom][key_value].get()
        },
        key_charisma: {
            key_modifier: data[key_charisma][key_modifier].get(),
            key_value: data[key_charisma][key_value].get()
        },
        key_saving_throws: {
            key_strength: {
                key_proficient: data[key_saving_throws][key_strength][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_strength][key_bonus].get()
            },
            key_dexterity: {
                key_proficient: data[key_saving_throws][key_dexterity][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_dexterity][key_bonus].get()
            },
            key_constitution: {
                key_proficient: data[key_saving_throws][key_constitution][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_constitution][key_bonus].get()
            },
            key_intelligence: {
                key_proficient: data[key_saving_throws][key_intelligence][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_intelligence][key_bonus].get()
            },
            key_wisdom: {
                key_proficient: data[key_saving_throws][key_wisdom][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_wisdom][key_bonus].get()
            },
            key_charisma: {
                key_proficient: data[key_saving_throws][key_charisma][key_proficient].get(),
                key_bonus: data[key_saving_throws][key_charisma][key_bonus].get()
            },
            key_modifiers: data[key_saving_throws][key_modifiers].get('0.0','end-1c')
        },
        key_initiative: data[key_initiative].get(),
        key_armor_class: data[key_armor_class].get(),
        key_proficiency: data[key_proficiency].get(),
        key_inspiration: data[key_inspiration].get(),
        key_proficiencies: data[key_proficiencies].get('0.0','end-1c'),
        key_skills: {
            key_acrobatics: {
                key_proficient: data[key_skills][key_acrobatics][key_proficient].get(),
                key_bonus: data[key_skills][key_acrobatics][key_bonus].get()
            },
            key_animal_handling: {
                key_proficient: data[key_skills][key_animal_handling][key_proficient].get(),
                key_bonus: data[key_skills][key_animal_handling][key_bonus].get()
            },
            key_arcana: {
                key_proficient: data[key_skills][key_arcana][key_proficient].get(),
                key_bonus: data[key_skills][key_arcana][key_bonus].get()
            },
            key_athletics: {
                key_proficient: data[key_skills][key_athletics][key_proficient].get(),
                key_bonus: data[key_skills][key_athletics][key_bonus].get()
            },
            key_decption: {
                key_proficient: data[key_skills][key_decption][key_proficient].get(),
                key_bonus: data[key_skills][key_decption][key_bonus].get()
            },
            key_history: {
                key_proficient: data[key_skills][key_history][key_proficient].get(),
                key_bonus: data[key_skills][key_history][key_bonus].get()
            },
            key_insight: {
                key_proficient: data[key_skills][key_insight][key_proficient].get(),
                key_bonus: data[key_skills][key_insight][key_bonus].get()
            },
            key_intimidation: {
                key_proficient: data[key_skills][key_intimidation][key_proficient].get(),
                key_bonus: data[key_skills][key_intimidation][key_bonus].get()
            },
            key_investigation: {
                key_proficient: data[key_skills][key_investigation][key_proficient].get(),
                key_bonus: data[key_skills][key_investigation][key_bonus].get()
            },
            key_medicine: {
                key_proficient: data[key_skills][key_medicine][key_proficient].get(),
                key_bonus: data[key_skills][key_medicine][key_bonus].get()
            },
            key_nature: {
                key_proficient: data[key_skills][key_nature][key_proficient].get(),
                key_bonus: data[key_skills][key_nature][key_bonus].get()
            },
            key_perception: {
                key_proficient: data[key_skills][key_perception][key_proficient].get(),
                key_bonus: data[key_skills][key_perception][key_bonus].get()
            },
            key_performance: {
                key_proficient: data[key_skills][key_performance][key_proficient].get(),
                key_bonus: data[key_skills][key_performance][key_bonus].get()
            },
            key_persuasion: {
                key_proficient: data[key_skills][key_persuasion][key_proficient].get(),
                key_bonus: data[key_skills][key_persuasion][key_bonus].get()
            },
            key_religion: {
                key_proficient: data[key_skills][key_religion][key_proficient].get(),
                key_bonus: data[key_skills][key_religion][key_bonus].get()
            },
            key_sleight_of_hand: {
                key_proficient: data[key_skills][key_sleight_of_hand][key_proficient].get(),
                key_bonus: data[key_skills][key_sleight_of_hand][key_bonus].get()
            },
            key_stealth: {
                key_proficient: data[key_skills][key_stealth][key_proficient].get(),
                key_bonus: data[key_skills][key_stealth][key_bonus].get()
            },
            key_survival: {
                key_proficient: data[key_skills][key_survival][key_proficient].get(),
                key_bonus: data[key_skills][key_survival][key_bonus].get()
            }
        },
        key_max_hp: data[key_max_hp].get(),
        key_temp_hp: data[key_temp_hp].get(),
        key_current_hp: data[key_current_hp].get(),
        key_hit_dice: data[key_hit_dice].get(),
        key_success_1: data[key_success_1].get(),
        key_success_2: data[key_success_2].get(),
        key_success_3: data[key_success_3].get(),
        key_failure_1: data[key_failure_1].get(),
        key_failure_2: data[key_failure_2].get(),
        key_failure_3: data[key_failure_3].get(),
        key_feat_trait: data[key_feat_trait].get('0.0','end-1c'),
        key_items: [],
        key_copper: data[key_copper].get(),
        key_silver: data[key_silver].get(),
        key_gold: data[key_gold].get(),
        key_journal: []
    }

    #POPULATE THE ITEMS
    if data.get(key_items) != None:
        for entry in data[key_items]:
            write[key_items].append({
                key_name: entry.var_name.get(),
                key_description: entry.description.get('0.0','end-1c')
            })

    #POPULATE THE JOURNAL
    if data.get(key_journal) != None:
        for entry in data[key_journal]:
            write[key_journal].append({
                key_title: entry.var_title.get(),
                key_note: entry.note.get('0.0','end-1c')
            })

    with open('data.json', 'w') as f:
        f.write(json.dumps(write, indent='    '))

    messagebox.showinfo(None, message='Saved')