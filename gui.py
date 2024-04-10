import tkinter as tk
import customtkinter as ctk
from save import *
import os


class AttributeFrame(ctk.CTkFrame):
    def __init__(self, parent, name, **kwargs):
        super().__init__(parent, **kwargs)
        frame = ctk.CTkFrame(self)
        
        attribute_name = ctk.CTkLabel(frame, text=name)
        attribute_name.place(relx=.56, rely=0, relheight=.2, anchor='n')

        #label and entry for the modifier
        mod_label = ctk.CTkLabel(frame, text='modifier')
        mod_label.place(relx=.4, rely=.2, relheight=.4, anchor='ne')
        self.var_modifier = tk.StringVar()
        mod_entry = ctk.CTkEntry(frame, justify='center', textvariable=self.var_modifier)
        mod_entry.place(relx=.56, rely=.2, relheight=.4, relwidth=.25, anchor='n')

        #label and entry for the value
        val_label = ctk.CTkLabel(frame, text='value')
        val_label.place(relx=.4, rely=.6, relheight=.4, anchor='ne')
        self.var_value = tk.StringVar()
        val_entry = ctk.CTkEntry(frame, justify='center', textvariable=self.var_value)
        val_entry.place(relx=.56, rely=.6, relheight=.4, relwidth=.25, anchor='n')
        frame.pack(padx=10, pady=10)


class BonusProfFrame(ctk.CTkFrame):
    def __init__(self, parent, name, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.var_bonus = tk.StringVar()
        bonus_entry = ctk.CTkEntry(self, width=40, justify='center', textvariable=self.var_bonus)
        bonus_entry.pack(side='left')

        self.var_prof = tk.BooleanVar()
        prof_box = ctk.CTkCheckBox(self, text=name, variable=self.var_prof)
        prof_box.pack(side='left', padx=10)


class LeftRightFrame(ctk.CTkFrame):
    def __init__(self, parent, left, right, **kwargs):
        super().__init__(parent, **kwargs)

        #initiative stuff
        left_frame = ctk.CTkFrame(self)
        left_label = ctk.CTkLabel(left_frame, text=left)
        left_label.place(rely=.1, relheight=.2, relwidth=1)
        self.var_left = tk.StringVar()
        left_entry = ctk.CTkEntry(left_frame, textvariable=self.var_left, justify='center')
        left_entry.place(relx=.25, rely=.4, relheight=.4, relwidth=.5)
        left_frame.place(relx=0, relheight=1, relwidth=.5)

        #armor stuff
        right_frame = ctk.CTkFrame(self)
        right_label = ctk.CTkLabel(right_frame, text=right)
        right_label.place(rely=.1, relheight=.2, relwidth=1)
        self.var_right = tk.StringVar()
        right_entry = ctk.CTkEntry(right_frame, textvariable=self.var_right, justify='center')
        right_entry.place(relx=.25, rely=.4, relheight=.4, relwidth=.5)
        right_frame.place(relx=.5, relheight=1, relwidth=.5)


class TextFrame(ctk.CTkFrame):
    def __init__(self, parent, label, **kwargs):
        super().__init__(parent, **kwargs)
        l = ctk.CTkLabel(self, text=label)
        l.pack()
        self.text = ctk.CTkTextbox(self)
        self.text.pack(expand=True, fill='both')


class SavingThrowsFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        label = ctk.CTkLabel(self, text="SAVING THROWS")
        label.place(rely=0, relheight=.1, relwidth=1)
        self.strength = BonusProfFrame(self, 'Strength')
        self.strength.place(rely=.1, relheight=.1, relwidth=1)
        self.dexterity = BonusProfFrame(self, 'Dexterity')
        self.dexterity.place(rely=.2, relheight=.1, relwidth=1)
        self.constitution = BonusProfFrame(self, 'Constitution')
        self.constitution.place(rely=.3, relheight=.1, relwidth=1)
        self.intelligence = BonusProfFrame(self, 'Intelligence')
        self.intelligence.place(rely=.4, relheight=.1, relwidth=1)
        self.wisdom = BonusProfFrame(self, 'Wisdom')
        self.wisdom.place(rely=.5, relheight=.1, relwidth=1)
        self.charisma = BonusProfFrame(self, 'Charisma')
        self.charisma.place(rely=.6, relheight=.1, relwidth=1)
        self.modifiers = ctk.CTkTextbox(self)
        self.modifiers.place(rely=.7, relheight=.3, relwidth=1)


class SkillsFrame(ctk.CTkFrame):
    '''18 skills, 19 rows (1 for label). Use 20 rows for simplicty.'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        label = ctk.CTkLabel(self, text="SKILLS")
        label.place(rely=0, relheight=.05, relwidth=1)
        self.acrobatics = BonusProfFrame(self, 'Acrobatics (DEX)')
        self.acrobatics.place(rely=.05, relheight=.05, relwidth=1)
        self.animal_handling = BonusProfFrame(self, 'Animal Handling (WIS)')
        self.animal_handling.place(rely=.10, relheight=.05, relwidth=1)
        self.arcana = BonusProfFrame(self, 'Arcana (INT)')
        self.arcana.place(rely=.15, relheight=.05, relwidth=1)
        self.athletics = BonusProfFrame(self, 'Athletics (STR)')
        self.athletics.place(rely=.20, relheight=.05, relwidth=1)
        self.deception = BonusProfFrame(self, 'Deception (CHA)')
        self.deception.place(rely=.25, relheight=.05, relwidth=1)
        self.history = BonusProfFrame(self, 'History (INT)')
        self.history.place(rely=.30, relheight=.05, relwidth=1)
        self.insight = BonusProfFrame(self, 'Insight (WIS)')
        self.insight.place(rely=.35, relheight=.05, relwidth=1)
        self.intimidation = BonusProfFrame(self, 'Intimidation (CHA)')
        self.intimidation.place(rely=.40, relheight=.05, relwidth=1)
        self.investigation = BonusProfFrame(self, 'Investigation (INT)')
        self.investigation.place(rely=.45, relheight=.05, relwidth=1)
        self.medicine = BonusProfFrame(self, 'Medicine (WIS)')
        self.medicine.place(rely=.50, relheight=.05, relwidth=1)
        self.nature = BonusProfFrame(self, 'Nature (INT)')
        self.nature.place(rely=.55, relheight=.05, relwidth=1)
        self.perception = BonusProfFrame(self, 'Perception (WIS)')
        self.perception.place(rely=.60, relheight=.05, relwidth=1)
        self.performance = BonusProfFrame(self, 'Performance (CHA)')
        self.performance.place(rely=.65, relheight=.05, relwidth=1)
        self.persuasion = BonusProfFrame(self, 'Persuasion (CHA)')
        self.persuasion.place(rely=.70, relheight=.05, relwidth=1)
        self.religion = BonusProfFrame(self, 'Religion (INT)')
        self.religion.place(rely=.75, relheight=.05, relwidth=1)
        self.sleight_of_hand = BonusProfFrame(self, 'Sleight of Hand (DEX)')
        self.sleight_of_hand.place(rely=.80, relheight=.05, relwidth=1)
        self.stealth = BonusProfFrame(self, 'Stealth (DEX)')
        self.stealth.place(rely=.85, relheight=.05, relwidth=1)
        self.survival = BonusProfFrame(self, 'Survival (WIS)')
        self.survival.place(rely=.90, relheight=.05, relwidth=1)


class DeathSavesFrame(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        death_saves = ctk.CTkLabel(self, text='DEATH SAVES')
        death_saves.place(rely=.05, relx=.5, anchor='n')

        #success stuff
        success_label = ctk.CTkLabel(self, text='SUCCESSES')
        success_label.place(rely=.3, relx=0, relwidth=.4)
        self.success_1 = tk.BooleanVar()
        s1 = ctk.CTkCheckBox(self, text='', variable=self.success_1)
        s1.place(rely=.3, relx=.45, relwidth=.2)
        self.success_2 = tk.BooleanVar()
        s2 = ctk.CTkCheckBox(self, text='', variable=self.success_2)
        s2.place(rely=.3, relx=.65, relwidth=.2)
        self.success_3 = tk.BooleanVar()
        s3 = ctk.CTkCheckBox(self, text='', variable=self.success_3)
        s3.place(rely=.3, relx=.85, relwidth=.2)

        #failure stuff
        failure_label = ctk.CTkLabel(self, text='FAILURES')
        failure_label.place(rely=.6, relx=0, relwidth=.4)
        self.failure_1 = tk.BooleanVar()
        f1 = ctk.CTkCheckBox(self, text='', variable=self.failure_1)
        f1.place(rely=.6, relx=.45, relwidth=.2)
        self.failure_2 = tk.BooleanVar()
        f2 = ctk.CTkCheckBox(self, text='', variable=self.failure_2)
        f2.place(rely=.6, relx=.65, relwidth=.2)
        self.failure_3 = tk.BooleanVar()
        f3 = ctk.CTkCheckBox(self, text='', variable=self.failure_3)
        f3.place(rely=.6, relx=.85, relwidth=.2)


class SheetTabs(ctk.CTkTabview):
    '''THIS IS WHERE THE MAGIC HAPPENS'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        data = {}

        #################
        #The Stats tab
        #################
        self.add("Stats")
        tab_stats = self.tab("Stats")
        #prepare the grid
        tab_stats.rowconfigure((0,1,2,3,4,5), weight=1, uniform='rows')
        offset = 10
        tab_stats.columnconfigure(0, weight=1+offset, uniform='1')
        tab_stats.columnconfigure(1, weight=3+offset, uniform='1')
        tab_stats.columnconfigure(2, weight=2+offset, uniform='1')
        tab_stats.columnconfigure(3, weight=2+offset, uniform='1')

        #main attributes
        strength = AttributeFrame(tab_stats, name='STRENGTH')
        strength.grid(row=0, column=0)
        data[key_strength] = {
            key_modifier: strength.var_modifier,
            key_value: strength.var_value
        }
        dexterity = AttributeFrame(tab_stats, name="DEXTERITY")
        dexterity.grid(row=1, column=0)
        data[key_dexterity] = {
            key_modifier: dexterity.var_modifier,
            key_value: dexterity.var_value
        }
        constitution = AttributeFrame(tab_stats, name='CONSTITUTION')
        constitution.grid(row=2, column=0)
        data[key_constitution] = {
            key_modifier: constitution.var_modifier,
            key_value: constitution.var_value
        }
        intelligence = AttributeFrame(tab_stats, name='INTELLIGENCE')
        intelligence.grid(row=3, column=0)
        data[key_intelligence] = {
            key_modifier: intelligence.var_modifier,
            key_value: intelligence.var_value
        }
        wisdom = AttributeFrame(tab_stats, name='WISDOM')
        wisdom.grid(row=4, column=0)
        data[key_wisdom] = {
            key_modifier: wisdom.var_modifier,
            key_value: wisdom.var_value
        }
        charisma = AttributeFrame(tab_stats, name='CHARISMA')
        charisma.grid(row=5, column=0)
        data[key_charisma] = {
            key_modifier: charisma.var_modifier,
            key_value: charisma.var_value
        }

        #initiative armor
        init_ac = LeftRightFrame(tab_stats, left='INITIATIVE', right='ARMOR CLASS')
        init_ac.grid(row=0, column=2, sticky='nsew', pady='10')
        data[key_initiative] = init_ac.var_left
        data[key_armor_class] = init_ac.var_right

        #proficienty bonus and inspiration
        prof_insp = LeftRightFrame(tab_stats, left='PROFICIENCY', right='INSPIRATION')
        prof_insp.grid(row=1, column=2, sticky='nsew', pady='10')
        data[key_proficiency] = prof_insp.var_left
        data[key_inspiration] = prof_insp.var_right

        #misc proficiencies
        misc_prof = TextFrame(tab_stats, 'STUFF & LANGUAGES')
        misc_prof.grid(row=2, column=2, sticky='nsew')
        data[key_proficiencies] = misc_prof.text

        #saving throws
        saving_throws = SavingThrowsFrame(tab_stats)
        saving_throws.grid(row=3, column=2, rowspan=3, sticky='nsew')
        data[key_saving_throws] = {
            key_strength: {
                key_proficient: saving_throws.strength.var_prof,
                key_bonus: saving_throws.strength.var_bonus
            },
            key_dexterity: {
                key_proficient: saving_throws.dexterity.var_prof,
                key_bonus: saving_throws.dexterity.var_bonus
            },
            key_constitution: {
                key_proficient: saving_throws.constitution.var_prof,
                key_bonus: saving_throws.constitution.var_bonus
            },
            key_intelligence: {
                key_proficient: saving_throws.intelligence.var_prof,
                key_bonus: saving_throws.intelligence.var_bonus
            },
            key_wisdom: {
                key_proficient: saving_throws.wisdom.var_prof,
                key_bonus: saving_throws.wisdom.var_bonus
            },
            key_charisma: {
                key_proficient: saving_throws.charisma.var_prof,
                key_bonus: saving_throws.charisma.var_bonus
            },
            key_modifiers: saving_throws.modifiers
        }

        #skills
        skills = SkillsFrame(tab_stats)
        skills.grid(row=0, column=1, rowspan=6, sticky='nsew')
        data[key_skills] = {
            key_acrobatics: {
                key_proficient: skills.acrobatics.var_prof,
                key_bonus: skills.acrobatics.var_bonus
            },
            key_animal_handling: {
                key_proficient: skills.animal_handling.var_prof,
                key_bonus: skills.animal_handling.var_bonus
            },
            key_arcana: {
                key_proficient: skills.arcana.var_prof,
                key_bonus: skills.arcana.var_bonus
            },
            key_athletics: {
                key_proficient: skills.athletics.var_prof,
                key_bonus: skills.athletics.var_bonus
            },
            key_decption: {
                key_proficient: skills.deception.var_prof,
                key_bonus: skills.deception.var_bonus
            },
            key_history: {
                key_proficient: skills.history.var_prof,
                key_bonus: skills.history.var_bonus
            },
            key_insight: {
                key_proficient: skills.insight.var_prof,
                key_bonus: skills.insight.var_bonus
            },
            key_intimidation: {
                key_proficient: skills.intimidation.var_prof,
                key_bonus: skills.intimidation.var_bonus
            },
            key_investigation: {
                key_proficient: skills.investigation.var_prof,
                key_bonus: skills.investigation.var_bonus
            },
            key_medicine: {
                key_proficient: skills.medicine.var_prof,
                key_bonus: skills.medicine.var_bonus
            },
            key_nature: {
                key_proficient: skills.nature.var_prof,
                key_bonus: skills.nature.var_bonus
            },
            key_perception: {
                key_proficient: skills.perception.var_prof,
                key_bonus: skills.perception.var_bonus
            },
            key_performance: {
                key_proficient: skills.performance.var_prof,
                key_bonus: skills.performance.var_bonus
            },
            key_persuasion: {
                key_proficient: skills.persuasion.var_prof,
                key_bonus: skills.persuasion.var_bonus
            },
            key_religion: {
                key_proficient: skills.religion.var_prof,
                key_bonus: skills.religion.var_bonus
            },
            key_sleight_of_hand: {
                key_proficient: skills.sleight_of_hand.var_prof,
                key_bonus: skills.sleight_of_hand.var_bonus
            },
            key_stealth: {
                key_proficient: skills.stealth.var_prof,
                key_bonus: skills.stealth.var_bonus
            },
            key_survival: {
                key_proficient: skills.survival.var_prof,
                key_bonus: skills.survival.var_bonus
            }
        }

        #max temp hp
        max_temp = LeftRightFrame(tab_stats, left='MAX HP', right='TEMP HP')
        max_temp.grid(row=0, column=3, sticky='nsew')
        data[key_max_hp] = max_temp.var_left
        data[key_temp_hp] = max_temp.var_right

        #current hp and hit dice
        current_hit = LeftRightFrame(tab_stats, left='CURRENT HP', right='HIT DICE')
        current_hit.grid(row=1, column=3, sticky='nsew')
        data[key_current_hp] = current_hit.var_left
        data[key_hit_dice] = current_hit.var_right

        #death saves
        death_saves = DeathSavesFrame(tab_stats)
        death_saves.grid(row=2, column=3, sticky='nsew')
        data[key_success_1] = death_saves.success_1
        data[key_success_2] = death_saves.success_2
        data[key_success_3] = death_saves.success_3
        data[key_failure_1] = death_saves.failure_1
        data[key_failure_2] = death_saves.failure_2
        data[key_failure_3] = death_saves.failure_3

        #features traits
        feat_trait = TextFrame(tab_stats, 'FEATURES & TRAITS')
        feat_trait.grid(row=3, column=3, rowspan=3, sticky='nsew')
        data[key_feat_trait] = feat_trait.text

        #################
        #The File... tab
        #################
        self.add("File...")
        button_save = ctk.CTkButton(self.tab('File...'), text='Save', command=lambda: save(data))
        button_save.pack()

        #################
        #Load saved data
        #################
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                saved = json.loads(f.read())
            s = 'missing' #s for string
            b = False #b for boolean
            d = {} #d for dictionary

            #stats
            strength.var_modifier.set( saved.get(key_strength, d).get(key_modifier, s) )
            strength.var_value.set( saved.get(key_strength, d).get(key_value, s) )
            dexterity.var_modifier.set( saved.get(key_dexterity, d).get(key_modifier, s) )
            dexterity.var_value.set( saved.get(key_dexterity, d).get(key_value, s) )
            constitution.var_modifier.set( saved.get(key_constitution, d).get(key_modifier, s) )
            constitution.var_value.set( saved.get(key_constitution, d).get(key_value, s) )
            intelligence.var_modifier.set( saved.get(key_intelligence, d).get(key_modifier, s) )
            intelligence.var_value.set( saved.get(key_intelligence, d).get(key_value, s) )
            wisdom.var_modifier.set( saved.get(key_wisdom, d).get(key_modifier, s) )
            wisdom.var_value.set( saved.get(key_wisdom, d).get(key_value, s) )
            charisma.var_modifier.set( saved.get(key_charisma, d).get(key_modifier, s) )
            charisma.var_value.set( saved.get(key_charisma, d).get(key_value, s) )

            #saving throws
            saving_throws.strength.var_prof.set( saved.get(key_saving_throws, d).get(key_strength, d).get(key_proficient, b) )
            saving_throws.strength.var_bonus.set( saved.get(key_saving_throws, d).get(key_strength, d).get(key_bonus, s) )
            saving_throws.dexterity.var_prof.set( saved.get(key_saving_throws, d).get(key_dexterity, d).get(key_proficient, b) )
            saving_throws.dexterity.var_bonus.set( saved.get(key_saving_throws, d).get(key_dexterity, d).get(key_bonus, s) )
            saving_throws.constitution.var_prof.set( saved.get(key_saving_throws, d).get(key_constitution, d).get(key_proficient, b) )
            saving_throws.constitution.var_bonus.set( saved.get(key_saving_throws, d).get(key_constitution, d).get(key_bonus, s) )
            saving_throws.intelligence.var_prof.set( saved.get(key_saving_throws, d).get(key_intelligence, d).get(key_proficient, b) )
            saving_throws.intelligence.var_bonus.set( saved.get(key_saving_throws, d).get(key_intelligence, d).get(key_bonus, s) )
            saving_throws.wisdom.var_prof.set( saved.get(key_saving_throws, d).get(key_wisdom, d).get(key_proficient, b) )
            saving_throws.wisdom.var_bonus.set( saved.get(key_saving_throws, d).get(key_wisdom, d).get(key_bonus, s) )
            saving_throws.charisma.var_prof.set( saved.get(key_saving_throws, d).get(key_charisma, d).get(key_proficient, b) )
            saving_throws.charisma.var_bonus.set( saved.get(key_saving_throws, d).get(key_charisma, d).get(key_bonus, s) )
            saving_throws.modifiers.insert('0.0', saved.get(key_saving_throws, d).get(key_modifiers, s) )

            #init ac
            init_ac.var_left.set( saved.get(key_initiative, s) )
            init_ac.var_right.set( saved.get(key_armor_class, s) )

            #prof insp
            prof_insp.var_left.set( saved.get(key_proficiency, s) )
            prof_insp.var_right.set( saved.get(key_inspiration, s) )

            #misc profs
            misc_prof.text.insert('0.0', saved.get(key_proficiencies, s) )

            #skills
            skills.acrobatics.var_prof.set( saved.get(key_skills, d).get(key_acrobatics, d).get(key_proficient, b) )
            skills.acrobatics.var_bonus.set( saved.get(key_skills, d).get(key_acrobatics, d).get(key_bonus, s) )
            skills.animal_handling.var_prof.set( saved.get(key_skills, d).get(key_animal_handling, d).get(key_proficient, b) )
            skills.animal_handling.var_bonus.set( saved.get(key_skills, d).get(key_animal_handling, d).get(key_bonus, s) )
            skills.arcana.var_prof.set( saved.get(key_skills, d).get(key_arcana, d).get(key_proficient, b) )
            skills.arcana.var_bonus.set( saved.get(key_skills, d).get(key_arcana, d).get(key_bonus, s) )
            skills.athletics.var_prof.set( saved.get(key_skills, d).get(key_athletics, d).get(key_proficient, b) )
            skills.athletics.var_bonus.set( saved.get(key_skills, d).get(key_athletics, d).get(key_bonus, s) )
            skills.deception.var_prof.set( saved.get(key_skills, d).get(key_decption, d).get(key_proficient, b) )
            skills.deception.var_bonus.set( saved.get(key_skills, d).get(key_decption, d).get(key_bonus, s) )
            skills.history.var_prof.set( saved.get(key_skills, d).get(key_history, d).get(key_proficient, b) )
            skills.history.var_bonus.set( saved.get(key_skills, d).get(key_history, d).get(key_bonus, s) )
            skills.insight.var_prof.set( saved.get(key_skills, d).get(key_insight, d).get(key_proficient, b) )
            skills.insight.var_bonus.set( saved.get(key_skills, d).get(key_insight, d).get(key_bonus, s) )
            skills.intimidation.var_prof.set( saved.get(key_skills, d).get(key_intimidation, d).get(key_proficient, b) )
            skills.intimidation.var_bonus.set( saved.get(key_skills, d).get(key_intimidation, d).get(key_bonus, s) )
            skills.investigation.var_prof.set( saved.get(key_skills, d).get(key_investigation, d).get(key_proficient, b) )
            skills.investigation.var_bonus.set( saved.get(key_skills, d).get(key_investigation, d).get(key_bonus, s) )
            skills.medicine.var_prof.set( saved.get(key_skills, d).get(key_medicine, d).get(key_proficient, b) )
            skills.medicine.var_bonus.set( saved.get(key_skills, d).get(key_medicine, d).get(key_bonus, s) )
            skills.nature.var_prof.set( saved.get(key_skills, d).get(key_nature, d).get(key_proficient, b) )
            skills.nature.var_bonus.set( saved.get(key_skills, d).get(key_nature, d).get(key_bonus, s) )
            skills.perception.var_prof.set( saved.get(key_skills, d).get(key_perception, d).get(key_proficient, b) )
            skills.perception.var_bonus.set( saved.get(key_skills, d).get(key_perception, d).get(key_bonus, s) )
            skills.performance.var_prof.set( saved.get(key_skills, d).get(key_performance, d).get(key_proficient, b) )
            skills.performance.var_bonus.set( saved.get(key_skills, d).get(key_performance, d).get(key_bonus, s) )
            skills.persuasion.var_prof.set( saved.get(key_skills, d).get(key_persuasion, d).get(key_proficient, b) )
            skills.persuasion.var_bonus.set( saved.get(key_skills, d).get(key_persuasion, d).get(key_bonus, s) )
            skills.religion.var_prof.set( saved.get(key_skills, d).get(key_religion, d).get(key_proficient, b) )
            skills.religion.var_bonus.set( saved.get(key_skills, d).get(key_religion, d).get(key_bonus, s) )
            skills.sleight_of_hand.var_prof.set( saved.get(key_skills, d).get(key_sleight_of_hand, d).get(key_proficient, b) )
            skills.sleight_of_hand.var_bonus.set( saved.get(key_skills, d).get(key_sleight_of_hand, d).get(key_bonus, s) )
            skills.stealth.var_prof.set( saved.get(key_skills, d).get(key_stealth, d).get(key_proficient, b) )
            skills.stealth.var_bonus.set( saved.get(key_skills, d).get(key_stealth, d).get(key_bonus, s) )
            skills.survival.var_prof.set( saved.get(key_skills, d).get(key_survival, d).get(key_proficient, b) )
            skills.survival.var_bonus.set( saved.get(key_skills, d).get(key_survival, d).get(key_bonus, s) )

            #hp
            max_temp.var_left.set( saved.get(key_max_hp, s) )
            max_temp.var_right.set( saved.get(key_temp_hp, s) )
            current_hit.var_left.set( saved.get(key_current_hp, s) )
            current_hit.var_right.set( saved.get(key_hit_dice, s) )
            death_saves.success_1.set( saved.get(key_success_1, b) )
            death_saves.success_2.set( saved.get(key_success_2, b) )
            death_saves.success_3.set( saved.get(key_success_3, b) )
            death_saves.failure_1.set( saved.get(key_failure_1, b) )
            death_saves.failure_2.set( saved.get(key_failure_2, b) )
            death_saves.failure_3.set( saved.get(key_failure_3, b) )

            #features and traits
            feat_trait.text.insert('0.0', saved.get(key_feat_trait, s) )


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.sheet_tabs = SheetTabs(self)
        self.sheet_tabs.pack()


if __name__ == '__main__':
    app = App()
    hs_width = int(app.winfo_screenwidth() / 2)
    hs_height = int(app.winfo_screenheight() / 2)
    a_width = 800
    a_height = 600
    ha_width = int(a_width / 2)
    ha_height = int(a_height / 2)
    app.geometry(f'{a_width}x{a_height}+{hs_width - ha_width}+{hs_height - ha_height}')
    app.minsize(width=800, height=600)
    app.mainloop()