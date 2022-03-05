# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3.

@author: 1569546
"""
# =============================================================================
# Anti-Temporary Mail GUI - SENSUS 2022
# Written by: Noah Olmeijer - n.c.c.p.olmeijer@student.tue.nl
# =============================================================================

import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image


class antiTempMail:
    """App class contains methods for reading, reducing, and writing votes."""

    def __init__(self, parent, db_tempmail='vote_files/dea_database.xlsx'):

        # set title and geometry
        parent.title("ATM-GUI - SensUs - 2022")
        parent.geometry("510x310")
        parent.minsize(640, 480)
        parent.maxsize(640, 480)

        # create select + start button and label
        select_button = tk.Button(parent, text='Select vote data', width=20,
                                  command=self.openFile, font='sans 9 bold')
        start_button = tk.Button(parent, text='Start', width=5,
                                 command=self.exportToExcel, bg='green',
                                 fg='white', font='sans 9 bold')
        self.select_label = tk.Label(parent, text='', fg='black')

        # pack objects
        self.select_label.pack(side=tk.BOTTOM)
        start_button.place(x=375, y=340)
        select_button.place(x=220, y=340)

        # add sensus logo
        logo = ImageTk.PhotoImage(Image.open('vote_files/logo.png'))
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.place(x=140, y=50)

        # set db_votes as NoneType string
        self.db_votes = ''

    def openFile(self):
        """Select Excel file containing SensUs Event votes."""
        # open vote file
        self.db_votes = askopenfilename(
            title="please, open voting file",
            filetypes=([("excel files", "*.xlsx")]))

        # update label with file location
        self.select_label['text'] = self.db_votes

        # update idletasks (reloads frame)
        root.update_idletasks()

        return self.db_votes

    def loadVoteData(self, db_tempmail='vote_files/dea_database.xlsx'):
        """Load Excel file containing SensUs Event votes."""
        # initialize voting data
        self.vote_data_org = pd.read_excel(self.db_votes)
        self.vote_data = self.vote_data_org.copy()

        # count amount of votes
        self.amt_votes = self.vote_data.shape[0]

        # initialize DEA database
        self.temp_mail = set(pd.read_excel(db_tempmail).iloc[:, 0].unique())

        # obtain email column
        self.vote_mail = self.vote_data.iloc[:, 0].to_list()

    def stripVoteMail(self):
        """Strip all usernames from email addresses."""
        # convert element datatype to string
        vote_mails = [str(mail) for mail in self.vote_mail]

        # create empty list for stripped email
        self.stripped_mail = []

        # for each email strip username and @-symbol
        for mail in vote_mails:

            # split string into username and mail server + domain
            split = mail.split('@')

            # append mail server + domain to stripped_mail
            self.stripped_mail.append(split[-1])

        return self.stripped_mail

    def delTempMail(self):
        """Remove all fake votes based on DEA database."""
        # create pandas series of booleans
        # True if mail server in DEA database
        bools = pd.Series(
            [boolean in self.temp_mail
             for boolean in self.stripVoteMail()], name='bool')

        # merge vote_data and bools
        self.bool_concat = pd.concat([self.vote_data, bools], axis=1)

        # remove all rows containing bool = True
        self.reduced_votes = self.bool_concat[self.bool_concat[
            'bool'] != True].copy()

        # remove bool column
        self.reduced_votes.drop('bool', inplace=True, axis=1)

        # count amount of votes in reduced dataframe
        self.amt_reduced_votes = self.reduced_votes.shape[0]

        return self.reduced_votes

    def exportToExcel(self):
        """Export reduced votes to Excel file."""
        # check if datafile is selected
        if self.db_votes == '':

            # show warning and return
            messagebox.showinfo('Warning', 'First select voting data!')
            return

        # run loadVoteData once
        self.loadVoteData()

        # write reduced voting data to excel (.xlsx)
        self.delTempMail().to_excel('reduced_voting.xlsx', index=False)

        # calculate amount of removed votes
        self.amt_removed = self.amt_votes - self.amt_reduced_votes

        # show finished and return
        messagebox.showinfo(
            'Finished', 'Finished removing votes,\n' +
            str(self.amt_removed) + ' votes removed!')
        return


root = tk.Tk()
root.iconbitmap('vote_files/sensus.ico')
App = antiTempMail(root)
root.mainloop()
root.mainloop()
