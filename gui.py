import tkinter as tk
import customtkinter as ctk
import os
from save import *


TEN = 10
TWENTY = 20
THIRTY = 30
FIFTY = 50

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
        frame.pack(padx=TEN, pady=TEN)


class BonusProfFrame(ctk.CTkFrame):
    def __init__(self, parent, name, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.var_bonus = tk.StringVar()
        bonus_entry = ctk.CTkEntry(self, width=40, justify='center', textvariable=self.var_bonus)
        bonus_entry.pack(side='left')

        self.var_prof = tk.BooleanVar()
        prof_box = ctk.CTkCheckBox(self, text=name, variable=self.var_prof)
        prof_box.pack(side='left', padx=TEN)


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
    def __init__(self, parent, data, **kwargs):
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

        data[key_saving_throws] = {
            key_strength: {
                key_proficient: self.strength.var_prof,
                key_bonus: self.strength.var_bonus
            },
            key_dexterity: {
                key_proficient: self.dexterity.var_prof,
                key_bonus: self.dexterity.var_bonus
            },
            key_constitution: {
                key_proficient: self.constitution.var_prof,
                key_bonus: self.constitution.var_bonus
            },
            key_intelligence: {
                key_proficient: self.intelligence.var_prof,
                key_bonus: self.intelligence.var_bonus
            },
            key_wisdom: {
                key_proficient: self.wisdom.var_prof,
                key_bonus: self.wisdom.var_bonus
            },
            key_charisma: {
                key_proficient: self.charisma.var_prof,
                key_bonus: self.charisma.var_bonus
            },
            key_modifiers: self.modifiers
        }


class SkillsFrame(ctk.CTkFrame):
    '''18 skills, 19 rows (1 for label). Use 20 rows for simplicty.'''
    def __init__(self, parent, data, **kwargs):
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

        data[key_skills] = {
            key_acrobatics: {
                key_proficient: self.acrobatics.var_prof,
                key_bonus: self.acrobatics.var_bonus
            },
            key_animal_handling: {
                key_proficient: self.animal_handling.var_prof,
                key_bonus: self.animal_handling.var_bonus
            },
            key_arcana: {
                key_proficient: self.arcana.var_prof,
                key_bonus: self.arcana.var_bonus
            },
            key_athletics: {
                key_proficient: self.athletics.var_prof,
                key_bonus: self.athletics.var_bonus
            },
            key_decption: {
                key_proficient: self.deception.var_prof,
                key_bonus: self.deception.var_bonus
            },
            key_history: {
                key_proficient: self.history.var_prof,
                key_bonus: self.history.var_bonus
            },
            key_insight: {
                key_proficient: self.insight.var_prof,
                key_bonus: self.insight.var_bonus
            },
            key_intimidation: {
                key_proficient: self.intimidation.var_prof,
                key_bonus: self.intimidation.var_bonus
            },
            key_investigation: {
                key_proficient: self.investigation.var_prof,
                key_bonus: self.investigation.var_bonus
            },
            key_medicine: {
                key_proficient: self.medicine.var_prof,
                key_bonus: self.medicine.var_bonus
            },
            key_nature: {
                key_proficient: self.nature.var_prof,
                key_bonus: self.nature.var_bonus
            },
            key_perception: {
                key_proficient: self.perception.var_prof,
                key_bonus: self.perception.var_bonus
            },
            key_performance: {
                key_proficient: self.performance.var_prof,
                key_bonus: self.performance.var_bonus
            },
            key_persuasion: {
                key_proficient: self.persuasion.var_prof,
                key_bonus: self.persuasion.var_bonus
            },
            key_religion: {
                key_proficient: self.religion.var_prof,
                key_bonus: self.religion.var_bonus
            },
            key_sleight_of_hand: {
                key_proficient: self.sleight_of_hand.var_prof,
                key_bonus: self.sleight_of_hand.var_bonus
            },
            key_stealth: {
                key_proficient: self.stealth.var_prof,
                key_bonus: self.stealth.var_bonus
            },
            key_survival: {
                key_proficient: self.survival.var_prof,
                key_bonus: self.survival.var_bonus
            }
        }


class DeathSavesFrame(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
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

        data[key_success_1] = self.success_1
        data[key_success_2] = self.success_2
        data[key_success_3] = self.success_3
        data[key_failure_1] = self.failure_1
        data[key_failure_2] = self.failure_2
        data[key_failure_3] = self.failure_3


class ItemFrame(ctk.CTkFrame):
    '''Upon creation this will automatically add itself to the data dict'''
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        button = ctk.CTkButton(self, text='X', fg_color='red', text_color='black', width=30, command=self.remove)
        button.pack(side='left')
        self.var_name = tk.StringVar()
        name = ctk.CTkEntry(self, justify='center', textvariable=self.var_name)
        name.pack(side='left', expand=True, fill='x')
        self.description = ctk.CTkTextbox(self, height=100)
        self.description.pack(side='left', expand=True, fill='x')

        self.data = data
        data[key_items].append(self)
        self.cached_index = len(data[key_items]) - 1

    def remove(self):
        '''
        1) remove this item from the list
        2) update all the other cached_index
        3) remove this item from the gui
        '''
        if messagebox.askyesno(title='WARNING!', message=f'Remove {self.var_name.get().upper()} from your inventory?'):
            #1) remove this item from the list
            del self.data[key_items][self.cached_index]
            #2) update all the other cached_index
            for i in range(len(self.data[key_items])):
                self.data[key_items][i].cached_index = i
            #3) remove this item from the gui
            self.destroy()
            

class CurrencyFrame(ctk.CTkFrame):
    def __init__(self, parent, currency, color='#ffffff', **kwargs):
        super().__init__(parent, **kwargs)

        label = ctk.CTkLabel(self, text=currency, text_color=color)
        label.pack()

        self.var_amount = tk.StringVar()
        amount = ctk.CTkEntry(self, justify='center', textvariable=self.var_amount)
        amount.pack()


class MoneyFrame(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        self.copper = CurrencyFrame(self, currency='COPPER', color='#B87333')
        self.copper.pack(side='left', padx=5)
        self.silver = CurrencyFrame(self, currency='SILVER', color='#C0C0C0')
        self.silver.pack(side='left', padx=5)
        self.gold = CurrencyFrame(self, currency='GOLD', color='#FFD700')
        self.gold.pack(side='left', padx=5)

        data[key_copper] = self.copper.var_amount
        data[key_silver] = self.silver.var_amount
        data[key_gold] = self.gold.var_amount


class JournalFrame(ctk.CTkFrame):
    '''Upon creation this will automatically add itself to the data dict'''
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        button = ctk.CTkButton(self, text='X', fg_color='red', text_color='black', width=30, command=self.remove)
        button.pack(side='left')
        self.var_title = tk.StringVar()
        name = ctk.CTkEntry(self, justify='center', textvariable=self.var_title)
        name.pack(side='left')
        self.note = ctk.CTkTextbox(self, height=120)
        self.note.pack(side='left', expand=True, fill='x')

        self.data = data
        data[key_journal].append(self)
        self.cached_index = len(data[key_journal]) - 1

    def remove(self):
        '''
        1) remove this journal entry from the list
        2) update all the other cached_index
        3) remove this journal entry from the gui
        '''
        if messagebox.askyesno(title='WARNING!', message=f'Remove {self.var_title.get().upper()} from your journal?'):
            #1) remove this journal entry from the list
            del self.data[key_journal][self.cached_index]
            #2) update all the other cached_index
            for i in range(len(self.data[key_journal])):
                self.data[key_journal][i].cached_index = i
            #3) remove this journal entry from the gui
            self.destroy()


class SpellStatFrame(ctk.CTkFrame):
    def __init__(self, parent, label, **kwargs):
        super().__init__(parent, **kwargs)

        l = ctk.CTkLabel(self, text=label)
        l.pack()
        self.var = tk.StringVar()
        entry = ctk.CTkEntry(self, justify='center', textvariable=self.var)
        entry.pack()


class SpellStatsBar(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        self.prepare = SpellStatFrame(self, label='AMOUNT PREPARE')
        self.prepare.pack(side='left')

        self.ability = SpellStatFrame(self, label='SPELLCAST ABILITY')
        self.ability.pack(side='left')

        self.dc = SpellStatFrame(self, label='SPELLSAVE DC')
        self.dc.pack(side='left')

        self.attack = SpellStatFrame(self, label='ATTACK BONUS')
        self.attack.pack(side='left')

        data[key_spell_stats] = {
            key_prepare: self.prepare.var,
            key_ability: self.ability.var,
            key_dc: self.dc.var,
            key_attack: self.attack.var
        }


class SpellSlotFrame(ctk.CTkFrame):
    def __init__(self, parent, level, **kwargs):
        super().__init__(parent, **kwargs)

        label = ctk.CTkLabel(self, text=level, font=(None, 15))
        label.pack()
        self.var_max = tk.StringVar()
        max_entry = ctk.CTkEntry(self, justify='center', width=30, font=(None, 20), textvariable=self.var_max)
        max_entry.pack()
        self.var_used = tk.StringVar()
        used_entry = ctk.CTkEntry(self, justify='center', width=30, font=(None, 20), textvariable=self.var_used)
        used_entry.pack()


class SpellSlotsBar(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        labels_frame = ctk.CTkFrame(self)
        ctk.CTkLabel(labels_frame, text='LVL').pack()
        ctk.CTkLabel(labels_frame, text='MAX').pack()
        ctk.CTkLabel(labels_frame, text='USED').pack()
        labels_frame.pack(side='left', padx=2)

        self.lvl1 = SpellSlotFrame(self, level='1')
        self.lvl1.pack(side='left', padx=2)

        self.lvl2 = SpellSlotFrame(self, level='2')
        self.lvl2.pack(side='left', padx=2)

        self.lvl3 = SpellSlotFrame(self, level='3')
        self.lvl3.pack(side='left', padx=2)

        self.lvl4 = SpellSlotFrame(self, level='4')
        self.lvl4.pack(side='left', padx=2)

        self.lvl5 = SpellSlotFrame(self, level='5')
        self.lvl5.pack(side='left', padx=2)

        self.lvl6 = SpellSlotFrame(self, level='6')
        self.lvl6.pack(side='left', padx=2)

        self.lvl7 = SpellSlotFrame(self, level='7')
        self.lvl7.pack(side='left', padx=2)

        self.lvl8 = SpellSlotFrame(self, level='8')
        self.lvl8.pack(side='left', padx=2)

        self.lvl9 = SpellSlotFrame(self, level='9')
        self.lvl9.pack(side='left', padx=2)

        data[key_spell_slots] = {
            key_lvl1_max: self.lvl1.var_max,
            key_lvl2_max: self.lvl2.var_max,
            key_lvl3_max: self.lvl3.var_max,
            key_lvl4_max: self.lvl4.var_max,
            key_lvl5_max: self.lvl5.var_max,
            key_lvl6_max: self.lvl6.var_max,
            key_lvl7_max: self.lvl7.var_max,
            key_lvl8_max: self.lvl8.var_max,
            key_lvl9_max: self.lvl9.var_max,
            key_lvl1_used: self.lvl1.var_used,
            key_lvl2_used: self.lvl2.var_used,
            key_lvl3_used: self.lvl3.var_used,
            key_lvl4_used: self.lvl4.var_used,
            key_lvl5_used: self.lvl5.var_used,
            key_lvl6_used: self.lvl6.var_used,
            key_lvl7_used: self.lvl7.var_used,
            key_lvl8_used: self.lvl8.var_used,
            key_lvl9_used: self.lvl9.var_used,
        }


class Spell:
    def __init__(self):
        self.cached_index = -1
        self.title = tk.StringVar()
        self.description = ''
        self.prepared = tk.BooleanVar()


class SpellFrame(ctk.CTkFrame):
    def __init__(self, parent, spell, **kwargs):
        super().__init__(parent, **kwargs)

        delete_button = ctk.CTkButton(self,
                                      text='X',
                                      text_color='black',
                                      fg_color='red',
                                      width=30,
                                      command=lambda: parent.delete_spell(spell))
        delete_button.pack(side='left', padx=TWENTY)

        spell_button = ctk.CTkButton(self,
                                     textvariable=spell.title,
                                     command=lambda: parent.view_spell_window(spell))
        spell_button.pack(side='left', expand=True, fill='x', padx=TWENTY)

        prepared = ctk.CTkCheckBox(self, text='PREPARED', variable=spell.prepared)
        prepared.pack(side='left', padx=TWENTY)

        updown_frame = ctk.CTkFrame(self)
        up = ctk.CTkButton(updown_frame, text='Top', width=FIFTY, command=lambda: parent.move_spell(spell, 'top'))
        up.pack(pady=5)
        down = ctk.CTkButton(updown_frame, text='Bot', width=FIFTY, command=lambda: parent.move_spell(spell, 'bot'))
        down.pack(pady=5)
        updown_frame.pack(side='left')


class SpellsFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        self.spell_window = None
        buttons_frame = ctk.CTkFrame(self)
        add_button = ctk.CTkButton(buttons_frame, text='Add', command=self.new_spell_window)
        add_button.pack(side='left', padx=TEN)
        order_by_title = ctk.CTkButton(buttons_frame, text='Order (title)', command=self.order_spells_by_title)
        order_by_title.pack(side='left', padx=TEN)
        order_by_prepared = ctk.CTkButton(buttons_frame, text='Order (prepared)', command=self.order_spells_by_prepared)
        order_by_prepared.pack(side='left', padx=TEN)
        buttons_frame.pack(pady=TWENTY)

        data[key_spells] = [] #initialize spells to empty list
        self.data = data
        self.spell_frames = []

    def delete_spell(self, spell):
        '''
        1) destroy the ui
        2) remove the ui from the list of frames
        3) remove the spell from data
        4) reset all the spells cached_index
        '''
        if messagebox.askyesno(title='WARNING!', message=f'Remove {spell.title.get().upper()} from your spells?'):
            #use i for the index
            ci = spell.cached_index
            #1) destroy the ui
            self.spell_frames[ci].destroy()
            #2) remove the ui from the list of frames
            del self.spell_frames[ci]
            #3) remove the spell from data
            del self.data[key_spells][ci]
            #4) reset all the spells cached_index
            for i in range(len(self.data[key_spells])):
                self.data[key_spells][i].cached_index = i

    def order_spells_by_title(self):
        self.data[key_spells].sort(key=lambda spell: spell.title.get())
        self.recreate_gui_with_data()

    def order_spells_by_prepared(self):
        self.data[key_spells].sort(key=lambda spell: spell.prepared.get())
        self.recreate_gui_with_data()

    def new_spell_window(self):
        self.make_spell_window()
        spell = Spell()
        title_label = ctk.CTkLabel(self.spell_window, text='TITLE')
        title_label.pack()
        title = ctk.CTkEntry(self.spell_window, justify='center', width=300, textvariable=spell.title)
        title.pack()
        ctk.CTkLabel(self.spell_window, text='').pack() #MAKE EMPTY SPACE WHILE USING PACK
        description_label = ctk.CTkLabel(self.spell_window, text='DESCRIPTION')
        description_label.pack()
        description = ctk.CTkTextbox(self.spell_window, border_color='#5f6467', border_width=2)
        description.configure(border_color='#5f6467', border_width=2)
        description.pack(expand=True, fill='both', padx=THIRTY)
        apply = ctk.CTkButton(self.spell_window, text='Apply', command=lambda: self.apply_spell(spell, description))
        apply.pack(pady=THIRTY)

    def view_spell_window(self, spell):
        self.make_spell_window()
        title_label = ctk.CTkLabel(self.spell_window, text='TITLE')
        title_label.pack()
        title = ctk.CTkEntry(self.spell_window, justify='center', width=300, textvariable=spell.title)
        title.pack()
        ctk.CTkLabel(self.spell_window, text='').pack() #MAKE EMPTY SPACE WHILE USING PACK
        description_label = ctk.CTkLabel(self.spell_window, text='DESCRIPTION')
        description_label.pack()
        description = ctk.CTkTextbox(self.spell_window, border_color='#5f6467', border_width=2)
        description.insert('0.0', spell.description)
        description.configure(border_color='#5f6467', border_width=2)
        description.pack(expand=True, fill='both', padx=THIRTY)
        apply = ctk.CTkButton(self.spell_window, text='Apply', command=lambda: self.apply_spell(spell, description))
        apply.pack(pady=THIRTY)

    def apply_spell(self, spell, description):
        '''This applies changes for new and existing spells'''
        #only append the spell if this is a new spell
        spell.description = description.get('0.0', 'end-1c')
        
        if spell.cached_index == -1:
            self.data[key_spells].append(spell)
            spell.cached_index = len(self.data[key_spells]) - 1
        
            spell_frame = SpellFrame(self, spell)
            spell_frame.pack(side='bottom', padx=TEN, pady=TEN, expand=True, fill='x')
            self.spell_frames.append(spell_frame)

        self.spell_window.destroy()

    def load_spell(self, spell):
        #load to data
        self.data[key_spells].append(spell)
        spell.cached_index = len(self.data[key_spells]) - 1

        #load to spells
        spell_frame = SpellFrame(self, spell)
        spell_frame.pack(side='bottom', padx=TEN, pady=TEN, expand=True, fill='x')
        self.spell_frames.append(spell_frame)

    def move_spell(self, spell, to):
        #remove this spell from its spot in data
        del self.data[key_spells][spell.cached_index]
        
        #move it to its new location in data
        if to == 'top':
            self.data[key_spells].append(spell)
        elif to == 'bot':
            self.data[key_spells].insert(0, spell)
        else:
            raise Exception('The only acceptable valutes for "to" are "top" and "bot"')
        
        self.recreate_gui_with_data()

    def recreate_gui_with_data(self):
        for i in range(len(self.data[key_spells])):
            self.data[key_spells][i].cached_index = i
            new_frame = SpellFrame(self, self.data[key_spells][i])
            new_frame.pack(side='bottom', padx=TEN, pady=TEN, expand=True, fill='x')
            self.spell_frames[i].destroy()
            self.spell_frames[i] = new_frame

    def make_spell_window(self):
        if self.spell_window != None:
            return
        self.spell_window = ctk.CTkToplevel(self)
        hs_width = int(self.winfo_screenwidth() / 2)
        hs_height = int(self.winfo_screenheight() / 2)
        w_width = 600
        w_height = 400
        hw_width = int(w_width / 2)
        hw_height = int(w_height / 2)
        self.spell_window.geometry(f'{w_width}x{w_height}+{hs_width - hw_width}+{hs_height - hw_height}')
        self.spell_window.resizable(width=True, height=True)
        self.spell_window.minsize(width=w_width, height=w_height)
        self.spell_window.title('Spell details')
        self.spell_window.bind('<FocusOut>', self.lost_focus)
        self.spell_window.bind('<Destroy>', self.close_window)

    def lost_focus(self, event):
        self.spell_window.focus_force()

    def close_window(self, event):
        self.spell_window = None


class SpellInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, data, **kwargs):
        super().__init__(parent, **kwargs)

        self.stats = SpellStatsBar(self, data=data)
        self.stats.pack(pady=5)

        self.slots = SpellSlotsBar(self, data=data)
        self.slots.pack(pady=5)

        self.spells_frame = SpellsFrame(self, data=data)
        self.spells_frame.pack(pady=5, expand=True, fill='both')


class SheetTabs(ctk.CTkTabview):
    '''THIS IS WHERE THE MAGIC HAPPENS'''
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(width=600, height=1000)

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
        saving_throws = SavingThrowsFrame(tab_stats, data=data)
        saving_throws.grid(row=3, column=2, rowspan=3, sticky='nsew')

        #skills
        skills = SkillsFrame(tab_stats, data=data)
        skills.grid(row=0, column=1, rowspan=6, sticky='nsew')

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
        death_saves = DeathSavesFrame(tab_stats, data=data)
        death_saves.grid(row=2, column=3, sticky='nsew')

        #features traits
        feat_trait = TextFrame(tab_stats, 'FEATURES & TRAITS')
        feat_trait.grid(row=3, column=3, rowspan=3, sticky='nsew')
        data[key_feat_trait] = feat_trait.text

        #################
        #The Inventory tab
        #################
        self.add('Inventory')
        scroll_inv = ctk.CTkScrollableFrame(self.tab('Inventory'))
        button_add = ctk.CTkButton(scroll_inv,
                                   text='Add',
                                   command=lambda: ItemFrame(scroll_inv, data).pack(side='bottom', expand=True, fill='x', pady=5))
        button_add.pack()
        scroll_inv.pack(expand=True, fill='both')
        data[key_items] = [] #initialize to empty list

        #################
        #The Money tab
        #################
        self.add('Money')
        money_frame = MoneyFrame(self.tab('Money'), data=data)
        money_frame.pack(pady=5)

        #################
        #The Journal tab
        #################
        self.add('Journal')
        scroll_journal = ctk.CTkScrollableFrame(self.tab('Journal'))
        button_add = ctk.CTkButton(scroll_journal,
                                   text='Add',
                                   command=lambda: JournalFrame(scroll_journal, data).pack(side='bottom', expand=True, fill='x', pady=5))
        button_add.pack()
        scroll_journal.pack(expand=True, fill='both')
        data[key_journal] = [] #initialize to empty list

        #################
        #The Spells tab
        #################
        self.add('Spells')
        spells_info_frame = SpellInfoFrame(self.tab('Spells'), data=data)
        spells_info_frame.pack(expand=True, fill='both')

        #################
        #The File... tab
        #################
        self.add("File...")
        button_save = ctk.CTkButton(self.tab('File...'), text='Save', command=lambda: save(data))
        button_save.pack(pady=5)

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

            #money
            money_frame.copper.var_amount.set( saved.get(key_copper, s) )
            money_frame.silver.var_amount.set( saved.get(key_silver, s) )
            money_frame.gold.var_amount.set( saved.get(key_gold, s) )

            #items
            if saved.get(key_items) != None:
                for saved_item in saved.get(key_items):
                    item_frame = ItemFrame(scroll_inv, data)
                    item_frame.pack(side='bottom', expand=True, fill='x', pady=5)
                    item_frame.var_name.set( saved_item[key_name] )
                    item_frame.description.insert('0.0', saved_item[key_description] )

            #journal
            if saved.get(key_journal) != None:
                for saved_entry in saved.get(key_journal):
                    journal_frame = JournalFrame(scroll_journal, data)
                    journal_frame.pack(side='bottom', expand=True, fill='x', pady=5)
                    journal_frame.var_title.set( saved_entry[key_title] )
                    journal_frame.note.insert('0.0', saved_entry[key_note] )

            #spell stats
            spells_info_frame.stats.prepare.var.set( saved.get(key_spell_stats, d).get(key_prepare, s) )
            spells_info_frame.stats.ability.var.set( saved.get(key_spell_stats, d).get(key_ability, s) )
            spells_info_frame.stats.dc.var.set( saved.get(key_spell_stats, d).get(key_dc, s) )
            spells_info_frame.stats.attack.var.set( saved.get(key_spell_stats, d).get(key_attack, s) )

            #spell slots
            spells_info_frame.slots.lvl1.var_max.set( saved.get(key_spell_slots, d).get(key_lvl1_max, s) )
            spells_info_frame.slots.lvl2.var_max.set( saved.get(key_spell_slots, d).get(key_lvl2_max, s) )
            spells_info_frame.slots.lvl3.var_max.set( saved.get(key_spell_slots, d).get(key_lvl3_max, s) )
            spells_info_frame.slots.lvl4.var_max.set( saved.get(key_spell_slots, d).get(key_lvl4_max, s) )
            spells_info_frame.slots.lvl5.var_max.set( saved.get(key_spell_slots, d).get(key_lvl5_max, s) )
            spells_info_frame.slots.lvl6.var_max.set( saved.get(key_spell_slots, d).get(key_lvl6_max, s) )
            spells_info_frame.slots.lvl7.var_max.set( saved.get(key_spell_slots, d).get(key_lvl7_max, s) )
            spells_info_frame.slots.lvl8.var_max.set( saved.get(key_spell_slots, d).get(key_lvl8_max, s) )
            spells_info_frame.slots.lvl9.var_max.set( saved.get(key_spell_slots, d).get(key_lvl9_max, s) )
            spells_info_frame.slots.lvl1.var_used.set( saved.get(key_spell_slots, d).get(key_lvl1_used, s) )
            spells_info_frame.slots.lvl2.var_used.set( saved.get(key_spell_slots, d).get(key_lvl2_used, s) )
            spells_info_frame.slots.lvl3.var_used.set( saved.get(key_spell_slots, d).get(key_lvl3_used, s) )
            spells_info_frame.slots.lvl4.var_used.set( saved.get(key_spell_slots, d).get(key_lvl4_used, s) )
            spells_info_frame.slots.lvl5.var_used.set( saved.get(key_spell_slots, d).get(key_lvl5_used, s) )
            spells_info_frame.slots.lvl6.var_used.set( saved.get(key_spell_slots, d).get(key_lvl6_used, s) )
            spells_info_frame.slots.lvl7.var_used.set( saved.get(key_spell_slots, d).get(key_lvl7_used, s) )
            spells_info_frame.slots.lvl8.var_used.set( saved.get(key_spell_slots, d).get(key_lvl8_used, s) )
            spells_info_frame.slots.lvl9.var_used.set( saved.get(key_spell_slots, d).get(key_lvl9_used, s) )

            #spells
            if saved.get(key_spells) != None:
                for saved_spell in saved.get(key_spells):
                    spell = Spell()
                    spell.title.set( saved_spell.get(key_title, s)) 
                    spell.description = saved_spell.get(key_description, s)
                    spell.prepared.set( saved_spell.get(key_prepared, b) )
                    spells_info_frame.spells_frame.load_spell(spell)


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
    app.title('Character Sheet')
    app.mainloop()