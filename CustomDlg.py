#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BTNCANCEL, wxID_DIALOG1BTNOK, wxID_DIALOG1CBGENDER, 
 wxID_DIALOG1CBMARITALSTATUS, wxID_DIALOG1CBSTATE, wxID_DIALOG1CBYEAR, 
 wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT10, wxID_DIALOG1STATICTEXT11, 
 wxID_DIALOG1STATICTEXT12, wxID_DIALOG1STATICTEXT13, wxID_DIALOG1STATICTEXT14, 
 wxID_DIALOG1STATICTEXT15, wxID_DIALOG1STATICTEXT16, wxID_DIALOG1STATICTEXT17, 
 wxID_DIALOG1STATICTEXT18, wxID_DIALOG1STATICTEXT19, wxID_DIALOG1STATICTEXT2, 
 wxID_DIALOG1STATICTEXT20, wxID_DIALOG1STATICTEXT21, wxID_DIALOG1STATICTEXT22, 
 wxID_DIALOG1STATICTEXT23, wxID_DIALOG1STATICTEXT24, wxID_DIALOG1STATICTEXT25, 
 wxID_DIALOG1STATICTEXT26, wxID_DIALOG1STATICTEXT27, wxID_DIALOG1STATICTEXT28, 
 wxID_DIALOG1STATICTEXT29, wxID_DIALOG1STATICTEXT3, wxID_DIALOG1STATICTEXT30, 
 wxID_DIALOG1STATICTEXT31, wxID_DIALOG1STATICTEXT32, wxID_DIALOG1STATICTEXT33, 
 wxID_DIALOG1STATICTEXT34, wxID_DIALOG1STATICTEXT35, wxID_DIALOG1STATICTEXT36, 
 wxID_DIALOG1STATICTEXT37, wxID_DIALOG1STATICTEXT38, wxID_DIALOG1STATICTEXT39, 
 wxID_DIALOG1STATICTEXT4, wxID_DIALOG1STATICTEXT40, wxID_DIALOG1STATICTEXT41, 
 wxID_DIALOG1STATICTEXT42, wxID_DIALOG1STATICTEXT43, wxID_DIALOG1STATICTEXT44, 
 wxID_DIALOG1STATICTEXT45, wxID_DIALOG1STATICTEXT46, wxID_DIALOG1STATICTEXT47, 
 wxID_DIALOG1STATICTEXT48, wxID_DIALOG1STATICTEXT5, wxID_DIALOG1STATICTEXT6, 
 wxID_DIALOG1STATICTEXT7, wxID_DIALOG1STATICTEXT8, wxID_DIALOG1STATICTEXT9, 
 wxID_DIALOG1TXTACHIEVEMENTS, wxID_DIALOG1TXTADDRESS, 
 wxID_DIALOG1TXTAFFILIATED_TO, wxID_DIALOG1TXTCITY, 
 wxID_DIALOG1TXTCOLLEGE_NAME, wxID_DIALOG1TXTCURRENT_CGPA, 
 wxID_DIALOG1TXTDATE, wxID_DIALOG1TXTDOB, wxID_DIALOG1TXTEC_ACTIVITIES, 
 wxID_DIALOG1TXTEMAIL_ID, wxID_DIALOG1TXTENROLLMENT_NO, 
 wxID_DIALOG1TXTFATHERS_NAME, wxID_DIALOG1TXTFIRST_NAME, 
 wxID_DIALOG1TXTHOBBIES, wxID_DIALOG1TXTHOD_NAME, 
 wxID_DIALOG1TXTIT_DESCRIPTION, wxID_DIALOG1TXTIT_DURATION, 
 wxID_DIALOG1TXTIT_ORGANIZATION, wxID_DIALOG1TXTIT_ROLE, 
 wxID_DIALOG1TXTLANG_KNOWN, wxID_DIALOG1TXTLAST_NAME, 
 wxID_DIALOG1TXTMA_DESCRIPTION, wxID_DIALOG1TXTMA_DURATION, 
 wxID_DIALOG1TXTMA_ORGANIZATION, wxID_DIALOG1TXTMA_ROLE, 
 wxID_DIALOG1TXTMIDDLE_NAME, wxID_DIALOG1TXTMI_DESCRIPTION, 
 wxID_DIALOG1TXTMI_DURATION, wxID_DIALOG1TXTMI_ORGANIZATION, 
 wxID_DIALOG1TXTMI_ROLE, wxID_DIALOG1TXTMOTHER_TONGUE, 
 wxID_DIALOG1TXTNATIONALITY, wxID_DIALOG1TXTOBJECTIVE, wxID_DIALOG1TXTPHNO, 
 wxID_DIALOG1TXTPIN, wxID_DIALOG1TXTSTRENGTH, wxID_DIALOG1TXTTECH_SKILLS, 
 wxID_DIALOG1TXTTENTH_PERCENT, wxID_DIALOG1TXTTWELTH_PERCENT, 
 wxID_DIALOG1TXTWEAKNESS, 
] = [wx.NewId() for _init_ctrls in range(95)]
class NotEmptyValidator(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)
    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()
    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("This field must contain some text!", "Error")
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True
    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(425, 172), size=wx.Size(1242, 582),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Student Record')
        self.SetClientSize(wx.Size(1242, 582))
        self.SetBackgroundColour(wx.Colour(165, 42, 42))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Enrollment no.-', name='staticText1', parent=self,
              pos=wx.Point(20, 22), size=wx.Size(110, 17), style=0)
        self.staticText1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticText1.SetHelpText(u'')
        self.staticText1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText1.SetToolTipString(u'Enter your enrollment no.')

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label=u'First Name-', name='staticText2', parent=self,
              pos=wx.Point(20, 50), size=wx.Size(103, 17), style=0)
        self.staticText2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText2.SetToolTipString(u'Enter your first name')

        self.txtEnrollment_no = wx.TextCtrl(id=wxID_DIALOG1TXTENROLLMENT_NO,
              name=u'txtEnrollment_no', parent=self, pos=wx.Point(135, 22),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())
        self.txtEnrollment_no.SetHelpText(u'roll no.')

        self.txtFirst_Name = wx.TextCtrl(id=wxID_DIALOG1TXTFIRST_NAME,
              name=u'txtFirst_Name', parent=self, pos=wx.Point(135, 50),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.staticText3 = wx.StaticText(id=wxID_DIALOG1STATICTEXT3,
              label=u'Middle Name*-', name='staticText3', parent=self,
              pos=wx.Point(20, 80), size=wx.Size(103, 17), style=0)
        self.staticText3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText3.SetToolTipString(u'Enter your middle name')

        self.staticText4 = wx.StaticText(id=wxID_DIALOG1STATICTEXT4,
              label=u'Last Name-', name='staticText4', parent=self,
              pos=wx.Point(20, 110), size=wx.Size(103, 17), style=0)
        self.staticText4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText4.SetToolTipString(u'Enter your last name')

        self.staticText5 = wx.StaticText(id=wxID_DIALOG1STATICTEXT5,
              label=u'Objective-', name='staticText5', parent=self,
              pos=wx.Point(20, 140), size=wx.Size(103, 17), style=0)
        self.staticText5.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText5.SetToolTipString(u'Enter your career objective')

        self.staticText6 = wx.StaticText(id=wxID_DIALOG1STATICTEXT6,
              label=u'Address-', name='staticText6', parent=self,
              pos=wx.Point(20, 170), size=wx.Size(103, 17), style=0)
        self.staticText6.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText6.SetToolTipString(u'Enter your address')

        self.txtMiddle_Name = wx.TextCtrl(id=wxID_DIALOG1TXTMIDDLE_NAME,
              name=u'txtMiddle_Name', parent=self, pos=wx.Point(135, 80),
              size=wx.Size(280, 27), style=0, value=u'')

        self.txtLast_Name = wx.TextCtrl(id=wxID_DIALOG1TXTLAST_NAME,
              name=u'txtLast_Name', parent=self, pos=wx.Point(135, 110),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtObjective = wx.TextCtrl(id=wxID_DIALOG1TXTOBJECTIVE,
              name=u'txtObjective', parent=self, pos=wx.Point(135, 140),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtAddress = wx.TextCtrl(id=wxID_DIALOG1TXTADDRESS,
              name=u'txtAddress', parent=self, pos=wx.Point(135, 170),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.btnOK = wx.Button(id=wx.ID_OK, label=u'&OK', name=u'btnOK',
              parent=self, pos=wx.Point(148, 532), size=wx.Size(85, 29),
              style=0)

        self.btnCancel = wx.Button(id=wx.ID_CANCEL, label=u'&Cancel',
              name=u'btnCancel', parent=self, pos=wx.Point(296, 532),
              size=wx.Size(85, 29), style=0)

        self.staticText7 = wx.StaticText(id=wxID_DIALOG1STATICTEXT7,
              label=u'city-', name='staticText7', parent=self, pos=wx.Point(20,
              200), size=wx.Size(103, 17), style=0)
        self.staticText7.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText7.SetToolTipString(u'Enter city')

        self.staticText8 = wx.StaticText(id=wxID_DIALOG1STATICTEXT8,
              label=u'state-', name='staticText8', parent=self, pos=wx.Point(20,
              230), size=wx.Size(47, 17), style=0)
        self.staticText8.SetHelpText(u'')
        self.staticText8.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText8.SetToolTipString(u'Enter State')

        self.staticText9 = wx.StaticText(id=wxID_DIALOG1STATICTEXT9,
              label=u'Pin-', name='staticText9', parent=self, pos=wx.Point(20,
              260), size=wx.Size(26, 17), style=0)
        self.staticText9.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText9.SetToolTipString(u'Enter your area pin code')

        self.staticText10 = wx.StaticText(id=wxID_DIALOG1STATICTEXT10,
              label=u'e-mail-', name='staticText10', parent=self,
              pos=wx.Point(20, 290), size=wx.Size(53, 17), style=0)
        self.staticText10.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText10.SetToolTipString(u'Enter your email address')

        self.staticText11 = wx.StaticText(id=wxID_DIALOG1STATICTEXT11,
              label=u'phoneno-', name='staticText11', parent=self,
              pos=wx.Point(20, 320), size=wx.Size(71, 17), style=0)
        self.staticText11.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText11.SetToolTipString(u'Enter your phone no.')

        self.staticText12 = wx.StaticText(id=wxID_DIALOG1STATICTEXT12,
              label=u'College_name-', name='staticText12', parent=self,
              pos=wx.Point(20, 350), size=wx.Size(106, 17), style=0)
        self.staticText12.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText12.SetToolTipString(u'Enter your full college name')

        self.staticText13 = wx.StaticText(id=wxID_DIALOG1STATICTEXT13,
              label=u'Affiliated-', name='staticText13', parent=self,
              pos=wx.Point(20, 380), size=wx.Size(69, 17), style=0)
        self.staticText13.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText13.SetToolTipString(u'Your college is affiliated to which university')

        self.staticText14 = wx.StaticText(id=wxID_DIALOG1STATICTEXT14,
              label=u'CurrentAvg-', name='staticText14', parent=self,
              pos=wx.Point(20, 410), size=wx.Size(88, 17), style=0)
        self.staticText14.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText14.SetToolTipString(u'Enter your current cgpa')

        self.staticText15 = wx.StaticText(id=wxID_DIALOG1STATICTEXT15,
              label=u'12thpercent-', name='staticText15', parent=self,
              pos=wx.Point(20, 440), size=wx.Size(94, 17), style=0)
        self.staticText15.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText15.SetToolTipString(u'Enter your twelth class percentage')

        self.staticText16 = wx.StaticText(id=wxID_DIALOG1STATICTEXT16,
              label=u'10thpercent-', name='staticText16', parent=self,
              pos=wx.Point(20, 470), size=wx.Size(94, 17), style=0)
        self.staticText16.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText16.SetToolTipString(u'Enter your tenth class percentage')

        self.staticText17 = wx.StaticText(id=wxID_DIALOG1STATICTEXT17,
              label=u'tech skills-', name='staticText17', parent=self,
              pos=wx.Point(450, 22), size=wx.Size(78, 17), style=0)
        self.staticText17.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText17.SetToolTipString(u'Enter your technical skills')

        self.staticText18 = wx.StaticText(id=wxID_DIALOG1STATICTEXT18,
              label=u'Organization-', name='staticText18', parent=self,
              pos=wx.Point(450, 80), size=wx.Size(92, 17), style=0)
        self.staticText18.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText18.SetToolTipString(u'Enter organization for industrial training')

        self.staticText19 = wx.StaticText(id=wxID_DIALOG1STATICTEXT19,
              label=u'Description-', name='staticText19', parent=self,
              pos=wx.Point(450, 110), size=wx.Size(83, 17), style=0)
        self.staticText19.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText19.SetToolTipString(u'Enter the description ofyour industrial training')

        self.staticText20 = wx.StaticText(id=wxID_DIALOG1STATICTEXT20,
              label=u'Duration-', name='staticText20', parent=self,
              pos=wx.Point(450, 140), size=wx.Size(64, 17), style=0)
        self.staticText20.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText20.SetToolTipString(u'In how much time you completed your training')

        self.staticText21 = wx.StaticText(id=wxID_DIALOG1STATICTEXT21,
              label=u'Role-', name='staticText21', parent=self,
              pos=wx.Point(450, 170), size=wx.Size(35, 17), style=0)
        self.staticText21.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText21.SetToolTipString(u'What was your role in training')

        self.staticText22 = wx.StaticText(id=wxID_DIALOG1STATICTEXT22,
              label=u'Organization-', name='staticText22', parent=self,
              pos=wx.Point(450, 230), size=wx.Size(92, 17), style=0)
        self.staticText22.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText22.SetToolTipString(u'from where have you done your minor project')

        self.staticText23 = wx.StaticText(id=wxID_DIALOG1STATICTEXT23,
              label=u'Description-', name='staticText23', parent=self,
              pos=wx.Point(450, 260), size=wx.Size(83, 17), style=0)
        self.staticText23.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText23.SetToolTipString(u'About what was your minor project')

        self.staticText24 = wx.StaticText(id=wxID_DIALOG1STATICTEXT24,
              label=u'Duration-', name='staticText24', parent=self,
              pos=wx.Point(450, 290), size=wx.Size(64, 17), style=0)
        self.staticText24.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText24.SetToolTipString(u'In how much time you have completed your project')

        self.staticText25 = wx.StaticText(id=wxID_DIALOG1STATICTEXT25,
              label=u'Role-', name='staticText25', parent=self,
              pos=wx.Point(450, 320), size=wx.Size(35, 17), style=0)
        self.staticText25.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText25.SetToolTipString(u'What was your role in minor project')

        self.staticText26 = wx.StaticText(id=wxID_DIALOG1STATICTEXT26,
              label=u'Organization-', name='staticText26', parent=self,
              pos=wx.Point(450, 380), size=wx.Size(92, 17), style=0)
        self.staticText26.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText26.SetToolTipString(u'from where have you done your major project')

        self.staticText27 = wx.StaticText(id=wxID_DIALOG1STATICTEXT27,
              label=u'Description-', name='staticText27', parent=self,
              pos=wx.Point(450, 410), size=wx.Size(83, 17), style=0)
        self.staticText27.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText27.SetToolTipString(u'about what was your major project')

        self.staticText28 = wx.StaticText(id=wxID_DIALOG1STATICTEXT28,
              label=u'Duration-', name='staticText28', parent=self,
              pos=wx.Point(450, 440), size=wx.Size(64, 17), style=0)
        self.staticText28.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText28.SetToolTipString(u'Inhow much time you have completed your project')

        self.staticText29 = wx.StaticText(id=wxID_DIALOG1STATICTEXT29,
              label=u'Role-', name='staticText29', parent=self,
              pos=wx.Point(450, 470), size=wx.Size(35, 17), style=0)
        self.staticText29.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText29.SetToolTipString(u'what was your role in your project')

        self.staticText30 = wx.StaticText(id=wxID_DIALOG1STATICTEXT30,
              label=u'ExtraCurricularActivities-', name='staticText30',
              parent=self, pos=wx.Point(833, 22), size=wx.Size(170, 17),
              style=0)
        self.staticText30.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText30.SetToolTipString(u'what are the activities in which you participated')

        self.staticText31 = wx.StaticText(id=wxID_DIALOG1STATICTEXT31,
              label=u'Achievement-', name='staticText31', parent=self,
              pos=wx.Point(833, 50), size=wx.Size(99, 17), style=0)
        self.staticText31.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText31.SetToolTipString(u'What have you achieved in your academics')

        self.staticText32 = wx.StaticText(id=wxID_DIALOG1STATICTEXT32,
              label=u'Strength-', name='staticText32', parent=self,
              pos=wx.Point(833, 80), size=wx.Size(70, 17), style=0)
        self.staticText32.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText32.SetToolTipString(u'what are your strengths')

        self.staticText33 = wx.StaticText(id=wxID_DIALOG1STATICTEXT33,
              label=u'weakness-', name='staticText33', parent=self,
              pos=wx.Point(833, 110), size=wx.Size(70, 17), style=0)
        self.staticText33.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText33.SetToolTipString(u'Enter your weakness')

        self.staticText34 = wx.StaticText(id=wxID_DIALOG1STATICTEXT34,
              label=u'Hobbies-', name='staticText34', parent=self,
              pos=wx.Point(833, 140), size=wx.Size(61, 17), style=0)
        self.staticText34.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText34.SetToolTipString(u'Enter your hobbies')

        self.staticText35 = wx.StaticText(id=wxID_DIALOG1STATICTEXT35,
              label=u'D.O.B.-', name='staticText35', parent=self,
              pos=wx.Point(833, 170), size=wx.Size(54, 17), style=0)
        self.staticText35.SetHelpText(u'')
        self.staticText35.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText35.SetToolTipString(u'Enter your date of birth')

        self.staticText36 = wx.StaticText(id=wxID_DIALOG1STATICTEXT36,
              label=u'Gender-', name='staticText36', parent=self,
              pos=wx.Point(833, 200), size=wx.Size(61, 17), style=0)
        self.staticText36.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText36.SetToolTipString(u'Enter your gender')

        self.staticText37 = wx.StaticText(id=wxID_DIALOG1STATICTEXT37,
              label=u'Nationality-', name='staticText37', parent=self,
              pos=wx.Point(833, 230), size=wx.Size(87, 17), style=0)
        self.staticText37.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText37.SetToolTipString(u'What is your nationality')

        self.staticText38 = wx.StaticText(id=wxID_DIALOG1STATICTEXT38,
              label=u'MaritalStatus-', name='staticText38', parent=self,
              pos=wx.Point(833, 260), size=wx.Size(104, 17), style=0)
        self.staticText38.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText38.SetToolTipString(u'What is your marital status-married or unmarried')

        self.staticText39 = wx.StaticText(id=wxID_DIALOG1STATICTEXT39,
              label=u'languageKnown-', name='staticText39', parent=self,
              pos=wx.Point(833, 290), size=wx.Size(117, 17), style=0)
        self.staticText39.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText39.SetToolTipString(u'What are the languages you know?')

        self.staticText40 = wx.StaticText(id=wxID_DIALOG1STATICTEXT40,
              label=u'Mother Tongue-', name='staticText40', parent=self,
              pos=wx.Point(833, 320), size=wx.Size(106, 17), style=0)
        self.staticText40.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText40.SetToolTipString(u'What is your mother tongue')

        self.staticText41 = wx.StaticText(id=wxID_DIALOG1STATICTEXT41,
              label=u"Father's Name-", name='staticText41', parent=self,
              pos=wx.Point(833, 350), size=wx.Size(109, 17), style=0)
        self.staticText41.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText41.SetToolTipString(u"Enter your father's name")

        self.staticText42 = wx.StaticText(id=wxID_DIALOG1STATICTEXT42,
              label=u'H.O.D. Name-', name='staticText42', parent=self,
              pos=wx.Point(833, 380), size=wx.Size(98, 17), style=0)
        self.staticText42.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText42.SetToolTipString(u"Enter your H.O.D's name")

        self.staticText43 = wx.StaticText(id=wxID_DIALOG1STATICTEXT43,
              label=u"Today's Date-", name='staticText43', parent=self,
              pos=wx.Point(833, 410), size=wx.Size(91, 17), style=0)
        self.staticText43.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText43.SetToolTipString(u"Enter today's date")

        self.txtcity = wx.TextCtrl(id=wxID_DIALOG1TXTCITY, name=u'txtcity',
              parent=self, pos=wx.Point(135, 200), size=wx.Size(280, 27),
              style=0, value=u'',validator=NotEmptyValidator())

        self.txtpin = wx.TextCtrl(id=wxID_DIALOG1TXTPIN, name=u'txtpin',
              parent=self, pos=wx.Point(135, 260), size=wx.Size(280, 27),
              style=0, value=u'',validator=NotEmptyValidator())

        self.txtemail_id = wx.TextCtrl(id=wxID_DIALOG1TXTEMAIL_ID,
              name=u'txtemail_id', parent=self, pos=wx.Point(135, 290),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtphno = wx.TextCtrl(id=wxID_DIALOG1TXTPHNO, name=u'txtphno',
              parent=self, pos=wx.Point(135, 320), size=wx.Size(280, 27),
              style=0, value=u'',validator=NotEmptyValidator())

        self.txtcollege_name = wx.TextCtrl(id=wxID_DIALOG1TXTCOLLEGE_NAME,
              name=u'txtcollege_name', parent=self, pos=wx.Point(135, 350),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtaffiliated_to = wx.TextCtrl(id=wxID_DIALOG1TXTAFFILIATED_TO,
              name=u'txtaffiliated_to', parent=self, pos=wx.Point(135, 380),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtcurrent_cgpa = wx.TextCtrl(id=wxID_DIALOG1TXTCURRENT_CGPA,
              name=u'txtcurrent_cgpa', parent=self, pos=wx.Point(135, 410),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txttwelth_percent = wx.TextCtrl(id=wxID_DIALOG1TXTTWELTH_PERCENT,
              name=u'txttwelth_percent', parent=self, pos=wx.Point(135, 440),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txttenth_percent = wx.TextCtrl(id=wxID_DIALOG1TXTTENTH_PERCENT,
              name=u'txttenth_percent', parent=self, pos=wx.Point(135, 470),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txttech_skills = wx.TextCtrl(id=wxID_DIALOG1TXTTECH_SKILLS,
              name=u'txttech_skills', parent=self, pos=wx.Point(538, 22),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtit_organization = wx.TextCtrl(id=wxID_DIALOG1TXTIT_ORGANIZATION,
              name=u'txtit_organization', parent=self, pos=wx.Point(540, 80),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtit_description = wx.TextCtrl(id=wxID_DIALOG1TXTIT_DESCRIPTION,
              name=u'txtit_description', parent=self, pos=wx.Point(538, 110),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtit_duration = wx.TextCtrl(id=wxID_DIALOG1TXTIT_DURATION,
              name=u'txtit_duration', parent=self, pos=wx.Point(538, 140),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtit_role = wx.TextCtrl(id=wxID_DIALOG1TXTIT_ROLE,
              name=u'txtit_role', parent=self, pos=wx.Point(538, 170),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtmi_organization = wx.TextCtrl(id=wxID_DIALOG1TXTMI_ORGANIZATION,
              name=u'txtmi_organization', parent=self, pos=wx.Point(538, 230),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtmi_description = wx.TextCtrl(id=wxID_DIALOG1TXTMI_DESCRIPTION,
              name=u'txtmi_description', parent=self, pos=wx.Point(538, 260),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtmi_duration = wx.TextCtrl(id=wxID_DIALOG1TXTMI_DURATION,
              name=u'txtmi_duration', parent=self, pos=wx.Point(538, 290),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtmi_role = wx.TextCtrl(id=wxID_DIALOG1TXTMI_ROLE,
              name=u'txtmi_role', parent=self, pos=wx.Point(538, 320),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtma_organization = wx.TextCtrl(id=wxID_DIALOG1TXTMA_ORGANIZATION,
              name=u'txtma_organization', parent=self, pos=wx.Point(538, 380),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtma_description = wx.TextCtrl(id=wxID_DIALOG1TXTMA_DESCRIPTION,
              name=u'txtma_description', parent=self, pos=wx.Point(538, 410),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtma_duration = wx.TextCtrl(id=wxID_DIALOG1TXTMA_DURATION,
              name=u'txtma_duration', parent=self, pos=wx.Point(538, 440),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtma_role = wx.TextCtrl(id=wxID_DIALOG1TXTMA_ROLE,
              name=u'txtma_role', parent=self, pos=wx.Point(538, 470),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtec_activities = wx.TextCtrl(id=wxID_DIALOG1TXTEC_ACTIVITIES,
              name=u'txtec_activities', parent=self, pos=wx.Point(1000, 22),
              size=wx.Size(190, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtachievements = wx.TextCtrl(id=wxID_DIALOG1TXTACHIEVEMENTS,
              name=u'txtachievements', parent=self, pos=wx.Point(941, 50),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtstrength = wx.TextCtrl(id=wxID_DIALOG1TXTSTRENGTH,
              name=u'txtstrength', parent=self, pos=wx.Point(941, 80),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtweakness = wx.TextCtrl(id=wxID_DIALOG1TXTWEAKNESS,
              name=u'txtweakness', parent=self, pos=wx.Point(941, 110),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txthobbies = wx.TextCtrl(id=wxID_DIALOG1TXTHOBBIES,
              name=u'txthobbies', parent=self, pos=wx.Point(941, 140),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtdob = wx.TextCtrl(id=wxID_DIALOG1TXTDOB, name=u'txtdob',
              parent=self, pos=wx.Point(941, 170), size=wx.Size(280, 27),
              style=0, value=u'',validator=NotEmptyValidator())

        self.txtnationality = wx.TextCtrl(id=wxID_DIALOG1TXTNATIONALITY,
              name=u'txtnationality', parent=self, pos=wx.Point(941, 230),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtlang_known = wx.TextCtrl(id=wxID_DIALOG1TXTLANG_KNOWN,
              name=u'txtlang_known', parent=self, pos=wx.Point(950, 290),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtmother_tongue = wx.TextCtrl(id=wxID_DIALOG1TXTMOTHER_TONGUE,
              name=u'txtmother_tongue', parent=self, pos=wx.Point(941, 320),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtfathers_name = wx.TextCtrl(id=wxID_DIALOG1TXTFATHERS_NAME,
              name=u'txtfathers_name', parent=self, pos=wx.Point(941, 350),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txthod_name = wx.TextCtrl(id=wxID_DIALOG1TXTHOD_NAME,
              name=u'txthod_name', parent=self, pos=wx.Point(941, 380),
              size=wx.Size(280, 27), style=0, value=u'',validator=NotEmptyValidator())

        self.txtdate = wx.TextCtrl(id=wxID_DIALOG1TXTDATE, name=u'txtdate',
              parent=self, pos=wx.Point(941, 410), size=wx.Size(280, 27),
              style=0, value=u'',validator=NotEmptyValidator())

        self.staticText44 = wx.StaticText(id=wxID_DIALOG1STATICTEXT44,
              label=u'Industrial Training-', name='staticText44', parent=self,
              pos=wx.Point(450, 50), size=wx.Size(125, 17), style=0)
        self.staticText44.SetForegroundColour(wx.Colour(255, 255, 0))
        self.staticText44.SetToolTipString(u'Industrial Training')

        self.staticText45 = wx.StaticText(id=wxID_DIALOG1STATICTEXT45,
              label=u'Minor project-', name='staticText45', parent=self,
              pos=wx.Point(450, 200), size=wx.Size(96, 17), style=0)
        self.staticText45.SetForegroundColour(wx.Colour(255, 255, 0))
        self.staticText45.SetToolTipString(u'Minor Project')

        self.staticText46 = wx.StaticText(id=wxID_DIALOG1STATICTEXT46,
              label=u'Major Project-', name='staticText46', parent=self,
              pos=wx.Point(450, 350), size=wx.Size(96, 17), style=0)
        self.staticText46.SetForegroundColour(wx.Colour(255, 255, 0))
        self.staticText46.SetToolTipString(u'Major Project')

        self.staticText47 = wx.StaticText(id=wxID_DIALOG1STATICTEXT47,
              label=u'Year-', name='staticText47', parent=self,
              pos=wx.Point(833, 440), size=wx.Size(42, 17), style=0)
        self.staticText47.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText47.SetToolTipString(u'In which year you are?')

        self.cbgender = wx.ComboBox(choices=['Male', 'Female'],
              id=wxID_DIALOG1CBGENDER, name=u'cbgender', parent=self,
              pos=wx.Point(941, 200), size=wx.Size(189, 29), style=0,
              value=u'Select Gender',validator=NotEmptyValidator())
        self.cbgender.SetLabel(u'')
        self.cbgender.SetToolTipString(u'Select gender')

        self.cbstate = wx.ComboBox(choices=['MP', 'AP', 'UP', 'Delhi', 'Punjab',
              'Kerela', 'Tamil Nadu', 'Maharashtra', 'Orissa'],
              id=wxID_DIALOG1CBSTATE, name=u'cbstate', parent=self,
              pos=wx.Point(135, 230), size=wx.Size(189, 29), style=0,
              value=u'Select State',validator=NotEmptyValidator())
        self.cbstate.SetLabel(u'')
        self.cbstate.SetToolTipString(u'Select State')

        self.cbmaritalstatus = wx.ComboBox(choices=['Married', 'Unmarried'],
              id=wxID_DIALOG1CBMARITALSTATUS, name=u'cbmaritalstatus',
              parent=self, pos=wx.Point(941, 260), size=wx.Size(189, 29),
              style=0, value=u'Select Marital Status',validator=NotEmptyValidator())
        self.cbmaritalstatus.SetLabel(u'')
        self.cbmaritalstatus.SetToolTipString(u'Select Marital Status')

        self.cbyear = wx.ComboBox(choices=['I', 'II', 'III', 'IV'],
              id=wxID_DIALOG1CBYEAR, name=u'cbyear', parent=self,
              pos=wx.Point(941, 440), size=wx.Size(189, 29), style=0,
              value=u'Select Year',validator=NotEmptyValidator())
        self.cbyear.SetLabel(u'')
        self.cbyear.SetToolTipString(u'comboBox1')

        self.staticText48 = wx.StaticText(id=wxID_DIALOG1STATICTEXT48,
              label=u'*-(optional)', name='staticText48', parent=self,
              pos=wx.Point(32, 504), size=wx.Size(79, 17), style=0)
        self.staticText48.SetForegroundColour(wx.Colour(255, 255, 255))

    def __init__(self, parent):
        self._init_ctrls(parent)
