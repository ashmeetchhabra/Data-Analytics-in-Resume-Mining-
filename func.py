import wx
import wx.grid
import sqlite3
import CustomDlg
import Frame2
import string
from bottle import route, run,template
import webbrowser
def OnDelete(self, event):
    dialog = wx.TextEntryDialog(None, "Student Enrollment no.?", "Student delete", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor()
        sql="select * from student where Enrollment_no='"+searchVal+"'"
        cursor.execute(sql)
        recordset=cursor.fetchall()
        if len(recordset)<>0:
            cursor.execute("DELETE FROM student WHERE Enrollment_no = '" + searchVal + "'") 
            connection.commit() 
            # A message dialog box with an OK button. wx.OK is a standard ID
            # in wxWidgets.
            dlg = wx.MessageDialog(self, "Record Deleted ", "DB GUI", wx.OK) 
            dlg.ShowModal() # Show it 
            dlg.Destroy() # finally destroy it when finished.
        else: 
            dlg2 = wx.MessageDialog(self, "Student Record does not exist", "DB GUI", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        cursor.close()
        connection.close()
    dialog.Destroy()

def OnMenuFileDeleteMenu(self, event):
    dialog = wx.TextEntryDialog(None, "Student Enrollment no.?", "Student delete", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor()
        sql="select * from student where Enrollment_no='"+searchVal+"'"
        cursor.execute(sql)
        recordset=cursor.fetchall()
        if len(recordset)<>0:
            cursor.execute("DELETE FROM student WHERE Enrollment_no = '" + searchVal + "'") 
            connection.commit() 
            # A message dialog box with an OK button. wx.OK is a standard ID
            # in wxWidgets.
            dlg = wx.MessageDialog(self, "Record Deleted ", "DB GUI", wx.OK) 
            dlg.ShowModal() # Show it 
            dlg.Destroy() # finally destroy it when finished.
        else: 
            dlg2 = wx.MessageDialog(self, "Student Record does not exist", "DB GUI", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        cursor.close()
        connection.close()
    dialog.Destroy()

def OnAdd(self, event):
    dlg = CustomDlg.Dialog1(self) 
    try: 
        if dlg.ShowModal() == wx.ID_OK:  
            Enrollment_no = dlg.txtEnrollment_no.GetValue() 
            First_Name = dlg.txtFirst_Name.GetValue()
            Last_Name = dlg.txtLast_Name.GetValue()
            Middle_Name = dlg.txtMiddle_Name.GetValue()
            Objective = dlg.txtObjective.GetValue()
            Address = dlg.txtAddress.GetValue()
            city=dlg.txtcity.GetValue()
            state=dlg.cbstate.GetStringSelection()
            pin=dlg.txtpin.GetValue()
            email_id=dlg.txtemail_id.GetValue()
            phno=dlg.txtphno.GetValue()
            college_name=dlg.txtcollege_name.GetValue()
            affiliated_to=dlg.txtaffiliated_to.GetValue()
            current_cgpa=dlg.txtcurrent_cgpa.GetValue()
            twelth_percent=dlg.txttwelth_percent.GetValue()
            tenth_percent=dlg.txttenth_percent.GetValue()
            tech_skills=dlg.txttech_skills.GetValue()
            it_organization=dlg.txtit_organization.GetValue()
            it_description=dlg.txtit_description.GetValue()
            it_duration=dlg.txtit_duration.GetValue()
            it_role=dlg.txtit_role.GetValue()
            mi_organization=dlg.txtmi_organization.GetValue()
            mi_description=dlg.txtmi_description.GetValue()
            mi_duration=dlg.txtmi_duration.GetValue()
            mi_role=dlg.txtmi_role.GetValue()
            ma_organization=dlg.txtma_organization.GetValue()
            ma_description=dlg.txtma_description.GetValue()
            ma_duration=dlg.txtma_duration.GetValue()
            ma_role=dlg.txtma_role.GetValue()
            ec_activities=dlg.txtec_activities.GetValue()
            achievements=dlg.txtachievements.GetValue()
            strength=dlg.txtstrength.GetValue()
            weakness=dlg.txtweakness.GetValue()
            hobbies=dlg.txthobbies.GetValue()
            dob=dlg.txtdob.GetValue()
            gender=dlg.cbgender.GetStringSelection()
            nationality=dlg.txtnationality.GetValue()
            marital_status=dlg.cbmaritalstatus.GetStringSelection()
            lang_known=dlg.txtlang_known.GetValue()
            mother_tongue=dlg.txtmother_tongue.GetValue()
            fathers_name=dlg.txtfathers_name.GetValue()
            hod_name=dlg.txthod_name.GetValue()
            date=dlg.txtdate.GetValue()
            year=dlg.cbyear.GetStringSelection()
            #password=dlg.txtpassword.GetValue()
            #renter_password=dlg.txtrenter_password.GetValue()
            
            connection = sqlite3.connect('student.db') 
            cursor = connection.cursor() 
            sql = "SELECT * FROM student WHERE Enrollment_no = '" + Enrollment_no + "'" 
            cursor.execute(sql) 
            recordset = cursor.fetchall() 
            if len(recordset) <> 0: 
                dlg2 = wx.MessageDialog(self, "Student Record already exists", "s", wx.OK) 
                dlg2.ShowModal() # Show it 
                dlg2.Destroy() # finally destroy it when finished. 
            else: 
                cursor.execute("INSERT INTO student VALUES ('%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s',\
'%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s',\
'%s','%s','%s','%s')" % (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,\
phno,college_name,affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,\
it_role,mi_organization,mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,\
strength,weakness,hobbies,dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year)) 
                connection.commit() 
                # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
                dlg2 = wx.MessageDialog( self, "Student record added", "student", wx.OK) 
                dlg2.ShowModal() # Show it 
                dlg2.Destroy() # finally destroy it when finished. 
    finally: 
            #cursor.Close() 
            #connection.Close() 
            dlg.Destroy()

def OnMenuFileAddMenu(self, event):
    dlg = CustomDlg.Dialog1(self) 
    try: 
        if dlg.ShowModal() == wx.ID_OK:  
            Enrollment_no = dlg.txtEnrollment_no.GetValue() 
            First_Name = dlg.txtFirst_Name.GetValue()
            Last_Name = dlg.txtLast_Name.GetValue()
            Middle_Name = dlg.txtMiddle_Name.GetValue()
            Objective = dlg.txtObjective.GetValue()
            Address = dlg.txtAddress.GetValue()
            city=dlg.txtcity.GetValue()
            state=dlg.cbstate.GetStringSelection()
            pin=dlg.txtpin.GetValue()
            email_id=dlg.txtemail_id.GetValue()
            phno=dlg.txtphno.GetValue()
            college_name=dlg.txtcollege_name.GetValue()
            affiliated_to=dlg.txtaffiliated_to.GetValue()
            current_cgpa=dlg.txtcurrent_cgpa.GetValue()
            twelth_percent=dlg.txttwelth_percent.GetValue()
            tenth_percent=dlg.txttenth_percent.GetValue()
            tech_skills=dlg.txttech_skills.GetValue()
            it_organization=dlg.txtit_organization.GetValue()
            it_description=dlg.txtit_description.GetValue()
            it_duration=dlg.txtit_duration.GetValue()
            it_role=dlg.txtit_role.GetValue()
            mi_organization=dlg.txtmi_organization.GetValue()
            mi_description=dlg.txtmi_description.GetValue()
            mi_duration=dlg.txtmi_duration.GetValue()
            mi_role=dlg.txtmi_role.GetValue()
            ma_organization=dlg.txtma_organization.GetValue()
            ma_description=dlg.txtma_description.GetValue()
            ma_duration=dlg.txtma_duration.GetValue()
            ma_role=dlg.txtma_role.GetValue()
            ec_activities=dlg.txtec_activities.GetValue()
            achievements=dlg.txtachievements.GetValue()
            strength=dlg.txtstrength.GetValue()
            weakness=dlg.txtweakness.GetValue()
            hobbies=dlg.txthobbies.GetValue()
            dob=dlg.txtdob.GetValue()
            gender=dlg.cbgender.GetStringSelection()
            nationality=dlg.txtnationality.GetValue()
            marital_status=dlg.cbmaritalstatus.GetStringSelection()
            lang_known=dlg.txtlang_known.GetValue()
            mother_tongue=dlg.txtmother_tongue.GetValue()
            fathers_name=dlg.txtfathers_name.GetValue()
            hod_name=dlg.txthod_name.GetValue()
            date=dlg.txtdate.GetValue()
            year=dlg.cbyear.GetStringSelection()
            #password=dlg.txtpassword.GetValue()
            #renter_password=dlg.txtrenter_password.GetValue()
            connection = sqlite3.connect('student.db') 
            cursor = connection.cursor() 
            sql = "SELECT * FROM student WHERE Enrollment_no = '" + Enrollment_no + "'" 
            cursor.execute(sql) 
            recordset = cursor.fetchall() 
            if len(recordset) <> 0: 
                dlg2 = wx.MessageDialog(self, "Student Record already exists", "s", wx.OK) 
                dlg2.ShowModal() # Show it 
                dlg2.Destroy() # finally destroy it when finished. 
            else: 
                cursor.execute("INSERT INTO student VALUES ('%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s',\
'%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s','%s','%s','%s', '%s', '%s','%s',\
'%s','%s','%s','%s')" % (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,\
phno,college_name,affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,\
it_role,mi_organization,mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,\
strength,weakness,hobbies,dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year)) 
                connection.commit() 
                # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
                dlg2 = wx.MessageDialog( self, "Student record added", "student", wx.OK) 
                dlg2.ShowModal() # Show it 
                dlg2.Destroy() # finally destroy it when finished. 
    finally: 
            #cursor.Close() 
            #connection.Close() 
            dlg.Destroy()

def OnFind(self, event): 
    dialog = wx.TextEntryDialog(None,"Student Enrollment no.?","Find Record", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db')
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE Enrollment_no = '" + searchVal + "'" 
        cursor.execute(sql)
        recordset = cursor.fetchall() 
        if len(recordset) <> 0: 
 
            for (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,phno,college_name,\
affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,it_role,mi_organization,\
mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,strength,weakness,hobbies,\
dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year) in recordset: 
                dlg = wx.MessageDialog( self,"Enrollment no.: " + str(Enrollment_no) + " \nFirst Name: " + First_Name + " \nMiddle Name:" + Middle_Name + "\nLast Name:" + Last_Name + "\n Objective:" + Objective + "\nAddress:" + str(Address) + "\ncity:" + city + "\nState:" + state + "\npin" + str(pin) + "\nEmail id:" + str(email_id) + "\n ph no.:" + str(phno) + "\ncollege name:" + college_name + "\nAffiliated to:" + affiliated_to + " \ncurrent CGPA: " + str(current_cgpa) + "\ntwelth percent:" + str(twelth_percent) + "\ntenth percent:" +str(tenth_percent)+ "\ntechnical skills:" +str(tech_skills) + "\nIndustrial training-organization:" + str(it_organization) + "\ndescription:" + str(it_description) + "\nduration:" + str(it_duration) + "\nrole:" + str(it_role) + "\nMinor Project-organization:" + str(mi_organization) + "\ndescription:" + str(it_description) + "\nduration:"+str(it_duration)+"role: " + str(it_role) + " \nMajor project-organization: " + str(ma_organization) + "\ndescription:" + str(ma_description) + "\nduration:" + str(ma_duration) + "\n role:" + str(ma_role) + "\nextra curricular activities:" +str(ec_activities) + "\nAchievements:" + str(achievements) + "\nStrength:" + str(strength) + " \nWeakness:" + str(weakness) +"\nhobbies:" + str(hobbies) + "\n D.O.B.:" + str(dob) + "\nGender:" + gender + "\nnationality: " + nationality + " \nmarital status: " + marital_status + " \nlanguage known:" + lang_known + "\nmother tongue:" + mother_tongue + "\nfather's name :" + fathers_name + "\nH.O.D.'s name:" + hod_name + "\ntoday's date: " + str(date) + "\nYear: " + str(year), "student", wx.OK) 
                dlg.ShowModal() # Show it 
                dlg.Destroy() # finally destroy it when finished. 
        else: 
            dlg2 = wx.MessageDialog( self, "Record not found", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        cursor.close() 
        connection.close() 
    dialog.Destroy()

def OnMenuFileFindMenu(self, event):
    dialog = wx.TextEntryDialog(None,"Student Enrollment no.?","Find Record", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db')
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE Enrollment_no = '" + searchVal + "'" 
        cursor.execute(sql)
        recordset = cursor.fetchall() 
        if len(recordset) <> 0: 
 
            for (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,phno,college_name,\
affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,it_role,mi_organization,\
mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,strength,weakness,hobbies,\
dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year) in recordset: 
                dlg = wx.MessageDialog( self,"Enrollment no.: " + str(Enrollment_no) + " \nFirst Name: " + First_Name + " \nMiddle Name:" + Middle_Name + "\nLast Name:" + Last_Name + "\n Objective:" + Objective + "\nAddress:" + str(Address) + "\ncity:" + city + "\nState:" + state + "\npin" + str(pin) + "\nEmail id:" + str(email_id) + "\n ph no.:" + str(phno) + "\ncollege name:" + college_name + "\nAffiliated to:" + affiliated_to + " \ncurrent CGPA: " + str(current_cgpa) + "\ntwelth percent:" + str(twelth_percent) + "\ntenth percent:" +str(tenth_percent)+ "\ntechnical skills:" +str(tech_skills) + "\nIndustrial training-organization:" + str(it_organization) + "\ndescription:" + str(it_description) + "\nduration:" + str(it_duration) + "\nrole:" + str(it_role) + "\nMinor Project-organization:" + str(mi_organization) + "\ndescription:" + str(it_description) + "\nduration:"+str(it_duration)+"role: " + str(it_role) + " \nMajor project-organization: " + str(ma_organization) + "\ndescription:" + str(ma_description) + "\nduration:" + str(ma_duration) + "\n role:" + str(ma_role) + "\nextra curricular activities:" +str(ec_activities) + "Achievements:" + str(achievements) + "\nStrength:" + str(strength) + " \nWeakness:" + str(weakness) +"\nhobbies:" + str(hobbies) + "\n D.O.B.:" + str(dob) + "\nGender:" + gender + "\nnationality: " + nationality + " \nmarital status: " + marital_status + " \nlanguage known:" + lang_known + "\nmother tongue:" + mother_tongue + "\nfather's name :" + fathers_name + "\nH.O.D.'s name:" + hod_name + "\ntoday's date: " + str(date) + "\nYear: " + str(year) , "student", wx.OK) 
                dlg.ShowModal() # Show it 
                dlg.Destroy() # finally destroy it when finished. 
        else: 
            dlg2 = wx.MessageDialog( self, "Record not found", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        cursor.close() 
        connection.close() 
    dialog.Destroy()


def OnEdit(self, event): 
    dialog = wx.TextEntryDialog(None,"Enrollment no.?","Edit Student Record", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE Enrollment_no = '" + searchVal + "'" 
        cursor.execute(sql) 
        recordset = cursor.fetchall() 
        if len(recordset) == 0: 
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
            dlg2 = wx.MessageDialog( self, "Student Record not found", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        else:
            # Write the user input to the CustomDlg text boxes. 
            for (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,\
phno,college_name,affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,\
it_role,mi_organization,mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,\
strength,weakness,hobbies,dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year) in recordset: 
                dlg = CustomDlg.Dialog1(self) 
                dlg.txtEnrollment_no.Value = "%s" % Enrollment_no 
                dlg.txtFirst_Name.Value = "%s" % First_Name
                dlg.txtMiddle_Name.Value = "%s" % Middle_Name
                dlg.txtLast_Name.Value = "%s" % Last_Name
                dlg.txtObjective.Value = "%s" % Objective
                dlg.txtAddress.Value = "%s" % Address
                dlg.txtcity.Value = "%s" % city
                dlg.cbstate.Value = "%s" % state
                dlg.txtpin.Value = "%s" % pin
                dlg.txtemail_id.Value = "%s" % email_id
                dlg.txtphno.Value = "%s" % phno
                dlg.txtcollege_name.Value = "%s" % college_name
                dlg.txtaffiliated_to.Value = "%s" % affiliated_to
                dlg.txtcurrent_cgpa.Value = "%s" % current_cgpa
                dlg.txttwelth_percent.Value = "%s" % twelth_percent
                dlg.txttenth_percent.Value = "%s" % tenth_percent
                dlg.txttech_skills.Value = "%s" % tech_skills
                dlg.txtit_organization.Value = "%s" % it_organization
                dlg.txtit_description.Value = "%s" % it_description
                dlg.txtit_duration.Value = "%s" % it_duration
                dlg.txtit_role.Value = "%s" % it_role
                dlg.txtmi_organization.Value = "%s" % mi_organization
                dlg.txtmi_description.Value = "%s" % mi_description
                dlg.txtmi_duration.Value = "%s" % mi_duration
                dlg.txtmi_role.Value = "%s" % mi_role
                dlg.txtma_organization.Value = "%s" % ma_organization
                dlg.txtma_description.Value = "%s" % ma_description
                dlg.txtma_duration.Value = "%s" % ma_duration
                dlg.txtma_role.Value = "%s" % ma_role
                dlg.txtec_activities.Value = "%s" % ec_activities
                dlg.txtachievements.Value = "%s" % achievements
                dlg.txtstrength.Value = "%s" % strength
                dlg.txtweakness.Value = "%s" % weakness
                dlg.txthobbies.Value = "%s" % hobbies
                dlg.txtdob.Value = "%s" % dob
                dlg.cbgender.Value = "%s" % gender
                dlg.txtnationality.Value = "%s" % nationality
                dlg.cbmaritalstatus.Value = "%s" % marital_status
                dlg.txtlang_known.Value = "%s" % lang_known
                dlg.txtmother_tongue.Value = "%s" % mother_tongue
                dlg.txtfathers_name.Value = "%s" % fathers_name
                dlg.txthod_name.Value = "%s" % hod_name
                dlg.txtdate.Value = "%s" % date
                dlg.cbyear.Value = "%s" % year
                #dlg.txtpassword.Value = "%s" % password
                #dlg.txtrenter_password.Value = "%s" % renter_password
                try: 
                    if dlg.ShowModal() == wx.ID_OK: 
                        Enrollment_no = dlg.txtEnrollment_no.GetValue() 
                        First_Name = dlg.txtFirst_Name.GetValue() 
                        Middle_Name = dlg.txtMiddle_Name.GetValue() 
                        Last_Name = dlg.txtLast_Name.GetValue() 
                        Objective = dlg.txtObjective.GetValue() 
                        Address = dlg.txtAddress.GetValue() 
                        city=dlg.txtcity.GetValue()
                        state=dlg.cbstate.GetValue()
                        pin=dlg.txtpin.GetValue()
                        email_id=dlg.txtemail_id.GetValue()
                        phno=dlg.txtphno.GetValue()
                        college_name=dlg.txtcollege_name.GetValue()
                        affiliated_to=dlg.txtaffiliated_to.GetValue()
                        current_cgpa=dlg.txtcurrent_cgpa.GetValue()
                        twelth_percent=dlg.txttwelth_percent.GetValue()
                        tenth_percent=dlg.txttenth_percent.GetValue()
                        tech_skills=dlg.txttech_skills.GetValue()
                        it_organization=dlg.txtit_organization.GetValue()
                        it_description=dlg.txtit_description.GetValue()
                        it_duration=dlg.txtit_duration.GetValue()
                        it_role=dlg.txtit_role.GetValue()
                        mi_organization=dlg.txtmi_organization.GetValue()
                        mi_description=dlg.txtmi_description.GetValue()
                        mi_duration=dlg.txtmi_duration.GetValue()
                        mi_role=dlg.txtmi_role.GetValue()
                        ma_organization=dlg.txtma_organization.GetValue()
                        ma_description=dlg.txtma_description.GetValue()
                        ma_duration=dlg.txtma_duration.GetValue()
                        ma_role=dlg.txtma_role.GetValue()
                        ec_activities=dlg.txtec_activities.GetValue()
                        achievements=dlg.txtachievements.GetValue()
                        strength=dlg.txtstrength.GetValue()
                        weakness=dlg.txtweakness.GetValue()
                        hobbies=dlg.txthobbies.GetValue()
                        dob=dlg.txtdob.GetValue()
                        gender=dlg.cbgender.GetStringSelection()
                        nationality=dlg.txtnationality.GetValue()
                        marital_status=dlg.cbmaritalstatus.GetValue()
                        lang_known=dlg.txtlang_known.GetValue()
                        mother_tongue=dlg.txtmother_tongue.GetValue()
                        fathers_name=dlg.txtfathers_name.GetValue()
                        hod_name=dlg.txthod_name.GetValue()
                        date=dlg.txtdate.GetValue()
                        year=dlg.cbyear.GetValue()
                        #password=dlg.txtpassword.GetValue()
                        #renter_password=dlg.txtrenter_password.GetValue()


                        connection = sqlite3.connect('student.db') 
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE student SET Enrollment_no ='" + Enrollment_no + "', First_Name ='" + First_Name +"', Middle_Name ='" + Middle_Name + "', Last_Name ='" + Last_Name + "', Objective ='" + Objective +"',Address ='" + Address +"',city='"+city+"',state='"+state+"',pin='"+pin+"',email_id='"+email_id+\
"',phno='"+phno+"',college_name='"+college_name+"',affiliated_to='"+affiliated_to+"',current_cgpa='"+current_cgpa+"',twelth_percent='"+twelth_percent+"',tenth_percent='"+tenth_percent+"',tech_skills='"+tech_skills+"',it_organization='"+it_organization+"',it_description='"+it_description+"',it_duration='"+it_duration+"',it_role='"+it_role+"',mi_organization='"+mi_organization+"',mi_description='"+mi_description+"',mi_duration='"+mi_duration+"',mi_role='"+mi_role+"',ma_organization='"+ma_organization+"',ma_description='"+ma_description+"',ma_duration='"+ma_duration+"',ma_role='"+ma_role+"',ec_activities='"+ec_activities+"',achievements='"+achievements+"',strength='"+strength+"',weakness='"+weakness+"',hobbies='"+hobbies+"',dob='"+dob+"',gender='"+gender+"',nationality='"+nationality+"',marital_status='"+marital_status+"',lang_known='"+lang_known+"',mother_tongue='"+mother_tongue+"',fathers_name='"+fathers_name+"',hod_name='"+hod_name+"',date='"+date+"',year='"+year+"' WHERE Enrollment_no='" + searchVal + "'")
                        
                        connection.commit() 
                        dlg.txtEnrollment_no.Clear() 
                        dlg.txtFirst_Name.Clear() 
                        dlg.txtMiddle_Name.Clear() 
                        dlg.txtLast_Name.Clear() 
                        dlg.txtObjective.Clear() 
                        dlg.txtAddress.Clear() 
                        dlg.txtcity.Clear() 
                        dlg.cbstate.Clear() 
                        dlg.txtpin.Clear() 
                        dlg.txtemail_id.Clear() 
                        dlg.txtphno.Clear() 
                        dlg.txtcollege_name.Clear() 
                        dlg.txtaffiliated_to.Clear() 
                        dlg.txtcurrent_cgpa.Clear() 
                        dlg.txttwelth_percent.Clear() 
                        dlg.txttenth_percent.Clear() 
                        dlg.txttech_skills.Clear() 
                        dlg.txtit_organization.Clear() 
                        dlg.txtit_description.Clear() 
                        dlg.txtit_duration.Clear() 
                        dlg.txtit_role.Clear() 
                        dlg.txtmi_organization.Clear() 
                        dlg.txtmi_description.Clear() 
                        dlg.txtmi_duration.Clear() 
                        dlg.txtmi_role.Clear() 
                        dlg.txtma_organization.Clear() 
                        dlg.txtma_description.Clear() 
                        dlg.txtma_duration.Clear() 
                        dlg.txtma_role.Clear() 
                        dlg.txtec_activities.Clear() 
                        dlg.txtachievements.Clear() 
                        dlg.txtstrength.Clear() 
                        dlg.txtweakness.Clear() 
                        dlg.txthobbies.Clear() 
                        dlg.txtdob.Clear() 
                        dlg.cbgender.Clear() 
                        dlg.txtnationality.Clear() 
                        dlg.cbmaritalstatus.Clear() 
                        dlg.txtlang_known.Clear() 
                        dlg.txtmother_tongue.Clear() 
                        dlg.txtfathers_name.Clear() 
                        dlg.txthod_name.Clear() 
                        dlg.txtdate.Clear() 
                        dlg.cbyear.Clear()
                        #dlg.txtpassword.Clear()
                        #dlg.txtrenter_password.Clear() 

                        dlg2 = wx.MessageDialog( self, "Student Record updated", "student", wx.OK) 
                        dlg2.ShowModal() # Show it 
                        dlg2.Destroy() # finally destroy it when finished. 
                finally: 
                        dlg.Destroy() 
        cursor.close() 
        connection.close() 
    dialog.Destroy()

def OnMenuFileEditMenu(self, event):
    dialog = wx.TextEntryDialog(None,"Enrollment no.?","Edit Student Record", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE Enrollment_no = '" + searchVal + "'" 
        cursor.execute(sql) 
        recordset = cursor.fetchall() 
        if len(recordset) == 0: 
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
            dlg2 = wx.MessageDialog( self, "Student Record not found", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        else:
            # Write the user input to the CustomDlg text boxes. 
            for (Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address,city,state,pin,email_id,\
phno,college_name,affiliated_to,current_cgpa,twelth_percent,tenth_percent,tech_skills,it_organization,it_description,it_duration,\
it_role,mi_organization,mi_description,mi_duration,mi_role,ma_organization,ma_description,ma_duration,ma_role,ec_activities,achievements,\
strength,weakness,hobbies,dob,gender,nationality,marital_status,lang_known,mother_tongue,fathers_name,hod_name,date,year) in recordset: 
                dlg = CustomDlg.Dialog1(self) 
                dlg.txtEnrollment_no.Value = "%s" % Enrollment_no 
                dlg.txtFirst_Name.Value = "%s" % First_Name
                dlg.txtMiddle_Name.Value = "%s" % Middle_Name
                dlg.txtLast_Name.Value = "%s" % Last_Name
                dlg.txtObjective.Value = "%s" % Objective
                dlg.txtAddress.Value = "%s" % Address
                dlg.txtcity.Value = "%s" % city
                dlg.txtstate.Value = "%s" % state
                dlg.txtpin.Value = "%s" % pin
                dlg.txtemail_id.Value = "%s" % email_id
                dlg.txtphno.Value = "%s" % phno
                dlg.txtcollege_name.Value = "%s" % college_name
                dlg.txtaffiliated_to.Value = "%s" % affiliated_to
                dlg.txtcurrent_cgpa.Value = "%s" % current_cgpa
                dlg.txttwelth_percent.Value = "%s" % twelth_percent
                dlg.txttenth_percent.Value = "%s" % tenth_percent
                dlg.txttech_skills.Value = "%s" % tech_skills
                dlg.txtit_organization.Value = "%s" % it_organization
                dlg.txtit_description.Value = "%s" % it_description
                dlg.txtit_duration.Value = "%s" % it_duration
                dlg.txtit_role.Value = "%s" % it_role
                dlg.txtmi_organization.Value = "%s" % mi_organization
                dlg.txtmi_description.Value = "%s" % mi_description
                dlg.txtmi_duration.Value = "%s" % mi_duration
                dlg.txtmi_role.Value = "%s" % mi_role
                dlg.txtma_organization.Value = "%s" % ma_organization
                dlg.txtma_description.Value = "%s" % ma_description
                dlg.txtma_duration.Value = "%s" % ma_duration
                dlg.txtma_role.Value = "%s" % ma_role
                dlg.txtec_activities.Value = "%s" % ec_activities
                dlg.txtachievements.Value = "%s" % achievements
                dlg.txtstrength.Value = "%s" % strength
                dlg.txtweakness.Value = "%s" % weakness
                dlg.txthobbies.Value = "%s" % hobbies
                dlg.txtdob.Value = "%s" % dob
                dlg.txtgender.Value = "%s" % gender
                dlg.txtnationality.Value = "%s" % nationality
                dlg.txtmarital_status.Value = "%s" % marital_status
                dlg.txtlang_known.Value = "%s" % lang_known
                dlg.txtmother_tongue.Value = "%s" % mother_tongue
                dlg.txtfathers_name.Value = "%s" % fathers_name
                dlg.txthod_name.Value = "%s" % hod_name
                dlg.txtdate.Value = "%s" % date
                dlg.txtyear.Value = "%s" % year
                try: 
                    if dlg.ShowModal() == wx.ID_OK: 
                        Enrollment_no = dlg.txtEnrollment_no.GetValue() 
                        First_Name = dlg.txtFirst_Name.GetValue() 
                        Middle_Name = dlg.txtMiddle_Name.GetValue() 
                        Last_Name = dlg.txtLast_Name.GetValue() 
                        Objective = dlg.txtObjective.GetValue() 
                        Address = dlg.txtAddress.GetValue() 
                        city=dlg.txtcity.GetValue()
                        state=dlg.txtstate.GetValue()
                        pin=dlg.txtpin.GetValue()
                        email_id=dlg.txtemail_id.GetValue()
                        phno=dlg.txtphno.GetValue()
                        college_name=dlg.txtcollege_name.GetValue()
                        affiliated_to=dlg.txtaffiliated_to.GetValue()
                        current_cgpa=dlg.txtcurrent_cgpa.GetValue()
                        twelth_percent=dlg.txttwelth_percent.GetValue()
                        tenth_percent=dlg.txttenth_percent.GetValue()
                        tech_skills=dlg.txttech_skills.GetValue()
                        it_organization=dlg.txtit_organization.GetValue()
                        it_description=dlg.txtit_description.GetValue()
                        it_duration=dlg.txtit_duration.GetValue()
                        it_role=dlg.txtit_role.GetValue()
                        mi_organization=dlg.txtmi_organization.GetValue()
                        mi_description=dlg.txtmi_description.GetValue()
                        mi_duration=dlg.txtmi_duration.GetValue()
                        mi_role=dlg.txtmi_role.GetValue()
                        ma_organization=dlg.txtma_organization.GetValue()
                        ma_description=dlg.txtma_description.GetValue()
                        ma_duration=dlg.txtma_duration.GetValue()
                        ma_role=dlg.txtma_role.GetValue()
                        ec_activities=dlg.txtec_activities.GetValue()
                        achievements=dlg.txtachievements.GetValue()
                        strength=dlg.txtstrength.GetValue()
                        weakness=dlg.txtweakness.GetValue()
                        hobbies=dlg.txthobbies.GetValue()
                        dob=dlg.txtdob.GetValue()
                        gender=dlg.txtgender.GetValue()
                        nationality=dlg.txtnationality.GetValue()
                        marital_status=dlg.txtmarital_status.GetValue()
                        lang_known=dlg.txtlang_known.GetValue()
                        mother_tongue=dlg.txtmother_tongue.GetValue()
                        fathers_name=dlg.txtfathers_name.GetValue()
                        hod_name=dlg.txthod_name.GetValue()
                        date=dlg.txtdate.GetValue()
                        year=dlg.txtyear.GetValue()


                        connection = sqlite3.connect('student.db') 
                        cursor = connection.cursor() 
                        cursor.execute("UPDATE student SET Enrollment_no ='" + Enrollment_no + "', First_Name ='" + First_Name +"', Middle_Name ='" + Middle_Name + "', Last_Name ='" + Last_Name + "', Objective ='" + Objective +"',Address ='" + Address +"',city='"+city+"',state='"+state+"',pin='"+pin+"',email_id='"+email_id+\
"',phno='"+phno+"',college_name='"+college_name+"',affiliated_to='"+affiliated_to+"',current_cgpa='"+current_cgpa+"',twelth_percent='"+twelth_percent+"',tenth_percent='"+tenth_percent+"',tech_skills='"+tech_skills+"',it_organization='"+it_organization+"',it_description='"+it_description+"',it_duration='"+it_duration+"',it_role='"+it_role+"',mi_organization='"+mi_organization+"',mi_description='"+mi_description+"',mi_duration='"+mi_duration+"',mi_role='"+mi_role+"',ma_organization='"+ma_organization+"',ma_description='"+ma_description+"',ma_duration='"+ma_duration+"',ma_role='"+ma_role+"',ec_activities='"+ec_activities+"',achievements='"+achievements+"',strength='"+strength+"',weakness='"+weakness+"',hobbies='"+hobbies+"',dob='"+dob+"',gender='"+gender+"',nationality='"+nationality+"',marital_status='"+marital_status+"',lang_known='"+lang_known+"',mother_tongue='"+mother_tongue+"',fathers_name='"+fathers_name+"',hod_name='"+hod_name+"',date='"+date+"',year='"+year+"' WHERE Enrollment_no='" + searchVal + "'")
                        
                        connection.commit() 
                        dlg.txtEnrollment_no.Clear() 
                        dlg.txtFirst_Name.Clear() 
                        dlg.txtMiddle_Name.Clear() 
                        dlg.txtLast_Name.Clear() 
                        dlg.txtObjective.Clear() 
                        dlg.txtAddress.Clear() 
                        dlg.txtcity.Clear() 
                        dlg.txtstate.Clear() 
                        dlg.txtpin.Clear() 
                        dlg.txtemail_id.Clear() 
                        dlg.txtphno.Clear() 
                        dlg.txtcollege_name.Clear() 
                        dlg.txtaffiliated_to.Clear() 
                        dlg.txtcurrent_cgpa.Clear() 
                        dlg.txttwelth_percent.Clear() 
                        dlg.txttenth_percent.Clear() 
                        dlg.txttech_skills.Clear() 
                        dlg.txtit_organization.Clear() 
                        dlg.txtit_description.Clear() 
                        dlg.txtit_duration.Clear() 
                        dlg.txtit_role.Clear() 
                        dlg.txtmi_organization.Clear() 
                        dlg.txtmi_description.Clear() 
                        dlg.txtmi_duration.Clear() 
                        dlg.txtmi_role.Clear() 
                        dlg.txtma_organization.Clear() 
                        dlg.txtma_description.Clear() 
                        dlg.txtma_duration.Clear() 
                        dlg.txtma_role.Clear() 
                        dlg.txtec_activities.Clear() 
                        dlg.txtachievements.Clear() 
                        dlg.txtstrength.Clear() 
                        dlg.txtweakness.Clear() 
                        dlg.txthobbies.Clear() 
                        dlg.txtdob.Clear() 
                        dlg.txtgender.Clear() 
                        dlg.txtnationality.Clear() 
                        dlg.txtmarital_status.Clear() 
                        dlg.txtlang_known.Clear() 
                        dlg.txtmother_tongue.Clear() 
                        dlg.txtfathers_name.Clear() 
                        dlg.txthod_name.Clear() 
                        dlg.txtdate.Clear() 
                        dlg.txtyear.Clear() 

                        dlg2 = wx.MessageDialog( self, "Student Record updated", "student", wx.OK) 
                        dlg2.ShowModal() # Show it 
                        dlg2.Destroy() # finally destroy it when finished. 
                finally: 
                        dlg.Destroy() 
        cursor.close() 
        connection.close() 
    dialog.Destroy()


def OnSeeResume(self, event):
    dialog = wx.TextEntryDialog(None,"Enrollment no.?","See Resume ", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE Enrollment_no = '" + searchVal + "'" 
        cursor.execute(sql) 
        recordset = cursor.fetchall()
        cursor.close() 
        if len(recordset) == 0: 
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
            dlg2 = wx.MessageDialog( self, "Student Record not found", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        else:
            #webbrowser.open('file:///home/ashmeet/python/student/resumetemp.tpl')
     
    
            def StartServer(self):
                thread.start_new_thread(self._Serve, ())
    
            def _Serve(self):
                print "starting server thread..."
    
            @route('/')
            def index():
                output=template('resumetemp',rows=recordset)
                return output
                #return '<b>enrollment no is</b> %s' % searchVal
                 #webbrowser.open('file:///home/ashmeet/python/student/resumetemp.tpl')
            run(host='localhost',port=8080)
        #else:
    
            #pos = self.GetPosition()
            #self.childFrame.Move(pos)
            #self.childFrame.Show()
            #self.Hide()



            #for row in recordset:
            #    Enrollment_no = row[0]
            #    First_Name = row[1]
            #    Middle_Name = row[2]
            #    Last_Name = row[3]
            #    Objective = row[4]
            #    Address = row[5]
            #    # Now print fetched result
            #    print "Enrollment no=%s,First Name=%s,Middle Name=%s,Last Name=%s,Objective=%s,Address=%s" %(Enrollment_no,First_Name,Middle_Name,Last_Name,Objective,Address)
                
            #output=template('resumetemp',rows=recordset)
            #return output
            ##return '<b>app data is</b> %s' % self.currentData





def OnSeeAllRecords(self, event):
    dialog = wx.TextEntryDialog(None,"Cut Off?","See All Data ", "", style=wx.OK|wx.CANCEL) 
    if dialog.ShowModal() == wx.ID_OK: 
        searchVal = dialog.GetValue() 
        connection = sqlite3.connect('student.db') 
        cursor = connection.cursor() 
        sql = "SELECT * FROM student WHERE current_cgpa >= '" + searchVal + "'" 
        cursor.execute(sql) 
        above_avg = cursor.fetchall()
        sql = "SELECT * FROM student WHERE current_cgpa < '" + searchVal + "'" 
        cursor.execute(sql) 
        below_avg = cursor.fetchall()
        cursor.close() 
        if len(above_avg) == 0 and len(below_avg)==0: 
            # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets. 
            dlg2 = wx.MessageDialog( self, "No Student In This Category", "student", wx.OK) 
            dlg2.ShowModal() # Show it 
            dlg2.Destroy() # finally destroy it when finished. 
        else:
     
    
            def StartServer(self):
                thread.start_new_thread(self._Serve, ())
    
            def _Serve(self):
                print "starting server thread..."
    
            @route('/')
            def index():
                output=template('resumetemp1',rows1=above_avg,rows2=below_avg)
                return output
                #return '<b>enrollment no is</b> %s' % searchVal
            run(host='localhost',port=8080)
            #bottle.run(server='gae')



