#!/usr/bin/python 

import os 
import wx 
import sqlite3 

# Create the main program window
class MainWindow(wx.Frame): 
    def __init__(self, parent, title): 
        # Create the window 
        wx.Frame.__init__(self, parent, title=title, pos=(100, 100), size=(180,150)) 
        # Place a button on the window 
        buttonCreate = wx.Button(self, wx.ID_ANY, "&Create Data",pos=(40,10),size=(100,25)) 
        # Place a panel on the window 
        self.control = wx.Panel(self)
        # Place a status bar on the window  
        self.CreateStatusBar() # A StatusBar in the bottom of the window 
        # Setting up the menu. 
        filemenu= wx.Menu() 

        # Add items to the menu
        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets. 
        menuCreate = filemenu.Append(wx.ID_ANY, "&Create Data","Create database.") 
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About","About this program.") 
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate program.")
        
        # Creating the menubar. 
        menuBar = wx.MenuBar() 
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar 
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content. 
        
        # Set events. Bind the events defined below to the various controls.
        self.Bind(wx.EVT_BUTTON, self.OnCreate, buttonCreate) 
        self.Bind(wx.EVT_MENU, self.OnCreate, menuCreate) 
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout) 
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Show the window. 
        self.Show(True) 

    def OnAbout(self,e): 
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
        dlg = wx.MessageDialog( self, "A database creator", "About DB Creator", wx.OK) 
        dlg.ShowModal() # Show it 
        dlg.Destroy() # finally destroy it when finished. 

        
    def OnCreate(self,e): 
        fname = "student.db" 
        if os.path.exists(fname): 
            dlg = wx.MessageDialog( self, "Database already exists", "DB Creator", wx.OK) 
            dlg.ShowModal() # Show it 
            dlg.Destroy() # finally destroy it when finished. 
        # This code is carried out if the database doesn't already exist.
        else: 
            connection = sqlite3.connect('student.db') 
            cursor = connection.cursor() 
            cursor.execute(""" 
            CREATE TABLE student ( 
            Enrollment_no varchar(20) primary key , 
            First_Name char(30),
            Middle_Name char (30), 
            Last_Name char(30),
            Objective char(400),
            Address varchar(30),
            city char(30),
            state char(20),
            pin varchar(7),
            email_id varchar(30),
            phno varchar(20),
            college_name char(50),
            affiliated_to char(50),
            current_cgpa varchar(5), 
            twelth_percent varchar(5),
            tenth_percent varchar(5),
            tech_skills varchar(150),
            it_organization varchar(150), 
            it_description varchar(400),
            it_duration varchar(20),
            it_role varchar(100),
            mi_organization varchar(150),
            mi_description varchar(400),
            mi_duration varchar(20),
            mi_role varchar(100),
            ma_organization varchar(150),
            ma_description varchar(400),
            ma_duration varchar(20),
            ma_role varchar(100),
            ec_activities varchar(400), 
            achievements varchar(400),
            strength varchar(400),
            weakness varchar(400),
            hobbies varchar(400),
            dob varchar(20),
            gender char (10),
            nationality char(30),
            marital_status char(30),
            lang_known char(40),
            mother_tongue char(40),
            fathers_name char (50),
            hod_name char (50),
            date varchar(20),
            year varchar(10)
            )""")

            cursor.execute("INSERT INTO student VALUES ('1','Ashmeet','Kaur','Chhabra','studying python','manik bagh road','indore','MP','452001','ash611w@gmail.com','1234567','AITR','RGPV','72','72','86','python','','','','','Aitr','Data Analytics and Resume Mining','3 months','database designer and developer',' ',' ',' ',' ','dance','coordinater in jog week','positive attitude',' ','dance','11-10-94','female','indian','unmarried','english','punjabi','charanjeet singh chhabra','Sanjay Bansal','23-4-15','III')")
            cursor.execute("INSERT INTO student VALUES ('2','divya',' ','soni','learning','palasia','indore','MP','452001','divya.soni2104@gmail.com','6757656','AITR','RGPV','78','73','74','C',' ',' ',' ',' ','Aitr','Data Analytics and Resume Mining','3 months','learner',' ',' ',' ',' ','debate','winner in marathon','punctual',' ','listening songs','21-04-94','female','indian','unmarried','english','hindi','kamal soni','Sanjay Bansal','23-4-15','III')")
            cursor.execute("INSERT INTO student VALUES ('3','garima',' ','sethiya','studying python','usha nagar','indore','MP','452001','gsgarima@gmail.com','1234567','AITR','RGPV','72','72','86','python',' ',' ',' ',' ','Aitr','Data Analytics and Resume Mining','3 months','database designer and developer',' ',' ',' ',' ','dance','coordinater in jog week','positive attitude',' ','dance','11-10-94','female','indian','unmarried','english','punjabi','charanjeet singh chhabra','Sanjay Bansal','23-4-15','III')")
            
                                       
            connection.commit()
            cursor.close()
            connection.close() 

            dlg = wx.MessageDialog( self, "Database created.", "DB Creator", wx.OK) 
            dlg.ShowModal() # Show it 
            dlg.Destroy() # finally destroy it when finished. 

    def OnExit(self,e): 
        self.Close(True) # Close the frame. 

app = wx.App(False) 
frame = MainWindow(None, "DB Creator") 
app.MainLoop()
