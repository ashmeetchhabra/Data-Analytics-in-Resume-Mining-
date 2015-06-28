<html>
<body>
<br>
<font size="2">
<div align="right" style="Times New Roman">
%for row in rows:
    %for col in row[1]+row[2]+row[3]:
    <b>{{col}}</b>
    %end
</font>
<br>
<font size="1" style="Times New Roman">
    Address:
    %for col in row[5]:
    {{col}}
    %end
<br> 
Phone no.:
    %for col in row[10]:
    {{col}}
    %end
email id:
    %for col in row[9]:
     {{col}}
    %end
  
%end
</div>
</font>

<hr>
 
<font size="2" style="Times New Roman">
%for row in rows:
   <b>Career Objective:</b>
    %for col in row[4]:
     {{col}}
    %end
 
<br>
<br>
<b>Academic Record:</b>
<br>
<ul>
<li><b>Profesional Qualification:</b></li>
</ul>
<ul style="list-style-type:circle">
<li>Pursuing Bachelor of Engineering from
    %for col in row[11]:
     {{col}}
    %end
Indore affiliated to RGTU with specialization in Computer Science (2008-2012) (Current Average-
   %for col in row[13]:
     {{col}}
    %end
)</li>
</ul>

<ul>
     <li><b>Educational Qualification:</li></b>
</ul>
<ul style="list-style-type:circle">
<li>Senior Secondary School Certificate (10+2) from Board of Secondary Education Bhopal M.P. with
      %for col in row[14]:
        {{col}}
      %end
percent</li>

<li>High School Certificate (10th) from Board of Secondary Education Bhopal M.P. with 
    %for col in row[13]:
     {{col}}
    %end
 percent</li>
</ul>
<b>It Skills:</b>
    %for col in row[16]:
     {{col}}
    %end
<br>
<br>
<b>Training:</b>
<ul>
<li><b>Industrial Training:</b></li>
Organization:
    %for col in row[17]:
     {{col}}
    %end
<br>
Description:
    %for col in row[18]:
     {{col}}
    %end
<br>
Duration:
    %for col in row[19]:
     {{col}}
    %end
<br>
Role:
    %for col in row[20]:
     {{col}}
    %end
<br>
<li><b>Minor Project:</b></li>
Organization:
    %for col in row[21]:
     {{col}}
    %end
<br>
Description:
    %for col in row[22]:
     {{col}}
    %end
<br>
Duration:
    %for col in row[23]:
     {{col}}
    %end
<br>
Role:
    %for col in row[24]:
     {{col}}
    %end
<br>
<li><b>Major Project:</b></li>
Organization:
    %for col in row[25]:
     {{col}}
    %end
<br>
Description:
    %for col in row[26]:
     {{col}}
    %end
<br>
Duration:
    %for col in row[27]:
     {{col}}
    %end
<br>
Role:
    %for col in row[28]:
     {{col}}
    %end
<br></ul>
<b>Extracurricular Activities:</b>
    %for col in row[29]:
     {{col}}
    %end
<br><br>
<b>Achievements</b>
    %for col in row[30]:
     {{col}}
    %end
<br><br>
<b>Strengths</b>
    %for col in row[31]:
     {{col}}
    %end
<br><br>
<b>Weakness</b>
    %for col in row[32]:
     {{col}}
    %end
<br><br>
<b>Hobbies</b>
    %for col in row[33]:
     {{col}}
    %end
<br><br>
<b>Personal Details:</b>
<br>
Date of Birth:
    %for col in row[34]:
     {{col}}
    %end
<br>
Gender:
    %for col in row[35]:
     {{col}}
    %end
<br>
Nationality:
    %for col in row[36]:
     {{col}}
    %end
<br>
Marital Status:
    %for col in row[37]:
     {{col}}
    %end
<br>
Language Known:
    %for col in row[38]:
     {{col}}
    %end
<br>
Mother Tongue:
    %for col in row[39]:
     {{col}}
    %end
<br>
Father's Name:
    %for col in row[40]:
     {{col}}
    %end
<br><br>
<b>References:</b>
Prof.
    %for col in row[41]:
     {{col}}
    %end
,
    %for col in row[11]:
     {{col}}
    %end
<br><br>
<b>Declaration</b>
I hereby declare that the information furnished above is true to the best of my knowledge.
<br>
Date:
    %for col in row[42]:
     {{col}}
    %end
<br>
Place:
    %for col in row[6]:
     {{col}}
    %end
<br>
<div align="right"><b>
    %for col in row[1]+row[2]+row[3]:
     {{col}}
    %end
</b></div>





</ul>
%end
</font>

</body>
</html>
